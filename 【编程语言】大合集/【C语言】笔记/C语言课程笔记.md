---
tags:
  - "#C语言"
  - "#编程"
abstract: 这里填写这篇笔记的摘要
author:
  - 关山难
---


![2025-07-05-21-55-07](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-21-55-07.png)

## 常识

# 计算机基础知识的补充


计算机由硬件系统和软件系统构成，

硬件系统细分为主机和外设

	主机包括内存储器、中央处理器（cpu），集成了运算器和控制器

	外设则包括了输入设备、输出设备、外存储器（固态硬盘和移动硬盘）


软件系统则细分为应用软件和系统软件

	系统软件包括了操作系统（os协作计算机的各种硬件）、语言处理程序（将高级语言和汇编语言处理成计算机可以识别和运行的程序）、服务程序（面向用户和开发者）

	应用软件则格式各样

___________


![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/fc9c3488dfdbcf6f797a21b0e9a62f45.png)

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/9eaa6749fa648d52ef1cad251c309f3d.png)


![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/faff0e557135e76bab6aaa62b9c6a5b0.png)

简而言之，我们在编写c语言程序时都是，编写高级语言程序.c
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/023b454d8fe55246534a1635b6c07ded.png)
经过编译器编译，变成.obj
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/8f5e423614e1c1ab81008618e01d1e0c.png)
并生成可执行程序.exe
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/b9df62afe2d0dc0dd1913fac4dfb217b.png)

这就是一个完整的过程


### 快捷键 


按`fn+f5`开始调试代码
`cirl+k+C`注释，`cirl+k+u`取消注释
在vscode中查找`cirl+F`
### 生成exe文件
![2025-07-03-15-03-48](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-03-15-03-48.png)
运行后exe文件保存在这里
![2025-07-03-15-04-55](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-03-15-04-55.png)
能不能运行就是未知数了
### 学习网址
菜鸟教程<https://www.runoob.com/cprogramming/c-function-memset.html>
C++官网<https://zh.cppreference.com/>


## 常用库

### \#include <stdio.h> 
```C
引用了标准库；i为input；o为output
```

### \#include <math.h>
```C
sqrt(16)//开平方
```

### \#include <stdlib.h>
```C
system();//执行系统命令
system("cls");//清空屏幕
srand();//生成随机数种子
rand();//用种子生成随机数
```

### \#define _CRT_SECURE_NO_WARNINGS
```C
scanf在VS引用的时候要在第一行加上
#define _CRT_SECURE_NO_WARNINGS
```

###  \# include <time.h>
#### time()
```C
time();//给一个地址，返回时间戳
```

### \#include <string.h>

#### strlen()
```C
int len = strlen("abc");//测长度为4，/0
```
返回值是 *size_t* 类型，即 *unsigned int* 类型









#### strcmp()
```C
if(strcmp(input,"我是猪")==0);//有点反常识
```
#### strcpy()拷贝
示例

```C
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

int main()
{
	char src[40] = { 0 };
	char dest[100]= { 0 };//字符串数组
	strcpy(src, "This is runoob.com");
	strcpy(dest, src);//拷贝
	printf("%s", src);//sr
	printf("%s", dest);//destination
}

```
不能用 *src= "This is runoob\.com"*

因为src是地址，不能被赋值

其中 *"This is runo\0ob\.com* 

*\0* 和以前的字符串都会被拷贝

目标空间必须够大，不然拷贝会涉及到越界访问

模拟实现
![2025-07-26-23-18-03](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-26-14-12-00.png)

![2025-07-26-23-18-03](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-26-23-18-03.png)

#### strcat() 字符串追加

![2025-07-26-23-19-46](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-26-23-19-46.png)

#### strncat() 特定长度字符串追加

![2025-07-27-07-32-33](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-27-07-32-33.png)

#### strncat() 特定长度字符串比较

![2025-07-27-07-41-08](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-27-07-41-08.png)

#### memset()替换

```C 
#### 
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	char str[50];

	strcpy(str, "This is string.h library function");
	puts(str);

	memset(str+8, '$', 8);
	puts(str);

	return(0);
}

```

结果

![2025-07-03-15-39-00](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-03-15-39-00.png)

### \#include <windows.h> 

```C
Sleep(1000);//休息一会再执行下一步
```

## 应用例子

```C
生成随机数：
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>//srand需要的头文件
#include <time.h>//time函数需要的头文件
int fun_random()
{
	return rand();//用种子生成随机数
}

int main()
{
	srand((unsigned int)time(NULL));//用时间生成随机数种子
	int a=fun_random();
    int b= fun_random();
	printf("%d %d",a,b);
	return 0;
}

```


## 数据类型

### 原码 反码 补码

![2025-07-08-17-13-32](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-08-17-13-32.png)
正数的原码反码补码都相等
而负数的原码的符号位为1，
负数的反码保留符号位，其他位置变成相反的
补码则是在反码的基础上加一
ps补码到原码也可以取反加一
整数在内存中存的是补码

内存中存的是2进制但给我们看是16
```C
20
0000 0000 0000 0000 0000 0000 0001 0100-原码
每四个二进制位写成16进制位
0    0    0    0    0    0    1    4
00        00        00        14  
加个0x//16进制表示符
0x 00 00 00 14

```



```C
-10
1000 0000 0000 0000 0000 0000 0000 1010-原码
0x 80 00 00 0a
1111 1111 1111 1111 1111 1111 1111 0101-反码
0x ff ff ff f5
1111 1111 1111 1111 1111 1111 1111 0110-补码
0x ff ff ff f6 
```
![2025-07-13-21-11-39](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-13-21-11-39.png)
说明内存存的是补码
```C
为什么呢？
拿1-1举例，1+（-1）如果是原码相加
0000 0000 0000 0000 0000 0000 0000 0001 原码1
1000 0000 0000 0000 0000 0000 0000 0001 原码-1
相加
1000 0000 0000 0000 0000 0000 0000 0010 变成-2
————————————————————————————————————————————————
如果是补码相加
0000 0000 0000 0000 0000 0000 0000 0001 补码1
1111 1111 1111 1111 1111 1111 1111 1111 补码-1
相加
1 0000 0000 0000 0000 0000 0000 0000 0000 丢掉第一位
0000 0000 0000 0000 0000 0000 0000 0000 变成0


```
### 取值范围

#### char类型
![2025-07-14-18-36-10](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-14-18-36-10.png)
#### short类型
![2025-07-14-18-33-38](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-14-18-33-38.png)

### 截断 与 整形提升
```C
int main()
{
	char a = -1;
	//char 和 signed char 完全一样的
	signed char b = -1;
	unsigned char c = -1;
	printf("a=%d\nb=%d\nc=%d", a, b, c);
	return 0;
}


//10000000 00000000 00000000 000000001 -1为整形的原码
//11111111 11111111 11111111 111111110
//11111111 11111111 11111111 111111111 -1的补码
//截断后
//11111111 

//如果是signed型
因为变成有符号型 ，最高位有意义
按照%d整形输出 ，需要整形提升
因为是有符号型，由于最高位是1，所以补1
//11111111 11111111 11111111 11111111
但是变为原码
//10000000 00000000 00000000 00000001 >打印出-1 


//如果是unsigned型
如果变成无符号型,
要整形提升
所以补0
//00000000 00000000 00000000 11111111
//这是无符号型
//直接打印出255
```
![2025-07-14-20-07-46](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-14-20-07-46.png)

```C
int main()
{
	char a = -128;
	printf("%u\n", a);
	//%u 打印无符号
	//10000000 00000000 00000000 10000000 >-128的原码
	//11111111 11111111 11111111 01111111 
	//11111111 11111111 11111111 10000000 >-128的补码
	//截断后
	//10000000
	//char 实际上是 unsigned char
	//先整形提升
	//而且首位是负数
	//有符号所以补1
	//11111111 11111111 11111111 10000000
	//按%u无符号打印出4294967168

	printf("%d\n", a);
	//有符号所以补1
	//11111111 11111111 11111111 10000000
	//按%d有符号打印
	//先变成原码
	//10000000 00000000 00000000 01111111
	//10000000 00000000 00000000 10000000
	//打印出-128
	return 0;
}
```
![2025-07-14-20-33-33](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-14-20-33-33.png)

```C
int main()
{
	char a = 128;
	printf("%u\n", a);
	//00000000 00000000 00000000 10000000
	//截断后
	//10000000
	//先整形提升
	//11111111 11111111 11111111 10000000
	//打印出无符号
	//4,294,967,168
	printf("%d\n", a);
	//打印出有符号
	//11111111 11111111 11111111 10000000
	//变成原码
	//10000000 00000000 00000000 01111111
	//10000000 00000000 00000000 10000000 >-128
	return 0;
}
```
![2025-07-14-21-00-10](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-14-21-00-10.png)
### 二进制相加
```C
int main()
{
	int i = -20;
	//10000000 00000000 00000000 00010100 -20的原码
	//11111111 11111111 11111111 11101100 -20的补码
	unsigned int j = 10;
	//00000000 00000000 00000000 00001010  10的原码也是补码
	printf("%d\n", i + j);
	//相加
	//11111111 11111111 11111111 11110110 -20与10相加后
	//按%d打印
	//变为原码
	//10000000 00000000 00000000 00001001
	//10000000 00000000 00000000 00001010 打印出-10
	return 0;
}
```
![2025-07-14-21-04-03](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-14-21-04-03.png)

### 正确储存
![2025-07-16-16-43-23](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-16-16-43-23.png)
-1没办法在unsigned int中储存 
```C
-1的原码
//10000000 00000000 00000000 00000001
-1的补码
//11111111 11111111 11111111 11111111
在unsigned中储存为 4,294,967,295
明显符合条件 继续循环
```
### 大小端

vs是小段，倒着存的

### 数据占用
```C
#include <stdio.h>//引用了标准库；i为input；o为output
int main()
{
printf("hehe\n");
return 0;
}
```
>记得写分号
```C
#include <stdio.h>
int main()
{
printf("%d\n",sizeof(char));//char 字符型              1
printf("%d\n", sizeof(short));//short 短整型           2
printf("%d\n", sizeof(int));//int 整型                 4
printf("%d\n", sizeof(long));//long 长整型             4
//32下是4个字节，64是8个字节
printf("%d\n", sizeof(long long));//long long 超长整形 8
printf("%d\n", sizeof(float));//float 单精度浮点型     4
printf("%d\n", sizeof(double));//double 双精度浮点型   8
return 0;
}
```
### 整型家族
```C
整型家族
char//字符本质是ASCII码值，是整型
	unsigned char
	signed char
	char
//两种属于编译器的实现
short
	unsigned short[int]
	signed short

int 
	unsigned int 
	signed int 

long
	unsigned long [int]
	signed long [int]

long long
	unsigned long long [int]
	signed long long [int]
//只有正数的是unsigned无符号
0000000000000000000000000000000000000000000
他的第一位有正负意义


//有符号的是unsigned有符号
0000000000000000000000000000000000000000000
他的第一位没有意义

```

### 浮点型
`float` 精度小
`double` 精度大


```C
#include<stdio.h>
#include<string.h>
int main()
{
	if (strlen("abc") - strlen("abcdef") >= 0)
		printf("abc>abcdef");
	else printf("abc<abcdef");
	return 0;
}
```
![2025-07-18-14-06-31](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-18-14-06-31.png)

`strlen()`求的是`unsigned int`类型
但是 $3-6=-3$
$-3$ 也应该是`unsigned int`类型 
会被转变为负数

![2025-07-16-16-43-23](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-16-16-43-23.png)

改成
```C
if (strlen("abc")>= strlen("abcdef") )
```
### 浮点型数据储存



浮点型常见数字
`3.14`
`1E10`
等等

#### 十进制转换为二进制数
$
V=(-1)^{S} \times M\times 2^{E}\\
$
___
**将5.0转换为二进制数**
$5.0 十进制\\
=101.0 二进制\\
=1.01\times 2^{2} 科学计数法\\
=(-1)^{1}\times1.01\times2^{2}\\
上面的2表示移动2位，下面的2表示几进制
所以
$
**S=1，M=1.01，E=2**
____

**将9.6转换为二进制数**
的结果是：1001.100110011001...（小数部分是循环的）。

转换方法：
整数部分（9）：
使用除2取余法：
- 9 ÷ 2 = 4 余 1
- 4 ÷ 2 = 2 余 0
- 2 ÷ 2 = 1 余 0
- 1 ÷ 2 = 0 余 1

将余数从下往上排列，得到整数部分的二进制：`1001`。
小数部分（0.6）：
使用乘2取整法：
- 0.6 × 2 = 1.2 → 取1，剩余0.2
- 0.2 × 2 = 0.4 → 取0
- 0.4 × 2 = 0.8 → 取0
- 0.8 × 2 = 1.6 → 取1，剩余0.6（开始循环）

因此小数部分的二进制是循环的：`1001...`。

最终结果为：$1001.100110011001$
$
=(-1)^{0}\times1.001100110011001...\times2^{3}\\
S=0，M=1.001100110011001...，E=3\\
$
**S=1，M=1.01，E=2**
____
#### 数据储存
![2025-07-18-17-25-28](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-18-17-25-28.png)
![2025-07-18-17-26-17](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-18-17-26-17.png)
![2025-07-18-17-28-53](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-18-17-28-53.png)
```C
int main()
{
	float t = 5.5;
	//5.5
	//101.1
	//1.011*2^2
	//S=0 M=1.011 E=2
	//32位储存
	//S=0 E=00000000 M=00000000 00000000 0000000 
	//2要加上中间数127等于=129
	//011后面全补0
	//S=0 E=10000001 M=01100000 00000000 0000000 
    //0100 0000 1011 0000 0000 0000 0000 0000
	//4    0    b	 0	  0	   0	0	 0    -> 16进制
	//0x40 b0 00 00
	return 0;
}
```
![2025-07-18-17-51-55](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-18-17-51-55.png)

#### 数据取出

E不为全0且不为全1时
```C
0 10000001 01100000000000000000000
E=10000001=129 - 127 =2
(-1)^0 * 1.01100000000000000000000 * 2^2
```
E为全0
说明很小大概在2的1-127次方左右

E为全1
说明大概是2的127次方，计成正无穷

![2025-07-18-14-39-48](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-18-14-39-48.png)
```C
#include<stdio.h>
#include<string.h>

int main()
{
	int n = 9;
	//00000000 00000000 00000000 00001001 >9的补码

	float* pFloat = (float*)&n;
	printf("n的值为：%d\n", n);
	//肯定是9
	printf("pFloat的值为：%f\n", *pFloat);
	//认为前面是浮点数
	//0 00000000 0000000 00000000 00001001
	//E为全0 E=-126 M=0.0000000 00000000 00001001
	//+ 0.0000000 00000000 00001001 * 2^126 太小了
	//%f 默认保留6位小数 所以打印 0.000000
	*pFloat = 9.0;
	//1001.0
	//1.001*2^3
	//S=0 M=1.001 E=3+127=130
	//0 10000010 0010000 00000000 00000000
	printf("num的值为：%d\n", n);
	//用%d来看待
	//010000010 0010000 00000000 00000000
	//为正数
	//1,091,567,616
	printf("pFloat的值为：%f\n", *pFloat);
	//以浮点数往外拿，保留6位 是 9.000000
	return 0;

}
```


### 构造类型

数组类型  ` int arr[]`
结构体类型`struct`
枚举类型  `enum`
联合类型 ` union`

### 指针类型


### 空类型

`void `返回类，无参数，指针



## 常量变量
### 变量
命名不能以数字开头
一般定义都要初始化为0
定义类型的本质是申请空间
```C
int a=150
float b=2.5
```

```C
scanf("%d %d", &num1, &num2);//输入函数

但是scanf在VS引用的时候要在第一行加上
#define _CRT_SECURE_NO_WARNINGS

printf("%d\n", sum);//输出函数
```

### 变量的作用域和生命周期
```C
int main()
{
       {
	int a = 20;
	}
	printf("%d\n", a);
	return 0;
}
```
此时就会报错

局部变量：作用域是变量所在的局部范围
全局变量：作用域是整个工程

如图
![2025-06-28-13-49-38](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-28-13-49-38.png)
test.c为
```C
#include<stdio.h>
extern int a;//声明引用了其他文件中的整形a
int main()
{
	printf("%d\n", a);
	return 0;
}
```
add.c为
```C
int a = 10;
```

### 常量
| 四种常量               | 说明                                                                        |
| ---------------------- | --------------------------------------------------------------------------- |
| 字面常量               | 3.14                                                                        |
| const修饰的常变量      | ```const int a = 10;```本质是变量，不能直接被修改                           |
| define定义的标识符常量 | ```#define MAX 100```                                                       |
| enum枚举常量           | `enum color{RED,GREEN,BLUE}`放在开头，且调用时用```enum color c=RED;``` |




## 字符串

打印字符串
```C
#define STR "12345"
~~~~
printf("%s\n", STR);
```

```C
char ch='a'//字符
char str="abc"//字符串
char arr1[10]="abcdef";//10如果不填会根据后面数据自动调节空间，
//而且abcdef后面自动隐藏了一个\0,结束标志,有7个字符
char arr2[] = { 'a','b','c','d','e','f'};
printf("%s\n", arr1);
printf("%s\n", arr2);
```
但是会有乱码
![2025-06-28-14-49-33](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-28-14-49-33.png)
应该主动在arr2后面补上一个终止密码子
```C
char arr2[] = { 'a','b','c','d','e','f','\0'};
```
成功
![2025-06-28-14-51-59](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-06-28-14-51-59.png)

求字符串长度
strlen是英文string length缩写
引用
```C
#include <string.h>
~~~
int len = strlen("abc")
```


### 转义字符
| 转义字符 | 意思              |
| ---- | --------------- |
| \\'  | '               |
| \n   | 换行              |
| \\\  | \               |
| \\?  | ?               |
| \0   | 终止字符串           |
| \\a  | 警告蜂鸣器           |
| \\b  | 退一个，相当与前后两个数据重叠 |
| \t   | 水平制表符           |
| \ddd | 打印8进制后的数字       |
| \xdd | 打印16进制          |

如果想打空格直接
```C
printf(" ");
```

比如\x63———99————c 
同时参考ASILL码表
<https://blog.csdn.net/jiayoudangdang/article/details/79828853>

比如我想打印123\0456
```C
应该是
printf("123\\0456");
而不是
printf("123\0456");
```
比如我想打印C:\test\test.c
```C
应该是
printf("C:\\test\\test.c");
而不
printf("C:\test\test.c");//因为\t转义成Tab
```

```C
共有14个字符，\t算一个，而且\628中八进制没有8，只能识别成\62
printf("%d\n",strlen("C:\test\628\test.c"));
```
### 打印%
```C
%d 打印整形,%4d代表向后占四位，常用来对齐
%c 打印字符
%s 打印字符串
%f 打印float
%lf 打印double
```

### 注释
用//解释性语句
和/**/来注释(简洁，最好不要嵌套注释)
```C
/*extern int a;
int main()*/
{
	printf("%d\n",strlen("C:\test\628\test.c"));
	//return 0;
}

```

## 语句结构

### 选择





### 循环
#### while循环

#### for循环
```C
int i=0;
for(i=1;i<=10;i++>)
{
	printf("")
}
最好不要像下面这样写，有些编译器不支持
for(int i=1;i<=10;i++>)
{
	printf("")
}
记得
int i=0;
for(i=1;i=0;i++>)//中间是赋值，不是取等，赋值为0后为假，不做循环。
{
	printf("")
}
```
建议for的循环变量前闭后开

#### do while
先do（做），后循环，至少循环一次
```C
do
    {循环语句;}
while(表达式);

先打印一个一到十：
int main()
{
	int i = 1;
	do 
	{
		printf("%d ", i); i++;
	} 
	while (i <= 10);
	return 0;
}
```







#### continue和break
在if内的break直接跳出循环
continue无视接下来步骤直接下一轮循环
但是会执行for中的i++

#### goto(尽量少用)
```C
#include<stdio.h>

int main()
{
again:
	printf("hehe\n");
	printf("haha\n");
	goto again;
	return 0;

}
```
不能跨函数使用，比如
```C
#include<stdio.h>
void fun()
{
	again:
}
int main()
{
	printf("hehe\n");
	printf("haha\n");
	goto again;
	return 0;

}
```
但在有些场景下非常适合




### 顺序






## 函数

### 函数声明
形参和实参可以同名
函数体内不能定义函数，也就是不能嵌套
如果引用函数在main后面，则在前面要声明 

```C
int Add(int x, int y)；//函数声明
```

### 函数封装
先创建文件
![2025-07-05-17-24-36](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-17-24-36.png)
写函数
![2025-07-08-19-40-50](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-08-19-40-50.png)
写声明
![2025-07-05-17-25-40](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-17-25-40.png)
写调用
![2025-07-05-17-26-37](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-17-26-37.png)

#### 函数卖掉
将项目生成静态库.lib文件，保护知识产权
![2025-07-05-17-46-11](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-17-46-11.png)

![2025-07-05-17-46-50](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-17-46-50.png)

![2025-07-05-17-47-47](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-17-47-47.png)
可以拿去卖了
![2025-07-05-17-48-23](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-17-48-23.png)
lib文件不可查看
![2025-07-05-17-48-44](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-17-48-44.png)

#### 函数买回
将买回来的Add.lib黏贴进项目文件夹
![2025-07-05-17-56-17](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-17-56-17.png)

导入静态库
![2025-07-05-18-02-32](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-18-02-32.png)

函数声明
![2025-07-05-18-03-07](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-18-03-07.png)

#### 函数递归
程序调用自身的编程技巧称为递归
条件：
1、存在限制条件
2、每次递归后接近限制条件
类似
$f(x)=f(x-1)+1且已知f(1)=1求f(5)$
那么我们开始求解
$ 
f(5)=f(4)+1\\
f(4)=f(3)+1\\
f(3)=f(2)+1\\
f(2)=f(1)+1\\
而f(1)=1\\
$此为递送，先向内

接着代入数值
$
f(2)=1+1=2\\
f(3)=2+1=3\\
f(4)=3+1=4\\
f(5)=4+1=5\\
$此为归，再向外

而函数递归也是同一个道理
>**:notebook_with_decorative_cover:练习：接受一个整型值（无符号）,按照顺序打印它的每一位。**
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

//%d 是打印有符号的整数（会有正负数）
//%u 是打印无符号的整数（只有正数）

int fun_print(int n)
{
	if (n > 9)
	{
		fun_print(n/10);
	}
	printf("%d ", n % 10);
}

int main()
{
	unsigned int num = 0;
	scanf("%u", &num);
	fun_print(num);
	return 0;
}
```
![2025-07-05-21-41-14](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-21-41-14.png)
红为递
紫为归

>**:notebook_with_decorative_cover:练习：不允许有临时变量，写一个函数模仿strlen()**
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

//%d 是打印有符号的整数（会有正负数）
//%u 是打印无符号的整数（只有正数）

int fun_strlen(char* strr)
{
	if (*strr != '\0')
	{
		return (fun_strlen(strr + 1) + 1);
	}
	else
	{
		return 0;
	}
}

int main()
{
	char arr[] = "adadawd";
	printf("%d", fun_strlen(arr));
	return 0;
}
```


>**:notebook_with_decorative_cover:练习：求n的阶乘，用递归**
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

//%d 是打印有符号的整数（会有正负数）
//%u 是打印无符号的整数（只有正数）

int fun_jc(int n)
{
	if (n<=1)
	{
		return 1;
	}
	else
	{
		return n * fun_jc(n-1);
	}
}

int main()
{
	int n=0;
	scanf("%d", &n);
	printf("%d", fun_jc(n));
	return 0;
}
```

>**:notebook_with_decorative_cover:练习：求n的阶乘，用迭代**
```C
int fun_jc(int n)
{
	int i=1;
	int sum=1;
	while(i<=n)
	{
		sum=sum*i;
		i++;
	}
	return sum;
}
```
其实递归不一定更好
比如要求斐波那契数列10个
用迭代法相当于正向思维
$
f(1)=1,f(2)=1\\
f(3)=f(2)+f(1)=1+1=2\\
f(4)=f(3)+f(2)=2+1=3\\
f(5)=f(4)+f(3)=2+3=5
$
用递归法相当于逆向思维
$
f(5)=f(4)+f(3)\\
f(4)=f(3)+f(2),f(3)=f(2)+f(1)\\
f(3)=f(2)+f(1),
再一一带入
$




### 函数返回
```C
printf("%d",printf(%d,printf("%d",43)));
//printf()返回长度，同时打印一遍
```
只能return一个值
所以返回多个就考虑借助结构体


### 函数的定义
```C
int Add(int x, int y)//函数头
{
	int z = 0;
	z = x + y;
	return z;//函数主体
}

在 C 语言中，函数由一个函数头和一个函数主体组成。下面列出一个函数的所有组成部分：

int 返回类型：一个函数可以返回一个值。有些函数执行所需的操作而不返回值，在这种情况下，return_type 是关键字 void。
Add 函数名称：这是函数的实际名称。函数名和参数列表一起构成了函数签名。

(int num1,int num2) 参数：参数就像是占位符。当函数被调用时，您向参数传递一个值，这个值被称为实际参数。

函数主体：函数主体包含一组定义函数执行任务的语句。

最好返回点东西，跟放回类型一致

没东西返回时 用void
void fun(void)//括号内的void明确说明fun不需要参数
{
printf("hehe"\n);
}
```


有时传入函数时不妨把序列号传进去，会有大用。



### 位置交换函数

当实参传递给形参，形参是实参的一份拷贝
对形参的修改不会影响实参
```C
//前情提要
int main()
{
	int  a = 10;
	int  *p = &a;
	a = 20;//直接改
	*p = 30;//间接改
	return 0;
}
```
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int fun_xiaohuan(int *px,int *py)
{
	int z = *px;
	*px = *py;
	*py = z;
}



int main()
{
	int a = 0;
	int b = 0;
	scanf("%d %d", &a, &b);
	fun_xiaohuan(&a, &b);
	printf("%d %d", a, b);
}
```

### 二分查找

### 函数例子
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int fun_getmax(int x,int y)
{
	int getmax = 0;

	if(x>y){ return x; }
	else { return y; }
}

int main()
{
	int a = 0;
	int b = 0;
	scanf("%d %d", &a, &b);
	int m = fun_getmax(a,b);
	printf("%d", m);
	return(0);
}
```


## 数组

数组创建
不可能实现输入自定义数组，而不限制长度
```C
char ch1[10]={'a','b','c'};
char ch2[10]="abc";
char ch1[]={'a','b','c'};
char ch2[10]="abc";
```
### 一维数组
```C
int main()
{
	int arr[]={1,2,3,4,5,6,7,8,9,10}
}
```

```C
//打印数组的每个元素的地址
for (i=0;i<cd;i++>)
{
printf("&arr[%d]=%p\n",i,&arr[i]);
}
```
![2025-07-06-21-39-55](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-06-21-39-55.png)

证明一维数组在内存中连续存放

### 二维数组
#### 二维数组创建
```C
int arr1[3][4];//三行四列
char arr2[5][10];
```
#### 二维数组初始化
```C
int arr1[3][4]={1,2,3,4,5,6,7,8,9,10,11,12};
相当于
int arr1[3][4]={{1,2,3,4},{5,6,7,8},{9,10,11,12}};

行可以省略，列不能省略
int arr[][4]={{1,2,3,4},{1,2}}
相当于
int arr[2][4]={{1,2,3,4},{1,2,0,0}}
```
#### 二维数组的使用
##### 整个数组的打印
![2025-07-06-21-57-05](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-06-21-57-05.png)
```C
int main()
{
	int arr1[3][4] = { 1,2,3,4,5,6,7,8,9,10,11,12 };

	for (int i = 0; i < 3; i++  )
	{
		for (int j = 0; j<4; j++)
		{
			printf("%2d ", arr1[i][j]);
		}

		printf("\n");
	}
}
```
![2025-07-06-22-02-56](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-06-22-02-56.png)

##### 单个数组的打印
```C
int main()
{
	int arr1[3][4] = { 1,2,3,4,5,6,7,8,9,10,11,12 };
	printf("%d", arr1[2][3]);//第三行，第四列，应该为12

}
```
![2025-07-06-22-06-33](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-06-22-06-33.png)

#### 数组越界
```C
int main()
{
	int arr[] = { 1, 2, 3, 4, 5, 6 };
	for (int i = 0; i < 10; i++)
	{

		printf("%d ", arr[i]);
	}
	return 0;
}
```
![2025-07-07-10-47-40](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-07-10-47-40.png)


### 数组名

#### 一维数组数组名

数组名本质上是数组首元素的地址
![2025-07-07-15-49-47](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-07-15-49-47.png)
```C
//数组名确实能表示首元素地址
//但是有两个例外
//1. sizeof(数组名)，这里的数组名表示整个数组，计算的是整个数组的大小，单位是字节
//2. &数组名，这里的数组名表示整个数组取出的是整个数组的地址
int main()
{
    int arr[10] = {0};
    printf("%p\n", arr);      //arr确实能表示首元素地址
    printf("%p\n", arr+1);    
    printf("\n");

    printf("%p\n", &arr[0]);  //首元素地址
    printf("%p\n", &arr[0]+1);
    printf("\n");

    printf("%p\n", &arr);     //整个数组的地址
    printf("%p\n", &arr+1);   //加一跳后面了
}
```
```C
用void fun(int*arr){}
或者void fun(int arr[]){}
来接收数组
```
#### 二维数组数组名
![2025-07-07-16-06-26](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-07-16-06-26.png)

```C
int arr[10]={0,1,2,3,4,5,6,7,8,9}
从arr[0]到arr[9]，下标，共十位
```

```C
i=0
while(i<=9>)
{
	printf("%d\n",arr[i])
}
```

如果有剩余未赋值的默认为0
如果不填长度，则会自动计算
计算数组长度

```C
cd=sizeof(arr)/sizeof(arr[0]);
```

### 字符数组
```c
char arr1[]="welcome to bit！！！";//定义字符串数组
int right=strlen(arr1)-1;
//或下面这种，不过字符串数组毕竟是字符串自带个/0,所以要-1，
//再减下标从0开始的1
//int right=sizeof(arr)/sizeof(buf[0])-2;

```
## 操作符

### 计算运算符
```C
+	把两个操作数相加	A + B 将得到 30
-	从第一个操作数中减去第二个操作数	A - B 将得到 -10
*	把两个操作数相乘	A * B 将得到 200
/	分子除以分母	B / A 将得到 2
%	取模运算符，整除后的余数	B % A 将得到 0
++	自增运算符，整数值增加 1	A++ 将得到 11
--	自减运算符，整数值减少 1	A-- 将得到 9
```
```C
int main()
{
	float a = 7 / 2.0;//出发两端有一个浮点型，结果变为浮点型
	printf("%.1f", a);//保留一位小数
	int b = 7 % 2;//取模两端都必须是整数
	printf("/d", b);
}
```
### 逻辑运算符
```C
&&	称为逻辑与运算符。如果两个操作数都非零，则条件为真。	(A && B) 为假。
||	称为逻辑或运算符。如果两个操作数中有任意一个非零，则条件为真。	(A || B) 为真。
!	称为逻辑非运算符。用来逆转操作数的逻辑状态。如果条件为真则逻辑非运算符将使其为假。

```
### 移位操作符
#### 原码反码补码

#### <<(只能对整数使用)
##### 如果是正数左移一位      
 ```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int a = 7;
	int b = a << 1;
	//其实a没变
	printf("%d\n", a);
	printf("%d\n", b);
}
```
![2025-07-08-16-55-34](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-08-16-55-34.png)
![2025-07-08-17-08-15](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-08-17-08-15.png)

##### 如果是负数左移一位  

  ```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int a = -7;
	int b = a << 1;
	//其实a没变
	printf("%d\n", a);
	printf("%d\n", b);
}
```
![2025-07-08-17-41-43](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-08-17-41-43.png)
![2025-07-08-17-40-55](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-08-17-40-55.png)


#### \>>(只能对整数使用)
##### 如果是正数右移一位  
   ```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int a = 7;
	int b = a >> 1;
	//其实a没变
	printf("%d\n", a);
	printf("%d\n", b);
}
```
 ![2025-07-08-17-53-00](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-08-17-53-00.png)
 ![2025-07-08-17-54-12](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-08-17-54-12.png)
##### 如果是负数右移一位 
Vs编译器用的是算数移位

  
### 位操作符
只适用于整型
位操作符|名字|
----|---|
&  |按位与（2进制）| 
^  |按位异或（2进制） |
\|  |按位或（2进制）|
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int a = 3;
	int b = -5;
	int c = a & b;
	//3的补码  00000000000000000000000000000011
	//-5的原码 10000000000000000000000000000101
	//-5的反码 11111111111111111111111111111010
	//-5的补码 11111111111111111111111111111011
    //&按位与，A与B同时为1才是1
	//结果为   00000000000000000000000000000011,即为3
	//%d 意味着打印一个有符号的整数
	printf("c=%d\n", c);
	
	
	
	int c = a | b;
    //|按位或，A或B为1就是1
	//结果为   11111111111111111111111111111011为补码
	//但是首位为负数
	//结果为   11111111111111111111111111111010为反码
	//结果为   10000000000000000000000000000101为原码，即为-5
	printf("c=%d\n", c);


	int c = a ^ b;
	//^按位异或，AB相同为0，相异为1
	//结果为   11111111111111111111111111111000为补码
	//结果为   11111111111111111111111111110111为反码
	//结果为   10000000000000000000000000001000为原码，即为-8

	return 0;
}
```
>**:notebook_with_decorative_cover:练习：不能创建临时变量，实现两个数的交换**
```C
int main()
{
	int a=3;
	int b=5;
	int c=0;
//第一种交换方式：
	c=a;
	a=b;
	b=c;
//第二种交换方式：
	a=a+b;
	b=a-b;
	a=a-b;
//第三种交换方式：
	a=a^b;//a=3^5
	b=a^b;//b=3^5^5=(5^5)^3=3
	a=a^b;//a=3^5^3=5
	return 0;

}
//3^3=000=0
//011^011
结论
//0^a=a
//a^a=0

//3^3^5=5
//3^5^3=5
异或支持交换律和结合律
```
>**:notebook_with_decorative_cover:练习：求一个整数储存在内存中二进制中1的个数**
```C
int a=3;

```



### 赋值运算符

```C
a = 3;
a += 3 ;//a=a+3
其他同理
```
0表示假，非0为真

```C
if(!flag){ }
b=-10
a=-b
sizeof(a)
sizeof(int)

b=++a// a=a+1 b=a
b=a++// b=a a=a+1
```

### 强制类型转换

```C
int a = (int)3.14;//向下取整
```

### 关系操作符
**~ 按位取反**
```C
int a=3;
//00011
printf("%d\n",~a)
//11100
//11011
//10100
//-4

int a=13;
//00000000000000000000001101
想将倒2位变成1
或个1上去
//或个000000000000000000000010<---(1<<1)
//变成了0000000000000000000001111
所以a |=(1<<1)即是所求00000000000000000001111

int a=29
//00000000000000000011101
想将倒5位变成0
//按位与上11111111111111101111<--- ~(1<<4)
//变成0000000000000000001101
所以a &=~(1<<4)即为所求0000000000000000001101



```

```C
!= 不是

== 是

三目运算符 int r=a>b?a;b;
```

## 关键字
关键字大全<https://c.biancheng.net/view/60bjy80.html>
### typedef关键字

typedef 


### static关键字
#### static修饰变量
将局部变量变成私有变量，防止其他源文件误用
将局部变量冻结后不销毁
```C
int test()
{
	int a = 1;
	a++;
	printf("%d ", a);
}

int main()
{
	int i = 0;
		while (i < 10)
		{
			i++;
			test();
		}
	return 0;
}
输出2 2 2 2 2 2 2 2 2 2
```
加个static
```C

int test()
{
	static int a = 1;
	a++;
	printf("%d ", a);
}

int main()
{
	int i = 0;
		while (i < 10)
		{
			i++;
			test();
		}
	return 0;
}
输出2 3 4 5 6 7 8 9 10 11
```
### static修饰函数
extern进行外部引用声明
```c
extern int Add(int x,int y)
```
同样将外部链接属性变成内部链接属性

### register关键字
电脑上的存储设备

寄存器
高速缓存
内存
硬盘

从下到上，速度越来越快，内容越来越小，造价高
```C
register int a=3；//建议电脑把数据放入寄存器
```
## define定义常量和宏
```C
#define NUM 100//定义标识符常量
#define ADD(x,y) ((x)+(y))//定义宏
对比函数
int ADD(int x,int y)
{return x+y;}
```

## 指针

什么的变量适配什么样的指针变量类型





```C
//指针变量的大小取决于地址的大小
//32位平台下地址是32个bit位即是4字节
//64位平台下是64个bit位，即是8字节
int a=10；
int* p=&a;
*p=20//解引用操作符，通过p这个地址找到p指向的对象,即a
printf("%d\n",a)
char ch='w';
int *p,*q,*r;
```
### 野指针
```C
int* p;//指针未初始化
*p=10;
```

### 字符指针
```C
int main()
{
	char ch='w';
	char* pc=&ch;
	return 0;
}

int main()
{
	char* p="abcdef";
	//字符串放在表达式中，是首字符的地址
	printf("%s\n",p)

}
```
![2025-07-18-20-32-09](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-18-20-32-09.png)
p1和p2其实是同一份只读常量
而arr1和arr2各自开辟了一串空间，地址肯定不一样
___





```C
int main()
{
	char ch='w';
	char* pc=&ch;
	return 0;
}


```
### 越界访问
```C
int arr[10]={0};
int *p=&arr[0];//或者=arr一样的
for (int i=0;i<=10;i++)
{
	*p=i;
	i++;//越界访问了
}
```

```C
int* test()
{
	int a=10;
	return &a;
}
int main()
{
int *p=test();//a被销毁
return 0;
}
//
```
 好的习惯
1. 指针初始化
2. 指针指向空间释放即使NULL
3. 避免返回局部变量的地址
4. 小心指针越界
5. 指针使用前用if检查有效性
```C
int main()
{
	int a = 10;
	int*P = &a;
	int *p2 = NULL;//说明p2是空指针
	*p2 = 100一定报错
		if (p3 != NULL)
		{
			*p3 = 100;
		}
}
```

### 指针运算
#### 指针+指针没意义
#### 指针-指针
必须是指向同一内存空间的相减才有意义
```C
int main()
{
int arr[10]={0};
printf("%d\n",&arr[9]-&arr[0]);
//结果为9，指针减去指针的绝对值为指针和指针之间的元素个数
}
```
可以用来计算字符串长度
```C
//在函数递归中也有实现
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int my_strlen(char* str)
{
	int count = 0;
	char*start = &str[0];
	while (*str != '\0')
	{
		str ++ ;
	}
	return (str-start);
}

int main()
{
	int len = my_strlen("abcdef");
	printf("%d\n", len);
	return 0;
}
```

数组用指针来访问
![2025-07-11-22-04-17](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-11-22-04-17.png)
### 指针的关系运算



### 二级指针
```C
int main()
{
int a=10;
int* pa=&a;//pa是一个一级指针变量
int** ppa=&pa;//ppa是一个二级指针变量，指向指针
//int*说明ppa指向对象pa是int*类型，*说明ppa是指针
**ppa=20;//此时a变为20
}
```
### 指针数组
存放指针的数组就是指针数组

```C




```

```C
int main()
{
	int a = 10;
	int b = 20;
	int c = 30;

	int arr[10];

	int *pa = &a;
	int *pb = &b;
	int *pc = &c;

	int *parr[10] = { &a,&b,&c };
	int i = 0;
	for (i = 0; i < 3; i++)
	{
		printf("%d\n", *(parr[i]));
	}
	return 0;
} 
```

二维数组

```C
int main()
{
	int arr1[3][4] = { 1,2,3,4,5,6,7,8,9,10,11,12 };

	for (int i = 0; i < 3; i++  )
	{
		for (int j = 0; j<4; j++)
		{
			printf("%2d ", arr1[i][j]);
		}

		printf("\n");
	}
}
```

用指针数组模拟一个二维数组

```C
int main()
{
	int arr1[4] = { 1,2,3,4 };
	int arr2[4] = { 2,3,4,5 };
	int arr3[4] = { 3,4,5,6 };

	int* parr[3] = { arr1,arr2,arr3 };
	int i = 0;
	for (i = 0; i < 3; i++)
	{
		int j = 0;
		for (j = 0; j < 4; j++)
		{
			printf("%d ", parr[i][j]);
		}
		printf("\n");
	}
	return 0;
}

```
![2025-07-11-23-01-35](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-11-23-01-35.png)

### 数组指针 
整形指针——指向数组的指针
数组指针——指向数组的指针

![2025-07-24-16-04-27](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-24-16-04-27.png)

![2025-07-24-16-05-08](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-24-16-05-08.png)

![2025-07-24-16-29-39](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-24-16-29-39.png)

说明 *\*p* 和 *arr* 是完全一样的
而 *arr* 表示的是 *arr[9]* 的首元素的地址
*arr+i* 正是下 *i* 个元素的地址
*\*(arr+i)* 才能取得该元素

![2025-07-24-16-40-10](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-24-16-40-10.png)

又说明 *&arr* 也可以取代 *\*p*
而且明显更简洁
所以说明数组指针在一维没啥用


**常见用法**

![2025-07-24-16-47-42](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-24-16-47-42.png)
我们想要打印一个二维数组

这时数组指针就发力了

![2025-07-24-17-29-09](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-24-17-29-09.png)

传过去的是 *arr* 的首元素地址，即是第一行
使 *p* 指向了*arr*的第一行

而 *\*p* 就是*arr*的第一行，
即是*arr*的第一行的首元素地址。

那么 *\*p+1*
表示*arr*的第一行的第二元素地址

那么 *\*(p+1)* 
就是*arr*的第二行，
表示*arr*的第二行的首元素地址。

那么 *\*(p+1)+1* 
表示 *arr* 的第二行的第二元素地址

那么 *\*(p+i)+j* 
表示 *arr* 的第 *1+i* 行的第 *1+j* 元素地址

在最外面加个 *\** ,取出该元素本身

### 函数指针

```C
printf("%p\n",&Add);
printf("%p\n",Add);
//这两个都可以打印函数Add的地址


int ret=(*pf)(2,3);
printf("%d\n",ret);
```
函数指针有什么用呢？
![2025-07-24-22-39-13](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-24-22-39-13.png)

 *\*pf* 与 *Add函数* 完全一样 

函数传参
![2025-07-25-14-28-42](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-25-14-28-42.png)

### 函数指针进阶
![2025-07-25-16-03-24](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-25-16-03-24.png)![alt text](2025-07-25-17-03-16.png)

#### 函数回调

下面是一个计算器
![2025-07-25-18-09-02](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-25-18-09-02.png)

#### 函数指针数组

![2025-07-25-17-27-52](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-25-17-27-52.png)

不妨使用函数指针数组来优化


![2025-07-25-18-05-39](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-25-18-05-39.png)

也叫做 *转移表*

可以利用数组随意跳转至任意函数

#### 指向函数指针数组的指针

![2025-07-26-16-37-21](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-26-16-37-21.png)

#### 函数回调进阶

冒泡函数 回调函数：

![2025-07-26-17-25-53](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-26-17-25-53.png)

![2025-07-26-17-26-10](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-26-17-26-10.png)

上面是错的

应该先强制类型转换

![2025-07-26-17-26-55](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-26-17-26-55.png)

再用 *qsort()* 函数来排序 

![2025-07-26-17-33-46](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-26-17-33-46.png)

![2025-07-26-17-32-06](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-26-17-32-06.png)

## 结构体


数据结构
数据在内存中的储存结构

线性
顺序表
链表

树形
二叉树

![2025-07-27-18-40-36](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-27-18-40-36.png)



```C
struct Student//类型
{
	//成员
	char name[20];
	int age;
	char sex[10];
	char tele[12];
}p1,p2;//记得加分号,p1,p2是全局变量
int main()
{
	struct Student stu1 = { "xiaomin",20,"nan","1888888888" };
		printf("%s %d %s %s\n", stu1.name, stu1.age, stu1.sex, stu1.tele);
	return 0;
}
```


#### 嵌套结构体 
```C

struct Peo//类型
{
	//成员
	char name[20];
	char tele[12];
	char sex[10];
	int high;
};

struct st
{
	struct Peo p;
	int num;
	float f;
};

int main()
{

	struct st  s = { {"李四","1559878679","女",166},100,3.14f };
	printf("%s %s %s %d %d %f\n", s.p.name, s.p.tele, s.p.sex, s.p.high, s.num, s.f);
	
}
```

#### 结构体内存对齐

![2025-07-27-19-43-34](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-27-19-43-34.png)


节省空间，最好把占用小的结合在一起



#### 结构体传参
```C

struct Peo//类型
{
	//成员
	char name[20];
	char tele[12];
	char sex[10];
	int high;
};
void print2(struct Peo* sp)
{

	printf("%s %s %s %d\n", sp->name, sp->tele, sp->sex, sp->high);//结构体指针->成员变量
}

void print1(struct Peo p)
{
	printf("%s %s %s %d\n", p.name, p.tele, p.sex, p.high);//结构体变量.成员变量
}

int main()
{
	struct Peo  p1 = { "张三","1131418679","男",181 };
	print2(&p1);//可以用两种方式
	print1(p1);

}
```

#### 位段

一种节省空间的结构体

![2025-07-27-19-58-03](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-27-19-58-03.png)

#### 位段的内存分配

按 4 byte - 32 bit 来开辟

#### 枚举

![2025-07-27-20-41-24](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-27-20-41-24.png)

#### 共用体
每一次只能安全使用一个变量，是一种极省空间的做法。


![2025-07-27-21-06-02](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-27-21-06-02.png)



## 内存

## getchar()函数
C语言中的getchar函数

在C语言中，getchar()函数用于从标准输入（通常是键盘）读取一个字符。它的返回值是读取的字符的ASCII码值。如果读取失败或到达文件末尾，getchar()会返回EOF（End Of File），其实际值为-1。

示例
```C
#include<stdio.h>
int main()
{
	char ch ;
	while ((ch=getchar()) != 'EOF')
	{
		putchar(ch);
	}
	return 0;
}
```

注意事项

getchar()每次只能读取一个字符。如果输入缓冲区中有多个字符，它会依次读取每个字符。

输入时，必须按下回车键才能结束输入并将字符传递给程序。回车键本身也被视为一个字符，并且在输出时会导致换行。

如果在使用getchar()之前已经使用了如scanf()这样的函数读取了输入，则可能需要清空输入缓冲区以避免读取意外的字符，如残留的回车符。

清空输入缓冲区

为了避免getchar()读取到意外的回车符或其他残留字符，可以使用以下代码片段来清空输入缓冲区：
### 清空缓存
```C
char temp;
while ((temp = getchar()) != '\n' && temp != EOF);
```
这段代码会读取并丢弃缓冲区中直到下一个换行符或文件结束符的所有字符。

总结来说，理解getchar()函数如何工作以及如何处理输入缓冲区是使用它时避免错误和混淆的关键。
```C
int main()
{
	    char password[20] = { 0 };
		printf("请输入密码");
		scanf("%s", password);
		printf("请确认密码（Y/N）");
		char temp;
		while ((temp = getchar()) != '\n' && temp != EOF);
		int ret = getchar();
		if ('Y' == ret)
		{
			printf("Yes\n");
		}
	else 
	{
			printf("No\n");
	}
		return 0;
}
```
```C
char ch='\0';//前面有提过，\0为字符串最后的结束字符
while((ch=getchar())!=EOF)
{
if(ch<'0'||ch>'9') continue;//字符比大小比的是ASCLL码大小
putchar(ch);
return 0;//只打印数字字符
}
```

## 调试
*Debug版本*调试版本
*Realse版本*经过优化便于发布



按`fn+f9`加断点
![2025-07-12-16-50-21](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-12-16-50-21.png)
按`fn+f10`运行到下一行
![2025-07-12-16-53-45](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-12-16-53-45.png)
再左边点击
![2025-07-12-16-55-37](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-12-16-55-37.png)
按`fn+f12`打开调试
![2025-07-12-16-32-01](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-12-16-32-01.png)

`fn+f5`模式只看断点

但`fn+f10`模式从主函数第一行
![2025-07-12-17-02-09](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-12-17-02-09.png)
按`fn+f10`模式可以一行一行调试
而`fn+f5`可以退出调试


`fn+f11`模式支持进入函数调试
要在*Debug*模式下进行

`fn+f1` 帮助

`fn+f2` 改名


## 动态内存管理

![2025-07-27-21-09-21](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-27-21-09-21.png)
![2025-07-27-21-31-24](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-27-21-31-24.png)

## 柔性数组


## 链表















## 动态数组

```C


```


## 文件管理


c语言已经帮我们定义好了一个叫FILE的的结构体类型
```c
typedef struct
{


short level;
unsigned flags;
chat fd;
unsigned char hold;
short bsize;
unsigned char* buffer;
unsigned ar*  curp;
unsigned istemp;
short token;


}FILE;

```
### 1、文件的基本操作
#### 文件指针
我们在使用时只用这样就可以

```c
FILE *fp;

```

#### 打开文件
```C
FILE *fp;
fp=fopen(文件名，使用文件方式)

FILE *fp1;
fp1=fopen("123.txt"，"r")

//下面是用if语句来读取打开文件的常用模块
if (((fp=fopen("E:\\exp1.txt","r"))==NULL)  
{
	printf("不能打开文件，按任意键结束")
	getchar();
	exit(0);
}


```

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/233adf463197563a1216a6fa5799d6d0.png)
#### 关闭文件
```C
fclose(文件指针)
```

### 2、文件的读写


#### 把字符写入文件
```C
fuptc(ch,fp)
//ch是一个字符型变量,fp是文件指针
```
#### 从文件中读取字符
 ```C
fgetc(fp)
//ch是一个字符型变量,fp是文件指针

//下面是用循环来读取完整文件的一个常用模块
ch=fgetc(fp);
while(ch!=EOF)
{
	putchar(ch);
	ch=fgetc(fp);
}//只要不等于EOF（end of file文件末尾）,就循环读取

```

#### 把字符串写入文件
```C
fputs(字符串,文件指针);
```
#### 从文件中读取字符串
```C
fgets(接受字符串的变量,n（代表个数）,文件指针)
```
#### 将数据格式化输入到文件中

```C
fprintf(文件指针,格式字符串,输出列表);
```
#### 从文件中格式化读取数据

```C
fscanf(文件指针,格式字符串,输入列表)
```
#### 将数据块输出到文件中
```C
fwrite(buffer,size,count,fp);
//buffer存放数据块的地址
//size要读取多少个字节
//cout要读取几个字节块
//fp文件指针
```
#### 从文件中读取数据块
```C
fread(a,2,3,fp);
//这里的a最好是一个数组指针，因为有好几块

```

### 3.文件的定位
#### 移动文件指针的函数

```C
fseek(文件类型指针,位移量,起始点);
-20L代表向后移动20个字节，而一个字符刚好一个字节，即20个字符,1从开头
```

#### 重置文件指针的函数
```C
rewind(fp);
```



#### 得到文件指针当前位置的函数
```C
ftell(fp);
```


### 3.文件管理

#### 删除文件
```C
remove(char* filename);
filename="E:\\exp1.txt"
```
#### 重命名文件
```C
ftell(fp);
```
#### 复制文件

```C
ftell(fp);
```


