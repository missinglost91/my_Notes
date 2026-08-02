---
tags:
  - "#计算机"
  - "#编程"
  - "#人工智能"
abstract: 以uv为基础的python环境配置教程，适用于本地电脑，以及autodl、colab、kaggle等平台的环境配置
author:
  - 关山难
---
# ==前言==：为何使用uv
对于初学者来说conda或许是一个不错的选择。

> anaconda，就是他自带的非常多，非常多包，是有很多是没有必要的，而且很冗余，而且到后面和你的配置会相冲突

> miniconda ,另外一个是这个，但他带的包很少，其实跟你用Python直接venv创一个虚拟环境是差不多的
> 
> 但是目前来说，uv是一个更好更现代化的管理方式的选择，简便快捷，也比较好理解。我个人用的是uv来管理我的python环境


# ==第一章== ：电脑上 uv 环境配置

## 下载uv

首先要下载python，下载vscode或者pycharm你喜欢的一款ide，这个不赘述

接着下载uv

可以参考官方文档下载
https://uv.doczh.com/guides/projects/#pyprojecttoml

或者直接
```bash
pip install uv
```
常用指令速查表

|命令|描述|
|--|---|
uv init <项目名>	|创建新项目
uv venv	|创建虚拟环境
uv add <包名>	|添加依赖
uv remove <包名>	|移除依赖
uv run <脚本>	|运行脚本
uv lock	|生成锁文件
uv sync|	同步环境与依赖
uv python install <版本>	|安装Python版本
uv tool install <工具>|	安装Python工具
uvx <工具> [参数]|	运行Python工具




## 更改缓存路径缓存

window下默认缓存的默认路径可以用这个来查看

```bash
uv cache dir 
```

一般都是在系统盘，我们想把他搬到别的盘，比如D盘

步骤如下

1. 一键清除原来的缓存
```bash
uv cache clean 
```
2. 在其他盘新建文件夹，比如` D:\uv-cache`

3. 以管理员身份打开命令提示符 / 终端执行：
```bash
setx UV_CACHE_DIR "D:\uv-cache" /M
```
4. 重启终端 / 电脑生效

![20260210202902](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210202902.png)

>为啥要改缓存路径
> 其一，因为系统盘一般比较小，而我们的uv缓存一般都有10几个G了太占地方
> 其二，以便于同盘硬连接，可以不用重下包，省空间
>

## 关于uv与pytorch的结合

假设我们项目用的是`pytorch==2.8`版本，用`cp312`的python版本

因为我的的电脑是win32的`interGPU`版本

考虑租服务器一般是linux-x86系统的`cuda128`

还要考虑别人的电脑是win32的`cuda128`版本


**我们直接来pytorch官网找相关适配项，也可选择其他镜像源
网址 https://download.pytorch.org/whl/torch/**

你觉得官网慢的话可以考虑阿里云镜像

![20260210181608](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210181608.png)

>直接将 PyTorch 安装指引 中的 https://download.pytorch.org/whl 替换为 https://mirrors.aliyun.com/pytorch-wheels即可。

1. 合适我电脑的torch+xpu版本
    ![20260209215455](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260209215455.png)

2. 适合服务器的torch+cuda版本

    ![20260209215324](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260209215324.png)

3. 适合win的cuda版本

    ![20260209220338](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260209220338.png)

4. 因为我的的电脑是win32的`interGPU`版本，我还需要`intel-extension-for-pytorch`这个依赖（其实inter宣布2.5以后的torch+xpu版本就原生支持xpu了，**不需要**这个了）
   
    网址 https://pytorch-extension.intel.com/release-whl/stable/xpu/cn/intel-extension-for-pytorch/


5. 因为我的的电脑是win32的`interGPU`版本，我还需要`pytorch-triton-xpu`这个依赖(也**不需要**这个了,torch+xpu里面已经有这个插件了)
    网址 https://download.pytorch.org/whl/pytorch-triton-xpu


## 配置环境

我们可以自己手搓一个`pyproject.toml`文件，也可以直接使用我提供的`pyvenv.zip`



### 情况一:鼓励自己手搓

先执行这个来创建一个项目

```bash
uv init myvenv
```

#### 更改其中的toml文件

详细语法可以见官方文档 https://uv.doczh.com/guides/projects/#pyprojecttoml

我写的如下
```toml
# 请从readme.md文件中挑选合适的toech版本下载
# 如果您不喜欢官方源下载torch，可以将链接 https://download.pytorch.org/whl 替换为 https://mirrors.aliyun.com/pytorch-wheelssh来使用阿里源即可

[project]
name = "pytorch-venv"
version = "0.1.0"
description = "该项目为Pytorch的通用环境"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [

    # Windows interGPU
     "torch @ https://mirrors.aliyun.com/pytorch-wheels/xpu/torch-2.8.0%2Bxpu-cp312-cp312-win_amd64.whl#sha256=0937d8943c145a83d9bafc6f80ef28971167817f9eda26066d33f72caf8a6646 ",

    "torchvision>=0.22.0 ",
    "matplotlib==3.10.5",
    "numpy==2.3.2",
    "tqdm>=4.66.2",
    "tensorboard>=2.20.0",
    "pandas==2.3.3",
    "opencv-python>=4.13.0.92",
    "scipy>=1.17.0",
    "scikit-image>=0.26.0",
    "thop>=0.1.1.post2209072238",
    "scikit-learn>=1.8.0",
    "ipykernel>=7.2.0",
]

[tool.uv]
index-url = "https://mirrors.aliyun.com/pypi/simple/"
extra-index-url = ["https://pypi.org/simple/", "https://pypi.tuna.tsinghua.edu.cn/simple/", "https://download.pytorch.org/whl/"]
```

#### 写一个readme.md文件
```
# 项目介绍

项目是一个用uv构建的基于python3.12版本和torch2.8.0的环境

你可以根据你的平台选择不同的torch版本(cu128,xpu,cpu), 并安装对应的依赖

同时包含了一些pytorch训练的常用依赖，详情请见 pyproject.toml文件

————————
确保你的电脑上已安装3.12版本的Python, 并安装了uv

请打开pyproject.toml文件,请根据自身配置，选取下方合适的版本替换掉`pyproject.toml`中的`"torch",`部分

 Windows cuda
"torch @ https://download.pytorch.org/whl/cu128/torch-2.8.0%2Bcu128-cp312-cp312-win_amd64.whl#sha256=0ad925202387f4e7314302a1b4f8860fa824357f9b1466d7992bf276370ebcff ",
 Windows interGPU
"torch @ https://download.pytorch.org/whl/xpu/torch-2.8.0%2Bxpu-cp312-cp312-win_amd64.whl#sha256=0937d8943c145a83d9bafc6f80ef28971167817f9eda26066d33f72caf8a6646 ",
 Linux CUDA
"torch @ https://mirrors.aliyun.com/pytorch-wheels/cu128/torch-2.8.0%2Bcu128-cp312-cp312-manylinux_2_28_x86_64.whl#sha256=4354fc05bb79b208d6995a04ca1ceef6a9547b1c4334435574353d381c55087c ",

命令行中进入该文件, 并执行以下命令

uv sync

如有不理解请参阅我的github上
`my_Notes/【其他】大合集/【经验之谈】-我的一些闲言碎语 (同步CSDN)
/python环境配置.md`
https://github.com/missinglost91/my_Notes/blob/main/


只需在其他项目时激活该环境即可

```
#### 写一个测试模块

我们写一个检测设备的模块`checkdevice.py`

```python
import torch
import platform


def check_device():
    # --- 2. 环境和设备设置 ---
    # 定义设备, 优先顺序: CUDA -> XPU -> CPU
    if torch.cuda.is_available():
        device = torch.device("cuda")
        # 关键优化：为CUDNN后端启用基准测试模式，可以加速固定尺寸输入的卷积网络
        torch.backends.cudnn.benchmark = True
        count = torch.cuda.device_count()
        print("CUDA 已启用, CuDNN benchmark 已开启。")
        print(f"CUDA 设备数量：{count}")
        for i in range(count):
            try:
                name = torch.cuda.get_device_name(i)
            except Exception:
                name = f"cuda:{i}"
            print(f"  - [{i}] {name}")

    elif hasattr(torch, 'xpu') and torch.xpu.is_available():
        count = torch.xpu.device_count()
        print(f"✅ Intel GPU 可用！设备数量：{count}")
        for i in range(count):
            try:
                name = torch.xpu.get_device_name(i)
            except Exception:
                name = f"xpu:{i}"
            print(f"  - [{i}] {name}")
        device = torch.device("xpu")
        
    else:
        device = torch.device("cpu")
        try:
            cpu_name = platform.processor() or platform.machine()
            if not cpu_name:
                cpu_name = "Unknown CPU"
        except Exception:
            cpu_name = "Unknown CPU"
        print(f"CPU: {cpu_name}")

    print("********************************************")
    print(f"-------------将使用设备: {device}----------------")
    print("********************************************")

    return device

```


在主程序`main.py`中引用

```python
import checkdevice

device = checkdevice.check_device()

```

### 情况二:使用我提供的pyvenv.zip

直接解压即可

按我们readme来调整toml文件


## 运行

```bash
uv sync
```

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260214153052556.png?imageSlim)

它显示用你电脑上的python来创建虚拟环境


![20260210223828](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210223828.png)
下载完毕

运行我们刚才写的脚本
```bash
uv run main.py
```


![20260210220306](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210220306.png)


成功了！



## 使用jupyter notebook

需要已经下好`ipkernel`包



![20260210222333](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210222333.png)

选择我们刚刚创建的虚拟环境

![20260210222312](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210222312.png)

成功

![20260210222444](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210222444.png)


## 共享解释器
（如果改了缓存路径就可以跳过这步）

因为我们现在只是都只是做一些小的demo，用到的依赖都差不多，所以我们可以用同一个解释器（我这里用demo312的），省空间
我们后续如果想管理依赖的话也只需要管理demo312中的就行



别的项目也可以用demo312的解释器


我们可以在ide中挑选我们解释器

![20260210142715](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210142715.png)

![20260209233226](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260209233226.png)

当然，后面做一些大的demo的话就需要有新的解释器

如果没有ide，就需要命令行先激活该环境，在切换到另一个项目的文件夹再执行程序


```bash
cd 环境文件夹
source .venv/bin/activate
cd 指定demo
uv run mian.py-
```


## 安装第三方库

我们要抛开以前无脑pip的思维，养成先找适配版本再安装的好习惯

![![20260210150534](httpslin01-image-1373317342.cos.ap-beijing.myqcloud.com20260210150534.png)](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/![20260210150534](httpslin01-image-1373317342.cos.ap-beijing.myqcloud.com20260210150534.png).png)


![20260210151126](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210151126.png)

这个就很可以直接来下载最新版

```bash
uv add tqdm
```

我们再来装一些其他的常用计算机视觉第三方库

这时候就要考虑版本冲突的问题了

而我们的`uv tree`这时候就发力了

这个是网络上推荐的稳定版本的组合

![20260210150026](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210150026.png)

![20260210150059](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210150059.png)

而我们的`uv tree`这时候就可以查看目前的依赖版本


如果依赖版本冲突的话会报错，而且光看下面冲突很难找到原因

![20260210150217](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210150217.png)


## 硬连接的理解

我们现在D盘的大小如下

![20260210235459](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210235459.png)

假如我们重复刚刚的过程
![20260210235635](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210235635.png)

你会发现几秒内就下载好了

![20260210225639](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210225639.png)

再看D盘

![20260210235655](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210235655.png)

且理论上是要多好几个G，但是D盘大小却没有变化

说明实际上是硬链接到缓存中的文件


# 在autodl上配置uv环境

租用服务器，无卡模式开机

![20260210003309](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210003309.png)

## 下载uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

退出重进
![20260210003440](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210003440.png)
成功下载
![20260210003504](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210003504.png)
检查python版本

```bash
uv python list
```
![20260210003548](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210003548.png)

## 更改缓存路径

1. 先在数据盘建一个专门的 uv 缓存文件夹，执行：
   
```bash
mkdir -p /root/autodl-tmp/uv-cache
```

2. 设置永久环境变量（核心）

    AutoDL 默认用 bash 终端，我们把 uv 缓存路径写入 ~/.bashrc（每次登录终端都会自动加载），执行：
```bash
运行
echo 'export UV_CACHE_DIR="/root/autodl-tmp/uv-cache"' >> ~/.bashrc
```
>这句命令的作用：把 UV_CACHE_DIR 环境变量（指定 uv 缓存路径）追加到 ~/.bashrc 文件末尾，实现永久生效。
注意：AutoDL 中你是 root 用户，~ 等价于 /root，不用额外加权限。
3. 让环境变量立即生效
执行下面的命令，让刚写入的配置立刻生效（不用重启终端）：
```bash
运行
source ~/.bashrc
```
4. 验证是否设置成功（关键）
执行下面的命令，查看 uv 当前的缓存目录：
```bash
uv cache dir
```
![20260210203700](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210203700.png)
成功



## 配置通用
环境把我们上传的`pyvenv.zip`解压

```bash
unzip pyvenv.zip
```
按照`readme.md`中的要求调整`pyproject.toml`文件中的内容

```bash
cd pyvenv
```
初始化环境

```bash
uv sync
```
运行测试文本
```bash
uv run main.py
```


有卡开机试试

再运行测试文本
```bash
uv run main.py
```
成功
![20260210222050](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210222050.png)



.venv会被linux隐藏，看不见是正常的

**把该环境注册成Jupter内核**

先激活环境uv
source .venv/bin/activate

删除环境
rm -rf .venv
下载一个专属于你环境的ipykernel
uv add ipykernel

注册
python -m ipykernel install --user --name=uv_env --display-name="pyvenv"

![20260210013915](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210013915.png)




## 在autodl上运行别人的项目

![20260210164517](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260210164517.png)


cd 目标文件夹

解压
unzip demo_wly.zip

先创建并继承虚拟环境
uv venv --system-site-packages

参照pyproject.toml内容并修改

任何的修改都要cirl+s保存

uv sync


autodl中的conda与uv混合使用
https://zhuanlan.zhihu.com/p/1898715062929175170

conda create -n myvenv python=3.12

conda init 

conda activate myvenv

conda env list

conda remove -n 环境名 --all


 Conda（不推荐）

AutoDL 是一个基于云的 AI 计算平台，提供了强大的 GPU 计算资源，用户可以在上面训练和部署 AI 模型。

autodl的服务器已经帮我们装好了conda了

我们可以用他给的conda环境创建一个我们自己的conda的虚拟环境


**配置与激活**
```bash
conda create -n myenv python=3.9 # 创建一个名为 myenv 的环境，Python 版本为 3.9

conda activate jupyter_venv  #激活虚拟环境 

#一般第一次激活它会让你conda init一下，再退出重进

```

**分享/备份一个虚拟环境**
一个分享环境的快速方法就是给他一个你的环境的.yml文件。

首先激活要分享的环境，在当前工作目录下生成一个environment.yml文件。

```bash
conda env export > environment.yml
```
对方拿到environment.yml文件后，将该文件放在工作目录下，可以通过以下命令从该文件创建环境即可。

```bash
conda env create -f environment.yml
```
**包管理**

安装包
```bash
conda install [package] (如：conda install numpy)
```bash

指定包版本：
```bash
conda install xlrd=1.2.0 (注意是单等于号）
```
也可以使用pip install安装：

```bash
pip install xlrd==1.2.0 (注意是双等于号）
```

## 批量安装 requirements.txt 文件中包含的组件依赖
conda install --yes --file requirements.txt

批量导出依赖包
批量导出包含环境中所有依赖包到requirements.txt文件。


```
conda list -e > requirements.txt
```


# Kaggle

https://www.kaggle.com/

![20260211151640](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260211151640.png)

最好手机打开再身份验证


![20260214152149](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260214152149.png)

这样就连上网络了










