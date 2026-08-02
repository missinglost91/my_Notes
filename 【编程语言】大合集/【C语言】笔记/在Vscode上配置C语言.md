# 在Vscode上配置C语言
#### 关山难编写
______
## 1预备环境安装
### vscode安装

我图方便全部都使用Vscode编写
### Mingw安装
教程<https://www.bilibili.com/video/BV1z4RcY1EwT/?spm_id_from=333.337.search-card.all.click&vd_source=8e2d51b3fb74130867ec7407fec9d377>
### 插件安装
![2025-06-26-14-32-00](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-14-32-00.png)
![2025-06-26-14-32-16](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-14-32-16.png)


## 2创建项目文件夹
![2025-06-26-16-54-06](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-16-54-06.png)
后缀名为.c的是C语言文件，后缀名为.cpp的是C++语言文件
> :memo: **注意：** 避免中文和空格。

## 3编译器设置
在Vscode中按住`cirl+shift+p`
![2025-06-26-16-57-07](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-16-57-07.png)
找到MinGw安装的路径
![2025-06-26-17-33-27](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-33-27.png)
填入下图
![2025-06-26-16-58-25](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-16-58-25.png)
接着改成如图
![2025-06-26-17-01-57](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-01-57.png)

## 4插入.vscode文件
如果项目为单文件则复制
![2025-06-26-17-05-35](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-05-35.png)
并黏贴到该项目同属文件夹中
![2025-06-26-17-07-32](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-07-32.png)
多文件同理
![2025-06-26-17-10-45](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-10-45.png)

## 5编写内容
在Text1中随便写行代码
```C
#include <stdio.h>
int main()

{
    printf("hehe\n");
    return 0;
}
// 打印出hehe
```

## 6生成exe可执行文件
在该项目页面中点击
![2025-06-26-17-18-26](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-18-26.png)
![2025-06-26-17-20-34](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-20-34.png)
![2025-06-26-17-20-13](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-20-13.png)

## 7用终端运行exe可执行文件
![2025-06-26-17-21-53](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-21-53.png)
按任意键关闭
变成
![2025-06-26-17-22-21](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-22-21.png)
这下面就涉及到了cmd命令行的知识点
cmd知识点大全<https://www.cnblogs.com/xiaodi888/p/18633228>
当然我们只需掌握很少的部分
![2025-06-26-17-27-41](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-27-41.png)
回车运行
![2025-06-26-17-28-15](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-28-15.png)
成功打印出hehe

## 8修改
包麻烦的
若我们想改成he
![2025-06-26-17-30-59](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-30-59.png)
重新
![2025-06-26-17-18-26](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-18-26.png)
再运行exe
![2025-06-26-17-32-35](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-17-32-35.png)
成功

## 9多项目同理
记得改json文件
