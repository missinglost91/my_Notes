## 第一章配置环境

> 以下操作均在 AutoDL 等带数据盘（`/root/autodl-tmp`）的 Linux 环境下进行，目标是把所有缓存挪到数据盘，避免系统盘被打满。

### 1-1 安装 uv

```bash
pip install uv
```

### 1-2 配置 uv 缓存路径

```bash
mkdir -p /root/autodl-tmp/uv-cache
echo 'export UV_CACHE_DIR="/root/autodl-tmp/uv-cache"' >> ~/.bashrc
source ~/.bashrc
uv cache dir          # 验证输出是否指向新路径
```

### 1-3 创建 vLLM 虚拟环境

```bash
cd ~
uv init vllm
cd vllm
uv venv
```

### 1-4 创建数据盘缓存目录

```bash
mkdir -p /root/autodl-tmp/huggingface_cache /root/autodl-tmp/vllm_cache
```

### 1-5 配置环境变量

一次性写入 `~/.bashrc`，涵盖 HuggingFace 缓存、vLLM 缓存、国内镜像、XET 兼容性：

```bash
# 1. Hugging Face 模型缓存路径
echo 'export HF_HOME=/root/autodl-tmp/huggingface_cache' >> ~/.bashrc
echo 'export HUGGINGFACE_HUB_CACHE=$HF_HOME' >> ~/.bashrc
echo 'export TRANSFORMERS_CACHE=$HF_HOME' >> ~/.bashrc

# 2. vLLM 编译缓存路径
echo 'export VLLM_CACHE_ROOT=/root/autodl-tmp/vllm_cache' >> ~/.bashrc

# 3. HF 国内镜像（解决下载超时）
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc

# 4. 关闭 XET 相关特性（解决 401 报错 / 下载失败）
echo 'export HF_HUB_DISABLE_XET=1' >> ~/.bashrc
echo 'export HF_HUB_ENABLE_HF_TRANSFER=0' >> ~/.bashrc
echo 'export HF_HUB_ENABLE_XET_STORAGE=0' >> ~/.bashrc

# 5. 立即生效
source ~/.bashrc
```

### 1-6 安装 vLLM 与 PyTorch

```bash
unset UV_TORCH_BACKEND

UV_HTTP_TIMEOUT=300 uv pip install vllm==0.23.0 \
  -i https://mirrors.aliyun.com/pypi/simple \
  --extra-index-url https://mirrors.aliyun.com/pytorch-wheels \
  --index-strategy unsafe-best-match
```

### 1-7 验证配置

```bash
env | grep HF_HOME
env | grep VLLM_CACHE_ROOT
```
激活环境
```bash
source .venv/bin/activate
vllm -v
```

### 1-8 下载模型并启动服务

推荐用 ModelScope（国内速度快）下载模型：

![20260730231729](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260730231729.png)
```bash
pip install modelscope
```

```bash
# 下载 Qwen2.5-7B-Instruct 到数据盘
modelscope download   --model Qwen/Qwen2.5-7B-Instruct  --local_dir /root/autodl-tmp/models/Qwen2.5-7B-Instruct
```

```bash
# 用本地路径启动 vLLM 服务（--trust-remote-code 允许加载自定义模型代码）
vllm serve /root/autodl-tmp/models/Qwen2.5-7B-Instruct --trust-remote-code
```


## 第二章： 前置知识基础
### 2-1 pytorch基础

### 2-1-1 模型前向传播
下面是一个常见的卷积神经网络的源码

```python
class Tudui(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.model(x)
        return x

#***省略其他代码***
tudui = Tudui().to(device)
tudui.train()
for data in train_dataloader:
    imgs, targets = data
    # pin_memory=True后，这里可以设置 non_blocking=True 进一步优化
    imgs = imgs.to(device, non_blocking=True)
    targets = targets.to(device, non_blocking=True)
    outputs = tudui(imgs)
#***省略其他代码***
```

**1. 模型初始化：`tudui = Tudui().to(device)`**

- `Tudui.__init__` 中调用了 `super().__init__()`，因此继承了 `nn.Module` 的所有属性和方法
- 随后通过 `self.model = nn.Sequential(...)` 把一系列网络层注册为子模块

**2. 前向调用：`tudui(imgs)`**

PyTorch 中实例像函数一样被调用，背后依赖 `nn.Module.__call__`，它等价于：

```python
tudui(imgs)  ≡  tudui.forward(imgs)
```

而 `Tudui.forward` 的实现是：

```python
def forward(self, x):
    x = self.model(x)
    return x
```

所以最终执行的是 `self.model(imgs)`，即把 `imgs` 依次送入 `nn.Sequential` 中定义的各层（Conv → Pool → … → Linear）进行加工，最后返回输出 `outputs`。

> 一句话总结：`tudui(imgs)` → `__call__` → `forward(imgs)` → `self.model(imgs)` → 逐层计算 → 输出。

### 2-2 训练模式 vs 推理模式

学 vLLM 时，这两个方法必须分清：

| 方法              | 作用         | Dropout  | BatchNorm              |
| --------------- | ---------- | -------- | ---------------------- |
| `model.train()` | 切到**训练模式** | 生效（随机丢弃） | 使用当前 batch 统计量         |
| `model.eval()`  | 切到**推理模式** | 关闭（不丢弃）  | 使用训练时累计的 running stats |

> vLLM 是纯推理框架，所以模型加载后始终处于 `eval()` 语义，不会调用 `train()`。

### 2-3 `nn.Module` 常用方法速查

| 方法                                    | 作用              | 常见用法 / 说明                                                                                                          |
| ------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------ |
| `model.to(device)`                    | 移动模型到指定设备 / 改精度 | `model.to("cuda")`、`model.cuda()`、`model.cpu()`、`model.to(dtype=torch.bfloat16)`。大模型推理里这一步很关键，参数会被放到 GPU/XPU/CPU 上 |
| `model.parameters()`                  | 返回所有可训练参数       | `for p in model.parameters(): print(p.shape)`。常用于构造优化器、统计参数量、冻结/解冻参数                                               |
| `model.named_parameters()`            | 返回 `(名字, 参数)` 对 | `for name, p in model.named_parameters(): ...`。调试大模型结构、在 vLLM 里定位某个权重时特别有用                                         |
| `model.buffers()` / `named_buffers()` | 返回非参数但会随模型保存的张量 | 如 BatchNorm 的 running mean/var、某些缓存状态                                                                              |
| `model.state_dict()`                  | 导出模型全部状态        | 包含所有参数和 buffer，是保存/加载模型最常用的方法之一                                                                                    |
| `model.load_state_dict(sd)`           | 加载参数            | 大模型推理框架的常规套路：先构建网络结构，再把 checkpoint 权重灌进去。vLLM 实现更复杂，但逻辑大体一致                                                        |
| `model.requires_grad_(flag)`          | 控制是否需要梯度        | 推理时常用 `model.requires_grad_(False)` 冻结参数                                                                           |
| `model.zero_grad()`                   | 清空梯度            | 训练里常用，推理里一般不重要                                                                                                     |

### 2-4 PyTorch「模型相关」核心概念

**子模块注册**：只要把层写成 `self.xxx = nn.Linear(...)`，PyTorch 就会自动把它当成子模块，出现在 `parameters()` / `state_dict()` / `to(device)` 中；写成普通变量则不会被管理。

```python
class M(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(10, 20)   # 自动注册
        self.l2 = nn.Linear(20, 1)
```

**参数注册**：`nn.Parameter` 会自动被识别为可训练参数，常用于自定义层。

```python
self.scale = nn.Parameter(torch.tensor(1.0))
```

**前向传播**：`forward()` 是计算图的主干。

```python
def forward(self, x):
    x = self.l1(x)
    x = torch.relu(x)
    return self.l2(x)
```

在 vLLM 中，可以把「模型前向」理解为：输入 token → embedding → transformer layers → 输出 logits / hidden states。

### 2-5 推理与训练的标准写法

**推理标准写法**

```python
model.eval()                  # 关闭训练态行为（Dropout / BatchNorm）
with torch.no_grad():         # 不构建梯度图，省显存、省时间
    y = model(x)
```

**训练标准写法**

```python
model.train()                         # 切到训练模式（Dropout 生效、BatchNorm 用 batch 统计）
y = model(x)                          # 前向传播，得到模型预测值
loss = criterion(y, target)           # 用损失函数计算预测值与真实标签的误差
loss.backward()                       # 反向传播，自动求出每个参数的梯度
optimizer.step()                      # 根据梯度更新参数（真正“学习”的一步）
optimizer.zero_grad()                 # 清空梯度，防止与下一个 batch 的梯度累加
```

### 2-6 读 vLLM 源码时最该关注的模型操作

- `model.eval()` —— 推理服务基本都在评估模式
- `model.to(device)` —— 权重被放到特定设备上
- `state_dict()` / `load_state_dict()` —— 权重加载、检查点恢复
- 子模块嵌套 —— 一个大模型里有很多 layers、attention、mlp
- `forward()` 的输入输出 —— vLLM 会围绕这个接口做封装、调度、批处理、缓存优化




## 第三章： vllm最简单的使用与部署

离线的推理代码

```python
from vllm import LLM, SamplingParams
llm = LLM(model="Qwen/Qwen2.5-7B-Instruct")
params = SamplingParams(temperature=0.7, max_tokens=256)
prompts = [
 "解释什么是梯度下降",
 "Python 装饰器怎么用？",
 "什么是 Transformer 的注意力机制？",
 "Docker 和虚拟机的区别是什么？",
 "HTTP 和 HTTPS 的区别？",
]
# vLLM 自动做 Continuous Batching，效率远高于逐条推理
outputs = llm.generate(prompts, params)
for output in outputs:
 print(f"Q: {output.prompt}")
 print(f"A: {output.outputs[0].text}")
 print("---")

```
每个 `output` 对象的结构（源码 `vllm/outputs.py`）：

```text
output.prompt           # str: 原始输入 prompt
output.prompt_token_ids # list[int]: prompt 的 token IDs
output.outputs          # list[CompletionOutput]: 生成结果列表
├── .text               # str: 生成的文本
├── .token_ids          # list[int]: 生成的 token IDs
├── .cumulative_logprob # float: 累积对数概率
├── .finish_reason      # str: 停止原因 ("stop"/"length"/...)
└── .logprobs           # list[dict]: 每个 token 的 logprobs （可选）
```


在线的推理代码


基础启动
```bash
source .venv/bin/activate
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

```text
CLI 子命令
vLLM 的 CLI 定义在 vllm/entrypoints/cli/main.py 中，支持以下子命令：
子命令 说明
vllm serve 启动 OpenAI 兼容 API 服务器
vllm chat 交互式聊天
vllm complete 交互式文本补全
vllm bench 基准测试
vllm collect-env 环境诊断
vllm run-batch 批量运行
```

## 第三章: vllm 的文件夹目录

> vLLM 核心架构深度解析。以下按模块职责划分，逐层拆解。

### 3-1 engine/ —— 核心引擎层

位置：`vllm/engine/`

**关键发现**：这个目录实际上是薄包装层，真正的实现在 `v1/` 子目录中。

主要文件：

| 文件 | 说明 |
| --- | --- |
| `arg_utils.py` | 定义 `EngineArgs` / `AsyncEngineArgs`，解析所有引擎参数 |
| `async_llm_engine.py` | `AsyncLLMEngine`，实际上是 `v1/engine/async_llm.py` 的别名 |
| `llm_engine.py` | `LLMEngine`，实际上是 `v1/engine/llm_engine.py` 的别名 |
| `protocol.py` | 引擎通信协议定义 |

V1 引擎的子目录结构：

```text
v1/
├── attention/           # 注意力后端 (flashinfer, flash_attn, xformers)
├── core/                # 核心调度逻辑
├── engine/              # 引擎核心实现 (LLMEngine, AsyncLLM)
├── executor/            # 执行器 (UniProcExecutor, RayExecutor)
├── fault_tolerance/     # 容错机制
├── kv_offload/          # KV 缓存卸载到 CPU/磁盘
├── metrics/             # 性能指标收集
├── pool/                # 池化操作 (embedding, classification)
├── sample/              # 采样逻辑 (top-p, top-k, temperature)
├── spec_decode/         # 推测解码 (加速推理)
├── structured_output/   # 结构化输出 (JSON/正则/语法约束)
└── worker/              # Worker 管理
```

### 3-2 entrypoints/ —— 入口点层

位置：`vllm/entrypoints/`

这是用户直接接触的 API 层。

核心入口：

| 文件 / 目录 | 功能 |
| --- | --- |
| `llm.py` | **最常用** —— `LLM` 类，离线推理入口 |
| `openai/` | OpenAI 兼容 API 服务器（FastAPI） |
| `anthropic/` | Anthropic 兼容 API |
| `cli/` | 命令行工具（serve, benchmark, launch） |
| `pooling/` | 池化任务（embedding, classification） |
| `generate/` | 文本生成（beam search） |
| `speech_to_text/` | 语音转文本 |
| `scale_out/` | 水平扩展（render, derender） |
| `mcp/` | MCP 协议支持 |
| `grpc_server.py` | gRPC 服务器 |

`LLM` 类核心参数示例：

```python
class LLM:
    def __init__(
        self, model: str,
        *,
        runner: RunnerOption = "auto",           # 运行器类型
        tokenizer: str | None = None,            # 分词器
        tensor_parallel_size: int = 1,           # 张量并行大小
        dtype: ModelDType = "auto",              # 数据类型
        quantization: QuantizationMethods | None = None,  # 量化
        gpu_memory_utilization: float = 0.92,    # GPU 显存利用率
        enforce_eager: bool = False,             # 强制 eager 执行
        ...
    )
```

### 3-3 models/ —— 模型实现层

位置：`vllm/models/`

**平台隔离设计模式**：

```python
# models/deepseek_v4/__init__.py
if current_platform.is_rocm():
    from .amd.model import DeepseekV4ForCausalLM
elif current_platform.is_xpu():
    from .xpu.model import DeepseekV4ForCausalLM
else:  # NVIDIA（默认）
    from .nvidia.model import DeepseekV4ForCausalLM
```

每个平台子目录包含：

| 文件 / 目录 | 说明 |
| --- | --- |
| `model.py` | 主模型定义 |
| `mtp.py` | Multi-Token Prediction 支持 |
| `dspark.py` | DeepSeek 特定优化 |
| `ops/` | 平台特定算子 |

共享代码：

| 路径 | 说明 |
| --- | --- |
| `deepseek_v4/common/` | 跨平台共享（attention, rope, ops） |
| `deepseek_v4/quant_config.py` | 量化配置 |
| `deepseek_v4/sparse_mla.py` | 稀疏 MLA 注意力 |

### 3-4 config/ —— 配置系统

位置：`vllm/config/`

包含 28 个配置类，全部由 `VllmConfig` 统一管理。

核心配置类：

| 配置类 | 功能 |
| --- | --- |
| `VllmConfig` | 统一配置容器，包含所有子配置 |
| `ModelConfig` | 模型配置（model, tokenizer, dtype） |
| `CacheConfig` | KV 缓存配置（block_size, gpu_memory_utilization） |
| `SchedulerConfig` | 调度器配置（max_num_seqs, policy） |
| `ParallelConfig` | 并行配置（TP, DP, EP 大小） |
| `CompilationConfig` | 编译优化（Inductor, CUDA graph） |
| `AttentionConfig` | 注意力后端配置 |
| `LoRAConfig` | LoRA 微调配置 |
| `Quantization` | 量化配置（FP8, AWQ, GPTQ） |
| `SpeculativeConfig` | 推测解码配置 |
| `MultiModalConfig` | 多模态配置 |
| `StructuredOutputsConfig` | 结构化输出配置 |

`CacheConfig` 核心参数：

```python
class CacheConfig:
    block_size: int = 16                       # KV 缓存块大小
    gpu_memory_utilization: float = 0.92       # GPU 显存利用率
    cache_dtype: CacheDType = "auto"           # 缓存数据类型
    enable_prefix_caching: bool = True         # 前缀缓存
    prefix_caching_hash_algo: str = "sha256"   # 哈希算法
```

### 3-5 distributed/ —— 分布式支持

位置：`vllm/distributed/`

核心模块：

| 路径 | 功能 |
| --- | --- |
| `parallel_state.py` | **核心** —— 管理分布式环境（进程组、TP、DP） |
| `communication_op.py` | 通信原语（all_reduce, all_gather） |
| `device_communicators/` | 设备通信器（CUDA, ROCm, CPU, Ray） |
| `kv_transfer/` | KV 缓存传输（LMCache, Mooncake, NIXL） |
| `weight_transfer/` | 权重传输（NCCL-based） |

`parallel_state.py` 核心函数：

```python
init_distributed_environment()   # 初始化分布式环境
initialize_model_parallel()      # 初始化模型并行组
all_reduce(tensor, group_name)   # 跨进程组 all-reduce
all_gather(tensor, dim, ws)      # 跨进程组 all-gather
reduce_scatter(tensor, dim, ws)  # reduce-scatter 操作
```

`kv_transfer` 支持的后端：

```text
kv_transfer/kv_connector/v1/
├── lmcache_connector.py       # LMCache 集成
├── mooncake/                  # Mooncake RDMA 传输
├── nixl/                      # NIXL 传输
├── hf3fs/                     # HF3FS 文件系统
└── moriio/                    # MoriIO 传输
```

### 3-6 kernels/ —— CUDA 内核实现

位置：`vllm/kernels/`

主要子目录：

| 路径 | 功能 |
| --- | --- |
| `vllm_c.py` | 核心 C 内核 —— RMSNorm, FusedAddRMSNorm |
| `triton/` | Triton 内核实现 |
| `helion/` | Helion 编译框架集成 |
| `aiter_ops.py` | AMD AITER 算子 |
| `xpu_ops.py` | Intel XPU 算子 |

`vllm_c.py` 示例：

```python
@ir.ops.rms_norm.register_impl("vllm_c", supports_args=rms_no_var_size)
def rms_norm(x, weight, epsilon, variance_size=None):
    """RMS 归一化 — 调用底层 C 实现"""
    output = torch.empty(x.shape, device=x.device, dtype=x.dtype)
    torch.ops._C.rms_norm(output, x, weight, epsilon)
    return output
```

`helion/ops/` 包含的算子：

| 文件 | 说明 |
| --- | --- |
| `dynamic_per_token_scaled_fp8_quant.py` | FP8 量化 |
| `fused_qk_norm_rope.py` | QK Norm + RoPE 融合 |
| `rms_norm_per_block_quant.py` | 分块 RMSNorm 量化 |
| `silu_and_mul_per_block_quant.py` | SiLU+Mul 融合 |

### 3-7 tokenizers/ —— 分词器层

位置：`vllm/tokenizers/`

核心文件：

| 文件 | 功能 |
| --- | --- |
| `registry.py` | `TokenizerRegistry` —— 分词器注册表 |
| `hf.py` | HuggingFace 分词器封装（线程安全 + 缓存） |
| `protocol.py` | `TokenizerLike` 协议定义 |
| `deepseek_v32.py` | DeepSeek V3.2 专用分词器 |
| `deepseek_v4.py` | DeepSeek V4 专用分词器 |
| `mistral.py` | Mistral 专用分词器 |
| `kimi_audio.py` | Kimi Audio 分词器 |

注册表模式：

```python
_VLLM_TOKENIZERS = {
    "deepseek_v32": ("deepseek_v32", "DeepseekV32Tokenizer"),
    "deepseek_v4": ("deepseek_v4", "DeepseekV4Tokenizer"),
    "hf": ("hf", "CachedHfTokenizer"),
    "kimi_audio": ("kimi_audio", "KimiAudioTokenizer"),
    "mistral": ("mistral", "MistralTokenizer"),
}
```

线程安全实现：

```python
class ThreadSafeHFTokenizerMixin:
    """线程安全的 HF 快速分词器"""

def maybe_make_thread_pool(tokenizer, copies=1):
    """通过深拷贝分词器池实现线程安全"""

def get_cached_tokenizer(tokenizer):
    """缓存 tokenizer 属性加速访问"""
```

### 3-8 完整调用链路

```text
用户代码
  │  from vllm import LLM
  │  llm = LLM("model_name")
  │  outputs = llm.generate()
  ↓
┌─────────────────────────────┐
│ entrypoints/llm.py          │
│ LLM 类                      │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│ engine/ → v1/engine/        │
│ LLMEngine, InputProcessor   │
└──────────────┬──────────────┘
               ↓
    ┌──────────┼──────────┐
    ↓          ↓          ↓
┌────────┐ ┌────────┐ ┌──────────────┐
│ config │ │ models │ │ distributed  │
│ Vllm   │ │ model  │ │ parallel_    │
│ Config │ │ .py    │ │ state.py     │
└────────┘ └────────┘ └──────────────┘
    ↓          ↓          ↓
┌──────────┐ ┌────────┐ ┌────────────┐
│tokenizer │ │kernels │ │ v1/worker  │
│ registry │ │ vllm_c │ │ sample     │
└──────────┘ └────────┘ └────────────┘
```

### 3-9 学习路径建议

作为初学者，建议按以下顺序深入学习：

1. **入门**：`entrypoints/llm.py` → 看 `LLM` 类如何使用
2. **理解引擎**：`v1/engine/llm_engine.py` → 核心调度逻辑
3. **配置系统**：`config/vllm.py` → `VllmConfig` 如何组合配置
4. **模型适配**：`models/` → 看特定模型实现（如 `deepseek_v4/`）
5. **深入优化**：`kernels/vllm_c.py` 和 `kernels/helion/` → 性能优化细节
6. **分布式**：`distributed/parallel_state.py` → 多卡并行原理
## 第四章: vllm 的结构 （离线）

下面是一段最简单的离线推理的代码

```python
# 示例代码
llm = LLM(model="facebook/opt-125m")
outputs = llm.generate(prompts, sampling_params)
print(outputs)
self.model()
```


下面我们来顺着代码来分析

### 第零阶段

```python
# 第 0 阶段：LLM 初始化 —— 搭建推理系统

llm = LLM(model="facebook/opt-125m")  # 用户创建 LLM 对象
    LLM.__init__()  # vllm/entrypoints/llm.py
        engine_args = EngineArgs(...)  # 收集模型名、显存比例、并行配置等参数

        self.llm_engine = LLMEngine.from_engine_args(...)  # 创建 LLMEngine
            vllm_config = engine_args.create_engine_config(...)  # 生成完整 vLLM 配置
            executor_class = Executor.get_class(vllm_config)  # 选择 Executor 类型

            return cls(...)  # cls == LLMEngine，创建 LLMEngine 对象
                LLMEngine.__init__(...)
                    self.input_processor = InputProcessor(...)  # 输入处理：prompt/token → EngineCoreRequest
                    self.output_processor = OutputProcessor(...)  # 输出处理：token id → 文本/RequestOutput

                    self.engine_core = EngineCoreClient.make_client(...)  # 创建和 EngineCore 通信的 client
                        if asyncio_mode and not multiprocess_mode:
                            raise NotImplementedError

                        if multiprocess_mode and asyncio_mode:
                            return make_async_mp_client(...)
                                return AsyncMPClient(...)  # 多进程 + 异步，在线服务常见
                                    launch_core_engines(...)  # 启动后台 EngineCore 进程
                                        EngineCoreProc(...)
                                            EngineCore.__init__(...)
                                            run_busy_loop()

                        if multiprocess_mode and not asyncio_mode:
                            return SyncMPClient(...)  # 多进程 + 同步
                                launch_core_engines(...)
                                    EngineCoreProc(...)
                                        EngineCore.__init__()
                                        run_busy_loop()

                        return InprocClient(...)  # 单进程 + 同步，适合本地源码学习
                            InprocClient.__init__(...)
                                self.engine_core = EngineCore(...)
                                    EngineCore.__init__(...)
                                        self.model_executor = executor_class(vllm_config)  # 创建 Executor

                                            # 如果 executor_class == UniProcExecutor
                                            UniProcExecutor(vllm_config)
                                                Executor.__init__(...)
                                                    self._init_executor()
                                                        # 动态分派到 UniProcExecutor._init_executor()
                                                        UniProcExecutor._init_executor()
                                                            self.driver_worker = WorkerWrapperBase(rpc_rank=0)
                                                            distributed_init_method, rank, local_rank = self._distributed_args()
                                                            kwargs = {...}

                                                            self.driver_worker.init_worker(all_kwargs=[kwargs])  # 创建真正 Worker
                                                            self.driver_worker.init_device()  # 初始化 GPU / CUDA
                                                            self.driver_worker.load_model()  # 加载模型权重

                                        kv_cache_config = self._initialize_kv_caches(vllm_config)  # 初始化 KV cache
                                        Scheduler = vllm_config.scheduler_config.get_scheduler_cls()
                                        self.scheduler = Scheduler(...)  # 创建调度器

```
[' self.driver_worker.load_model() ' 源码位置：./vllm/vllm/v1/executor/uniproc_executor.py#L68 ](./vllm/vllm/v1/executor/uniproc_executor.py#L68)

```python
self.driver_worker.load_model()  # 加载模型权重
    WorkerWrapperBase.load_model()
        self.worker.load_model()
            GPUWorker.load_model()
                self.model_runner.load_model()
                    GPUModelRunner.load_model()
                        model_loader = get_model_loader(self.vllm_config.load_config)

                        self.model = model_loader.load_model(...)
                            # 这里把真正的 PyTorch 模型挂到 GPUModelRunner.self.model 上

                            model_class, _ = get_model_architecture(model_config)
                            model = model_class(vllm_config=vllm_config, prefix=prefix)
                            # 对 facebook/opt-125m：
                            # model_class 通常是 OPTForCausalLM
                            # model = OPTForCausalLM(...)

                            return model


```

**模型加载流程**（以 Qwen2 为例）：

```text
1. 读取模型目录/config.json
   → architectures = ["Qwen2ForCausalLM"]

2. get_model_architecture(model_config)
   → 读取 architectures 字段

3. ModelRegistry 查表
   → "Qwen2ForCausalLM" 映射到 ("qwen2", "Qwen2ForCausalLM")
   → 注册表位置：vllm/model_executor/models/registry.py

4. 动态 import
   → import vllm.model_executor.models.qwen2

5. 取出类
   → Qwen2ForCausalLM

6. 创建模型
   → model = Qwen2ForCausalLM(vllm_config=vllm_config, prefix=prefix)

7. 保存到 runner
   → GPUModelRunner.self.model = model
```

> 一句话：`config.json` 的 `architectures` → ModelRegistry 查表 → 动态 import 对应模块 → 实例化模型类 → 挂到 ModelRunner 上。

### 第一阶段：请求入口与前后端注册

**调用链总览**（从 `LLM.generate()` 到进入第二阶段循环）：

```python
# 第 1 阶段：LLM.generate() —— 离线请求入口
LLM.generate(prompts, sampling_params)
    └─ self._run_completion()          # 添加请求 + 跑完请求 + 返回输出
        ├─ self._add_completion_requests(...)
        │   └─ self._render_and_add_requests(...)   # prompt 渲染/分词 → 内部请求格式
        │       └─ self._add_request(...)
        │           └─ self.llm_engine.add_request(...)
        │               ├─ request = self.input_processor.process_inputs(...)   # 输入预处理
        │               ├─ self.output_processor.add_request(...)               # 前端记录输出状态
        │               └─ self.engine_core.add_request(request)                # 后端加入调度队列
        └─ self._run_engine()          # 驱动引擎直到请求完成
            └─ while self.llm_engine.has_unfinished_requests():
                  step_outputs = self.llm_engine.step()   # → 进入第二阶段，开始循环推理
```

---

#### 为什么 vLLM 也叫「前后端」

它把一次推理拆成两类工作，分别交给不同模块：

| | 前端（CPU / I/O 密集） | 后端（GPU 密集） |
| --- | --- | --- |
| **职责** | 接收请求、检查参数、tokenizer 分词、记录 request 状态、token id 解码成文本、处理 streaming 输出 | 调度本轮执行的请求、分配 KV cache block、组织 batch、跑模型 forward、采样 token、更新 KV cache |
| **所在模块** | `LLMEngine` / `AsyncLLM` / `OutputProcessor` | `EngineCore` / `Executor` / `Worker` |

> 这里的「前端 / 后端」不是网站 UI，而是推理系统内部的职责划分。

#### 「双写注册」是什么意思

`add_request` 里会把同一个 request 同时交给前端和后端各登记一次：

```python
def add_request(self, request_id, prompt, params, ...):
    # 1. 输入预处理：prompt(字符串/token) → EngineCoreRequest
    request = self.input_processor.process_inputs(...)

    # 2. 双写注册
    self.output_processor.add_request(request)  # 前端：状态跟踪（用于取回输出）
    self.engine_core.add_request(request)       # 后端：送入调度队列（用于实际计算）
```

#### 前后端架构示意

```text
LLMEngine (前端进程)              EngineCore (后端进程)
├── InputProcessor                ├── Scheduler
├── OutputProcessor               ├── Executor
└── EngineCoreClient ──IPC──→     └── (GPU 计算)
   (ZMQ / 进程内)
```




### 第二阶段

```Python
# 第 2 阶段：LLMEngine.step() —— 前端取结果 / 处理输出

LLMEngine.step()
    if self.should_execute_dummy_batch:
        self.engine_core.execute_dummy_batch()
        return []

    outputs = self.engine_core.get_output()  # 从 EngineCore 取一轮输出，并进入下一轮

    processed_outputs = self.output_processor.process_outputs(
        outputs.outputs,
        engine_core_timestamp=outputs.timestamp,
        iteration_stats=iteration_stats,
    )  # token id → 文本 / RequestOutput

    self.output_processor.update_scheduler_stats(outputs.scheduler_stats)

    self.engine_core.abort_requests(processed_outputs.reqs_to_abort)
        # 如果 OutputProcessor 发现 stop string，需要通知后端停止对应请求

    self.logger_manager.record(...)  # 记录统计信息

    return processed_outputs.request_outputs


```

### 第三阶段

```python


outputs = self.engine_core.get_output()
    def get_output(self) -> EngineCoreOutputs:
        outputs, model_executed = self.engine_core.step_fn()
            self.step  or self.step_with_batch_queue #进入第四阶段

        self.engine_core.post_step(model_executed=model_executed)
        return outputs and outputs.get(0) or EngineCoreOutputs()



```

### 第四阶段

```python
  def step(self):
    scheduler_output = self.model_executor.execute_model(scheduler_output, non_block=True)
    def execute_model(self):
        output = self.collective_rpc(  # type: ignore[call-overload]
            "execute_model", args=(scheduler_output,), non_block=non_block
        )
            def collective_rpc(  # type: ignore[override]
                run_method(
                        self.driver_worker,
                        "execute_model",
                        args=(scheduler_output,),
                        kwargs=None,
                    )    # 等价self.driver_worker.execute_model
                        self.driver_worker.execute_model(scheduler_output)
    WorkerWrapperBase.execute_model(...)
        self.worker.execute_model(...)
            GPUWorker.execute_model(...)
                GPUModelRunner.execute_model(...)
                    self.model(...) #进入model阶段
       #去到UniProcExecutor.collective_rpc(...)
```

self.model在哪


### 第五阶段


## 几个主流模型架构


[opt模型源码](./vllm/vllm/model_executor/models/opt.py#L10)

[qwen2源码](./vllm/vllm/model_executor/models/qwen2.py#L10)



## 学习路径

建议分成 7 个阶段，每阶段配合「实验 + 读代码」推进。

### 阶段 0：环境跑通

**目标**：在 3080 上启动一个最小 vLLM 服务。

环境检查：

```bash
nvidia-smi
python --version
pip install vllm
```

启动小模型：

```bash
vllm serve Qwen/Qwen2.5-0.5B-Instruct \
  --max-model-len 2048 \
  --gpu-memory-utilization 0.85 \
  --port 8000
```

测试请求：

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen2.5-0.5B-Instruct",
    "messages": [{"role": "user", "content": "你好，简单介绍一下 vLLM"}],
    "max_tokens": 64
  }'
```

### 阶段 1：理解推理基本流程

先不碰 vLLM，先搞懂大模型推理本身：

```
prompt tokenization → embedding → transformer layers → prefill → KV cache → decode → sampling
```

重点问题：

- 为什么 prefill 影响 TTFT（首 token 延迟）？
- 为什么 decode 是一个 token 一个 token 生成？
- KV cache 为什么能避免重复算历史 token？

> 产出：画一张「极简 Transformer 推理流程图」。

### 阶段 2：用 vLLM 跑实验

**目标**：亲眼看到参数怎么影响性能。

| 实验 | 变量 | 固定项 | 观察指标 |
| --- | --- | --- | --- |
| 实验 1：输入越长，TTFT 越高 | 输入 `128 / 512 / 1024 / 2048` tokens | `max_tokens = 1` | 主要测 prefill |
| 实验 2：输出越长，decode 时间越长 | `max_tokens = 16 / 64 / 256` | 固定 prompt | decode 阶段耗时 |
| 实验 3：并发请求 | 并发数 | —— | throughput 变化（用 `vllm bench` 或 Python 并发脚本） |

### 阶段 3：读入口代码

看请求怎么进入 vLLM。重点文件：

- `vllm/entrypoints/llm.py`
- `vllm/entrypoints/openai/api_server.py`
- `vllm/engine/llm_engine.py`

建立这条「请求生命周期」主线：

```
用户请求 → API Server / LLM.generate → LLMEngine.add_request → LLMEngine.step → executor 执行模型 → 返回 token
```

> 这一阶段不用追每个细节，只要建立整体认知。

### 阶段 4：读 scheduler

重点文件：`vllm/core/scheduler.py`

看懂三个队列 / 状态：

- `WAITING`：等待 prefill 的请求
- `RUNNING`：正在 decode 的请求
- `FINISHED`：已完成（正常结束 / 被中止 / 超过长度）

以及：

- prefill 请求怎么进来
- decode 请求怎么继续
- 请求在三个状态间怎么流转
