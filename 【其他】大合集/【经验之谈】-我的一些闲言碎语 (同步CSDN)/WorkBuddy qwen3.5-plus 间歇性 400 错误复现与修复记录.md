# WorkBuddy qwen3.5-plus 间歇性 400 错误复现与修复记录

记录时间：2026-07-31 19:43:50 +08:00

## 问题现象

WorkBuddy 使用自定义模型 `qwen3.5-plus` 时，请求有时成功，有时报错。

用户侧看到的错误大致如下：

```text
自定义模型 qwen3.5-plus 错误，请切换模型或重试。
400 Invalid request: Invalid request: invalid character 'P' looking for beginning of value
```

典型错误信息：

```text
Error Code: 0
Server Detail: {"code":-32603,"message":"Internal error","data":{"code":0,"message":"Invalid request: Invalid request: invalid character 'P' looking for beginning of value", ...}}
```

## 复现方式

在 WorkBuddy 中选择自定义模型 `qwen3.5-plus`，连续发送简单消息，例如：

```text
你好
稳定性测试1
稳定性测试2
稳定性测试3
```

观察结果：

- 有些请求正常返回。
- 有些请求在模型请求阶段直接失败。
- 失败时没有工具调用，没有文件修改，也没有进入模型流式输出阶段。

相关日志文件：

```text
C:\Users\lin junrui\.workbuddy\logs\2026-07-31\vllm__d1ee656142eedd58cf2c6b585f074d02.log
```

失败日志片段示例：

```text
[ModelProvider] Sending request: agent=cli, model=custom-local:qwen3.5-plus, stream=true, url=http://yclk158.w3design.cn:52301/v1/chat/completions
[ProxyResolver] L0 PAC: http://yclk158.w3design.cn:52301/v1/chat/completions -> http://127.0.0.1:7897/
[ModelProvider] Request failed: error=Request failed with status code 400
400 Invalid request: Invalid request: invalid character 'P' looking for beginning of value
```

成功日志片段示例：

```text
[ModelProvider] First raw chunk received
[ModelProvider] Stream completed
[ACP Agent] RESULT: completed successfully, stopReason=end_turn, finishReason=stop
```

## 定位过程

### 1. 排除模型配置 JSON 语法问题

执行：

```powershell
Get-Content models.json | ConvertFrom-Json
```

结果：`models.json` 可正常解析。

### 2. 排除 API Key 或上游接口完全不可用

直接向上游接口发送非流式请求，连续 12 次全部成功。

结论：

- API Key 不是完全失效。
- 上游接口不是完全不可用。
- 问题不是简单的“模型挂了”。

### 3. 测试流式请求与代理

显式通过本地代理 `127.0.0.1:7897` 发送 `stream=true` 请求，连续 15 次成功。

结论：

- 普通流式请求本身可以成功。
- 代理不是单独必然导致失败。

### 4. 验证模型名差异

直接测试两个模型名：

```text
qwen3.5-plus
custom-local:qwen3.5-plus
```

结果：

- `qwen3.5-plus` 连续成功。
- `custom-local:qwen3.5-plus` 被上游拒绝，返回 403。

关键发现：

WorkBuddy 在内部会把自定义模型请求里的模型名变成：

```text
custom-local:qwen3.5-plus
```

但上游接口更稳定接受的是：

```text
qwen3.5-plus
```

## 根因判断

这次问题的核心不是 UI、文件夹、工具调用或 API Key。

更可能的根因是：

```text
WorkBuddy 自定义模型内部名 custom-local:qwen3.5-plus 与上游 OpenAI-compatible 接口的模型名兼容性不好。
```

同时日志里还出现过：

```text
ECONNRESET
```

说明链路偶尔也有网络层抖动。因此最终方案同时处理两件事：

- 把 WorkBuddy 传出的 `custom-local:qwen3.5-plus` 改写为上游认识的 `qwen3.5-plus`。
- 对偶发网络或上游解析失败做少量重试。

## 解决方案

新增一个本机兼容代理：

```text
C:\Users\lin junrui\.workbuddy\workbuddy-qwen-proxy.mjs
```

代理监听：

```text
http://127.0.0.1:53180/v1/chat/completions
```

代理转发到真实上游：

```text
http://yclk158.w3design.cn:52301/v1/chat/completions
```

代理做的事情：

- 接收 WorkBuddy 的请求。
- 如果请求体里的 `model` 是 `custom-local:qwen3.5-plus`，自动改成 `qwen3.5-plus`。
- 保持流式响应，不破坏 WorkBuddy 的 SSE 读取方式。
- 对部分网络错误或上游临时错误最多重试 3 次。

### models.json 修改

`qwen3.5-plus` 的配置改为：

```json
{
  "id": "qwen3.5-plus",
  "name": "qwen3.5-plus",
  "vendor": "Custom",
  "url": "http://127.0.0.1:53180/v1/chat/completions",
  "upstreamUrl": "http://yclk158.w3design.cn:52301/v1/chat/completions",
  "apiKey": "<真实 API Key，不要写进文档或截图>",
  "supportsToolCall": false,
  "supportsImages": false,
  "supportsReasoning": false,
  "useCustomProtocol": false
}
```

说明：

- `url` 指向本机代理。
- `upstreamUrl` 保留真实上游地址。
- `apiKey` 仍由本机代理读取并转发，不应公开。
- `supportsToolCall` 设为 `false`，避免 WorkBuddy 给该模型发送工具调用字段。
- `supportsImages` 设为 `false`，避免发送图片能力字段。

## 端口选择说明

最初尝试使用端口 `52302`，但 Windows 报错：

```text
listen EACCES: permission denied 127.0.0.1:52302
```

检查 Windows TCP 保留端口后发现：

```text
52226-52325
```

这段端口被系统保留，因此改用：

```text
53180
```

## 启动方式

当前代理通过 Node.js 启动：

```powershell
node C:\Users\lin junrui\.workbuddy\workbuddy-qwen-proxy.mjs
```

为了避免每次重启电脑后手动启动，已创建 Windows 当前用户启动项：

```text
C:\Users\lin junrui\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\WorkBuddy Qwen Proxy.lnk
```

这样登录 Windows 后，本机代理会自动启动。

## 验证结果

### 本机代理验证

向本机代理发送请求：

```text
model = custom-local:qwen3.5-plus
url = http://127.0.0.1:53180/v1/chat/completions
stream = true
```

结果：

```text
HTTP 200
```

### WorkBuddy UI 验证

在 WorkBuddy 真实界面里连续发送：

```text
代理修复验证1
代理修复验证2
代理修复验证3
```

结果全部成功：

```text
代理修复验证 1 通过。
代理修复验证 2 通过。
代理修复验证 3 通过。
```

### WorkBuddy 日志验证

修复后日志显示 WorkBuddy 已经使用本机代理：

```text
Using custom URL for model custom-local:qwen3.5-plus: http://127.0.0.1:53180/v1/chat/completions
ProxyResolver L0 PAC: http://127.0.0.1:53180/v1/chat/completions -> DIRECT
First raw chunk received
Stream completed
RESULT: completed successfully
```

修复后没有再出现新的：

```text
invalid character 'P' looking for beginning of value
```

## 后续维护

如果之后又出现问题，优先检查：

### 1. 代理是否在监听

```powershell
netstat -ano | Select-String 53180
```

看到类似结果表示代理正在运行：

```text
127.0.0.1:53180 LISTENING
```

### 2. WorkBuddy 是否仍指向本机代理

检查：

```text
C:\Users\lin junrui\.workbuddy\models.json
```

确认 `qwen3.5-plus` 的 `url` 是：

```text
http://127.0.0.1:53180/v1/chat/completions
```

### 3. 启动项是否还在

检查：

```text
C:\Users\lin junrui\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\WorkBuddy Qwen Proxy.lnk
```

### 4. API Key 是否泄露或过期

如果真实 API Key 曾经出现在聊天、截图或日志外发材料里，建议在上游平台轮换 API Key。

本记录刻意没有写入真实 API Key。

## 二次故障：代理未启动导致 502

### 现象

2026-07-31 20:54 左右再次出现错误，但错误类型已经变化：

```text
Error Code: 3002
Network error: 502 连接被拒绝
connect ECONNREFUSED 127.0.0.1:53180
```

这说明 WorkBuddy 已经正确请求本机代理：

```text
http://127.0.0.1:53180
```

但当时本机代理没有监听该端口。

### 复现/检查

执行：

```powershell
netstat -ano | Select-String ':53180'
```

如果没有看到：

```text
127.0.0.1:53180 LISTENING
```

就表示本机代理没有运行。

### 原因

最初的修复只启动了一次代理，并创建了 Windows 登录启动项。

问题在于：

- 当前会话里代理进程可能退出后不会自动恢复。
- 启动项直接启动 Node，没有守护能力。
- 用户目录包含空格：`C:\Users\lin junrui`。
- PowerShell `-File` 参数如果没有正确加引号，会被截断成 `C:\Users\lin`，导致 watchdog 启动失败。

### 加固修复

新增 watchdog：

```text
C:\Users\lin junrui\.workbuddy\workbuddy-qwen-proxy-watchdog.ps1
```

watchdog 的作用：

- 启动 `workbuddy-qwen-proxy.mjs`。
- 等待代理进程。
- 如果代理退出，记录日志并在 3 秒后自动重启。

watchdog 日志：

```text
C:\Users\lin junrui\.workbuddy\workbuddy-qwen-proxy-watchdog.log
```

代理自身日志：

```text
C:\Users\lin junrui\.workbuddy\workbuddy-qwen-proxy.log
```

Windows 启动项现在指向：

```text
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
```

启动参数：

```powershell
-NoProfile -ExecutionPolicy Bypass -File "C:\Users\lin junrui\.workbuddy\workbuddy-qwen-proxy-watchdog.ps1"
```

注意：`-File` 后面的路径必须带英文双引号，否则路径里的空格会导致启动失败。

### 当前验证

修复后再次检查：

```powershell
netstat -ano | Select-String ':53180'
```

结果：

```text
127.0.0.1:53180 LISTENING
```

向本机代理发送 `custom-local:qwen3.5-plus` 流式请求：

```text
HTTP 200
```

watchdog 日志显示：

```text
watchdog started
starting proxy
proxy pid=9680
```
