# Transformer 补充笔记

## 目录

- [Transformer 补充笔记](#transformer-补充笔记)
  - [目录](#目录)
  - [一、张量基础](#一张量基础)
    - [1.1 创建张量](#11-创建张量)
    - [1.2 重新认识维度](#12-重新认识维度)
    - [1.3 高维张量与 `...` 语法](#13-高维张量与--语法)
    - [1.4 切片实战](#14-切片实战)
  - [二、激活函数](#二激活函数)
    - [2.1 ReLU](#21-relu)
    - [2.2 Sigmoid](#22-sigmoid)
    - [2.3 SiLU（Swish）](#23-siluswish)
    - [2.4 ReLU vs SiLU 对比](#24-relu-vs-silu-对比)
  - [三、前馈神经网络（FFN）](#三前馈神经网络ffn)
    - [3.1 传统 FFN](#31-传统-ffn)
    - [3.2 门控 FFN（Gated FFN / SwiGLU）](#32-门控-ffngated-ffn--swiglu)
    - [3.3 传统 FFN vs 门控 FFN](#33-传统-ffn-vs-门控-ffn)
  - [四、三维张量 `(batch, seq, hidden)`](#四三维张量-batch-seq-hidden)
  - [五、Self-Attention（自注意力机制）](#五self-attention自注意力机制)
    - [5.3 多头注意力（Multi-Head Attention）](#53-多头注意力multi-head-attention)
    - [5.4 每个头的维度](#54-每个头的维度)
    - [5.5 分组查询注意力（GQA）：为什么 K/V 不需要那么多头？](#55-分组查询注意力gqa为什么-kv-不需要那么多头)
    - [5.6 旋转位置编码（RoPE）](#56-旋转位置编码rope)
      - [5.6.1 核心直觉：把向量看作平面上的点](#561-核心直觉把向量看作平面上的点)
      - [5.6.2 数学原理：旋转矩阵](#562-数学原理旋转矩阵)
- [\\begin{bmatrix} x' \\ y' \\end{bmatrix}](#beginbmatrix-x--y-endbmatrix)
      - [5.6.3 如何应用到 128 维向量？](#563-如何应用到-128-维向量)
      - [5.6.4 代码实现](#564-代码实现)
    - [5.7 Attention 的完整流程](#57-attention-的完整流程)

---

## 一、张量基础

### 1.1 创建张量

```python
x = torch.randn(2, 3)
# 相当于下面这个张量的 shape
x = torch.tensor(
    [[1, 1, 1],
     [2, 2, 2]])
# 这里的 2 和 3 并非严格意义上的"几行几列"
# 而是表示：第一个维度有 2 个元素，第二个维度有 3 个元素
```

### 1.2 重新认识维度

```python
x = torch.tensor(1)
x.dim()  # 0

x = torch.tensor([1, 2, 3, 4, 5, 6])  # 1 维

x[:4]  # 切片 [0:4]，取前 4 个元素 → tensor([1, 2, 3, 4])

x[:1]  # 取第 0 个元素，等价于 x[0:1]，注意左闭右开
x[0]   # 也是取第 0 个元素
# 区别：x[0:1] 是 1 维张量，x[0] 发生降维，变成 0 维张量
```

![20260731222748](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260731222748.png)

### 1.3 高维张量与 `...` 语法

创建一个高维张量：

```python
x = torch.tensor([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
])  # 2 维

# 取第一行：第一个维度的第 0 个元素，第二个维度的全部元素
x[0:1, :]  # 取第 0 行（不降维）
x[0, :]    # 取第 0 行（降维）
```

![20260731223614](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260731223614.png)

> 平时更推荐写成 `x[0:1, :]`，避免降维。

5 维张量：

```python
x = torch.randn(2, 3, 4, 5, 6)
# 第 1 维：2 个元素
# 第 2 维：3 个元素
# 第 3 维：4 个元素
# 第 4 维：5 个元素
# 第 5 维：6 个元素
```

取第一个维度的第一个元素，其他全保留：

```python
x[:1, :, :, :, :]  # 完整写法
x[:1, ...]         # 简便写法：... 自动展开剩余维度
```

### 1.4 切片实战

```python
x = torch.tensor(
    [[1, 2, 3, 4, 5, 6, 7, 8],
     [9, 10, 11, 12, 13, 14, 15, 16]])

# 从中间切开：y 为前一半，z 为后一半
y = x[..., :4]  # 保留第 1 维全部，第 2 维取前一半
z = x[..., 4:]  # 保留第 1 维全部，第 2 维取后一半
```

![20260731224827](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260731224827.png)

---

## 二、激活函数

### 2.1 ReLU

$$
ReLU(x) = \begin{cases} 0, & x \leq 0 \\ x, & x > 0 \end{cases}
$$

### 2.2 Sigmoid

$$
sigmoid(x) = \frac{1}{1 + e^{-x}}
$$

### 2.3 SiLU（Swish）

$$
SiLU(x) = \frac{x}{1 + e^{-x}} = x \cdot \sigma(x)
$$

![20260801183400](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260801183400.png)

> SiLU 在负数区域有轻微翘起（约 -0.1~0），这反而是好事，更符合神经网络的非线性特征。

![20260801192224](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260801192224.png)

### 2.4 ReLU vs SiLU 对比

| 特性     | ReLU            | SiLU                    |
| -------- | --------------- | ----------------------- |
| 公式     | `max(0, x)`     | `x · σ(x)`              |
| 负数输出 | 0               | 非零（约 -0.1~0）       |
| 平滑度   | 在 0 处不可导   | 全程平滑                |
| 计算成本 | 低              | 中等（含指数）          |
| 现代应用 | 基础网络        | LLaMA/Mistral 的 SwiGLU |

---

## 三、前馈神经网络（FFN）

> **FFN = Feed-Forward Network（前馈神经网络）**
>
> 在 Transformer 中，FFN 是注意力机制后面的关键组件。
>
> **作用**：对每个位置的 token 独立进行非线性变换，增强模型表达能力。

### 3.1 传统 FFN

```text
输入 x
  → 线性层(升维)
  → 激活函数
  → 线性层(降维)
  → 输出
```

```python
x = linear1(x)
x = torch.relu(x)   # 负数全部变 0
x = linear2(x)
```

$$
FFN(x) = ReLU(xW_1 + b_1)W_2 + b_2
$$

### 3.2 门控 FFN（Gated FFN / SwiGLU）

**门控是啥？** 引入一个"门"分支，控制信息通过量：

```python
gate = gate_proj(x)   # 产生门信号
up   = up_proj(x)     # 产生信息
x    = silu(gate) * up  # 用门控制信息通过量
x    = down_proj(x)   # 合并输出
```

$$
FFN(x) = SiLU(xW_g + b_g) \otimes (xW_v + b_v) W_2 + b_2
$$

### 3.3 传统 FFN vs 门控 FFN

| 维度       | 标准 FFN                                              | 门控 FFN (Gated FFN)                                          |
| ---------- | ----------------------------------------------------- | ------------------------------------------------------------- |
| 公式       | $ReLU(xW_1 + b_1)W_2 + b_2$                           | $SiLU(xW_g + b_g) \otimes (xW_v + b_v)W_2 + b_2$              |
| 线性层数量 | 2 个（up → activation → down）                        | 3 个（gate + value + down）                                   |
| 门控机制   | 无                                                    | 引入 gate 分支，与 value 逐元素相乘（⊗）                      |
| 激活函数   | ReLU / GELU                                           | SiLU（Swish）                                                 |
| 参数量     | 2 × hidden × ffn_dim                                  | 3 × hidden × ffn_dim（多约 50%）                              |
| 代表模型   | 原始 Transformer                                      | LLaMA、Qwen、Mistral 等主流 LLM                               |

---


在真实代码中，我们的门控FFN并不会这样写

而是这样


```python
# 理论版本
self.gate_proj = nn.Linear(hidden_size, intermediate_size)
self.up_proj   = nn.Linear(hidden_size, intermediate_size)

# 真实代码（qwen2.py 第 90 行）
self.gate_up_proj = MergedColumnParallelLinear(
    hidden_size,
    [intermediate_size] * 2,  # 输出是 2 * intermediate_size
    bias=False,
)
```
SiluAndMul 的内部实现
```python
你之前看到的是：

python
x = self.act(gate) * up   # 两步：先激活，再乘法
真实代码用的是：

python
self.act_fn = SiluAndMul()
x = self.act_fn(gate_up)  # 一步：内部自动拆分 + 计算
```
## 四、三维张量 `(batch, seq, hidden)`

Transformer 里最常见的三维张量：`(batch, seq, hidden)`

**示例**：3 句话（batch=3），每句话 4 个 token（seq=4），每个 token 用 4 维向量表示（hidden=4）

```python
x = torch.tensor([
    # ===== 第 1 句话：今天天气 =====
    [
        [1.0,  0.5, -2.0,  0.8],   # "今"
        [0.3, -1.0,  1.5, -0.5],   # "天"
        [2.0,  0.1, -0.5,  1.2],   # "天"
        [-0.5, 1.5,  0.8, -1.0],   # "气"
    ],
    # ===== 第 2 句话：我喜欢吃 =====
    [
        [0.8, -0.3,  1.2,  0.5],   # "我"
        [1.5,  0.2, -0.8,  0.1],   # "喜"
        [-0.2, 0.9,  0.5, -1.5],   # "欢"
        [0.6, -0.5,  1.0,  0.3],   # "吃"
    ],
    # ===== 第 3 句话：明天要考 =====
    [
        [1.2, -0.8,  0.5,  0.9],   # "明"
        [0.4,  1.5, -0.3, -0.2],   # "天"
        [-1.0, 0.8,  0.2,  1.5],   # "要"
        [0.7, -0.1,  1.8,  0.6],   # "考"
    ],
])
# x.shape: (3, 4, 4)
#          │  │  └─ hidden_size=4（每个 token 的向量维度）
#          │  └──── seq=4（每句话 4 个 token）
#          └─────── batch=3（3 句话）
```


---

## 五、Self-Attention（自注意力机制）

> 论文：《Attention Is All You Need》

**核心公式**：

$$
Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

| 符号        | 含义                                   |
| ----------- | -------------------------------------- |
| $Q$         | Query（查询矩阵）                      |
| $K$         | Key（键矩阵）                          |
| $V$         | Value（值矩阵）                        |
| $d_k$       | 键向量的维度                           |
| $\sqrt{d_k}$ | 缩放因子，防止点积过大导致梯度消失     |
| $softmax$   | 归一化，使注意力权重和为 1             |


在 Qwen2 中：`hidden_states` 本质上就是经过编码后的词向量（经过多层网络传递后的结果）。

#### 5.1.1 核心类比：图书馆查资料

想象你在图书馆找书：

| 概念       | 角色     | 通俗解释                       |
| ---------- | -------- | ------------------------------ |
| Q (Query)  | 你的需求 | "我想找深度学习的入门书"       |
| K (Key)    | 书的标签 | 书架上每本书的分类标签         |
| V (Value)  | 书的内容 | 真正要读的正文内容             |

**工作流程**：

1. 你拿着需求 (Q) → 去匹配书架标签 (K)
2. 计算匹配度 → 决定每本书的"注意力权重"
3. 按权重提取内容 (V) → 加权组合出最终信息

**公式对应关系**：

```text
注意力输出 = softmax(Q × Kᵀ / √d) × V
              ↑         ↑           ↑
           最终结果   匹配分数    实际内容
```

### 5.3 多头注意力（Multi-Head Attention）

**什么是"多头"？** 原始的 Attention 只有一个"头"（Single-head）。Multi-head 就是同时运行多个独立的 Attention，每个头关注不同的信息。

**生活类比**：想象一个班级有 32 个学生（Head），同时观察同一句话 "今天苹果真好吃"：

| 学生（Head） | 关注点     | 注意力分配                  |
| ------------ | ---------- | --------------------------- |
| Head 1       | 语法结构   | 关注"好吃"和"苹果"的关系    |
| Head 2       | 语义实体   | 关注"苹果"是一种水果        |
| Head 3       | 情感色彩   | 关注"真好吃"表达了正面情绪  |
| Head 4       | 上下文关联 | 关注"今天"和时间有关        |

> **为什么需要多头？** 单个头只能看到一种模式。32 个头并行工作，能同时捕获语法、语义、情感等多种特征。

### 5.4 每个头的维度

在 Qwen2 中：

```python
hidden_size = 4096   # 模型工作维度
num_heads   = 32     # 注意力头数
head_dim    = 4096 // 32  # = 128，每个头的维度
```

> **直观理解**：把一根长度为 4096 的"长绳子"切成 32 段，每段长度就是 128。

### 5.5 分组查询注意力（GQA）：为什么 K/V 不需要那么多头？

**直觉理解**：想象一个学生（Query）在图书馆（Key/Value）里找资料。

**Q（学生）的视角 —— 32 个头**：
学生需要从 32 个不同角度（语法、实体、时间、逻辑等）同时提问。角度越多，问得越细，找答案越准。
→ 所以 Q 的头数需要多，以便进行细粒度检索。

**K/V（图书馆）的视角 —— 8 个头**：
图书馆里的书（信息）是相对固定的。不需要为这 32 个角度分别建 32 座一模一样的图书馆，只要有几组核心索引（比如 8 组）能覆盖这些知识就足够了。
→ 所以 K/V 的头数可以少，因为它们主要负责提供信息。

> **结论**：一个 K/V 头可以被 4 个 Q 头"共享"。Q 负责"多问"，K/V 负责"多存"。

---

### 5.6 旋转位置编码（RoPE）

#### 5.6.1 核心直觉：把向量看作平面上的点

想象词向量简化成 **2 维**（一个 X，一个 Y），在坐标系中就是一个点。

RoPE 的做法：

- 位置 0 的向量：不旋转（角度 0）
- 位置 1 的向量：逆时针旋转 $\theta$ 度
- 位置 2 的向量：逆时针旋转 $2\theta$ 度
- ...以此类推

> **为什么用旋转而不用加法？** 旋转是一种"保长变换"——向量旋转后长度（模长）不变，能保持模型数值计算的稳定性。

#### 5.6.2 数学原理：旋转矩阵

在二维平面中，把点 $(x, y)$ 旋转 $\theta$ 度，得到新点 $(x', y')$：

$$
\begin{bmatrix} x' \\ y' \end{bmatrix}
=
\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
$$

也就是：

$$
x' = x\cos\theta - y\sin\theta
$$

$$
y' = x\sin\theta + y\cos\theta
$$

**关键点**：当 Attention 计算两个向量的相似度（点积）时，旋转后的点积变成：

$$
(R_m Q) \cdot (R_n K) = Q \cdot K + \text{与 } (m-n)\theta \text{ 相关的项}
$$

> **结论**：计算结果中自然出现了与位置差 $(m-n)$ 有关的项。模型不需要额外学习位置信息，旋转本身就把相对位置"编码"进了相似度计算中。

#### 5.6.3 如何应用到 128 维向量？

实际向量是 128 维的，做法是**两两一组，分别旋转**：

把 128 维向量看作 64 对 2 维向量：

| 维度对             | 旋转角度       |
| ------------------ | -------------- |
| 第 1 对（维度 0, 1）   | $\theta_1$     |
| 第 2 对（维度 2, 3）   | $\theta_2$     |
| ...                | ...            |
| 第 64 对（维度 126, 127） | $\theta_{64}$  |

> **为什么每对角度不同？** 为了捕捉不同尺度的相对位置关系——就像齿轮系统，有快转的小齿轮（高频），也有慢转的大齿轮（低频）。

#### 5.6.4 代码实现

在 Qwen2 中，`rotary_emb` 的具体操作就是把上述公式"向量化"：

```python
# 假设这是 Q 向量的一部分 (batch, seq, head_dim)
x = torch.randn(2, 128, 128)

# 1. 计算旋转角度 (Cosine & Sine)
cos, sin = self.rotary_emb(positions)
# cos/sin shape: (batch, seq, 1, 128)
# 内部是根据 RoPE 公式生成的：cos(m * theta^(-i/d))

# 2. 将向量切片
x1 = x[..., ::2]   # 偶数维度：x
x2 = x[..., 1::2]  # 奇数维度：y

# 3. 应用旋转公式 (x' = x*cos - y*sin)
out = torch.cat([
    x1 * cos - x2 * sin,
    x1 * sin + x2 * cos
], dim=-1)
```

### 5.7 Attention 的完整流程

```text
输入 hidden_states
  ↓
[qkv_proj]   一次投影，得到 Q、K、V 三个张量
  ↓
q, k, v = qkv.split()   把 qkv 拆成三份
  ↓
[可选] qk_norm   对 Q/K 做归一化
  ↓
[rotary_emb]   给 Q/K 加上位置信息（RoPE）
  ↓
[attn]   计算 Attention(Q, K, V)
  ↓
[o_proj]   输出投影
  ↓
输出 attention_output
```

```python
# 输入
hidden_states  # shape: (batch, seq, hidden_size) 比如 (2, 128, 4096)

# qkv_proj 做什么？
qkv = hidden_states @ W_qkv.T + bias
# qkv shape: (batch, seq, 3 个头的总维度)
```

