# C++学习 基于C
关山难编写
_____

## 一、C++对C的增强

![2025-07-28-20-42-58](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-28-20-42-58.png)

### 1.命名空间
使用系统库函数的三种方式

方式一

![2025-07-28-20-48-29](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-28-20-48-29.png)

方式二

![2025-07-28-20-51-01](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-28-20-51-01.png)

方式三

![2025-07-28-20-50-28](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-28-20-50-28.png)


### 2.bool类型的增强

bool 一个字节

true 1

false 0


### 3.三目运算符的加强

在C++里 三目运算符返回变量

而C里 三目运算符放回值

### 4.const的增强

在C语言中
```const int a = 10;```本质是变量，不能直接被修改,但可以通过地址修改

在C++

```const int a = 10;``` 直接变成常量

![2025-07-29-00-46-42](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-00-46-42.png)

说明在对常量取地址时，临时开辟一个空间

### 5.枚举的增强

C语言

![2025-07-29-00-50-09](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-00-50-09.png)

字面量太多时，记不清楚

可以用数字来代替枚举类型偷懒

C++中不允许用数字代替枚举类型

**string字符串类型**

![2025-07-29-02-58-35](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-02-58-35.png)

**引用**

b是a的引用，可以理解为a的别名

![2025-07-29-01-09-36](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-01-09-36.png)

**const修饰指针**

*常量指针* `const int* p=&a;`

指针的指向可以修改

但是指针指向的值不可以修改

`*p=20` :x:指针的值不可以改

`p=&b` :white_check_mark:指针指向可以改

*指针常量*`int* const p=&a`

指针的指向不可以修改

但是指针指向的值可以修改

`*p=20` :white_check_mark:指针的值不以改

`p=&b` :x:指针指向不可以改


*常量指针常量*` const int* const p=&a`

都不可以改

**结构体数组**
用 *X . Y* 来操作
![2025-07-29-03-04-13](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-03-04-13.png)

**结构体指针**

用 *X -> Y* 来操作






## 二、内存四区


### 1.代码区

写的代码
共享、只读

### 2.全局区

全局变量

静态变量 static

全局常量 （const）

### 3.栈区

由编译器自动分配释放

:heavy_exclamation_mark:注意事项：不要返回局部变量的地址'

局部变量存放在栈区，栈区的数据在函数执行完自动释放

第一次可以打印正确的数字,但第二次会错

### 4.堆区

C++ 用 *new* 来在堆区开辟数据




开辟变量

![2025-07-29-18-10-06](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-18-10-06.png)

开辟数组

![2025-07-29-18-10-26](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-18-10-26.png)

`delete` 运算符用于释放之前使用 `new` 分配的内存。

## 三、引用

### 引用的基础语法

![2025-07-29-20-15-18](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-20-15-18.png)

引用传参可以改变原值

![2025-07-29-20-13-39](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-20-13-39.png)

:x:错误示范 不要放回局部变量的引用

函数结束后销毁

第一次成功只是编译器的保留机制

![2025-07-29-20-25-30](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-20-25-30.png)

:white_check_mark:正确示范

用 *static* 将局部变量变成静态变量

![2025-07-29-20-26-59](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-20-26-59.png)

如果函数的返回值是引用，这个函数可以作为左值

![2025-07-29-20-40-06](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-20-40-06.png)

### 引用的本质

引用的本质在C++内部实现是一个指针常量

即

指向的值可以改变

指向的对象不可以改变

![2025-07-29-21-05-21](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-21-05-21.png)

只要是发现ref是*引用*，会自动帮我们解引用


### 常量引用

const 修饰

![2025-07-29-21-16-42](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-21-16-42.png)

引用场景

![2025-07-29-21-22-53](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-29-21-22-53.png)

防止修改

 cmath数学库

|序号|函数 & 描述|
|---|---|
|1|**double cos(double);**  <br>该函数返回弧度角（double 型）的余弦。|
|2|**double sin(double);**  <br>该函数返回弧度角（double 型）的正弦。|
|3|**double tan(double);**  <br>该函数返回弧度角（double 型）的正切。|
|4|**double log(double);**  <br>该函数返回参数的自然对数。|
|5|**double pow(double, double);**  <br>假设第一个参数为 x，第二个参数为 y，则该函数返回 x 的 y 次方。|
|6|**double hypot(double, double);**  <br>该函数返回两个参数的平方总和的平方根，也就是说，参数为一个直角三角形的两个直角边，函数会返回斜边的长度。|
|7|**double sqrt(double);**  <br>该函数返回参数的平方根。|
|8|**int abs(int);**  <br>该函数返回整数的绝对值。|
|9|**double fabs(double);**  <br>该函数返回任意一个浮点数的绝对值。|
|10|**double floor(double);**  <br>该函数返回一个小于或等于传入参数的最大整数。|



随机数
```Cpp

#include <iostream>
#include <ctime> 
#include <cstdlib>
 
using namespace std;
 
int main ()
{
   int i,j;
 
   // 设置种子
   srand( (unsigned)time( NULL ) );
 
   /* 生成 10 个随机数 */
   for( i = 0; i < 10; i++ )
   {
      // 生成实际的随机数
      j= rand();
      cout <<"随机数： " << j << endl;
   }
 
   return 0;
}
```

c++数学常数
```Cpp
### π
std::numbers::pi
### e
std::numbers::e
### φ 黄金比例
std::numbers::phi
```

相比C，加入了string类型
```Cpp
string str1 = "runoob";
```

关于时间

```cpp


// 基于当前系统的当前日期/时间 
time_t now = time(0); 

// 把 now 转换为字符串形式 
char* dt = ctime(&now);

//把 now 转换为tm的结构体形式,便于格式化输出 
tm* ltm = localtime(&now);

// 输出 tm 结构的各个组成部分 
cout << "年: "<< 1900 + ltm->tm_year << endl; 
cout << "月: "<< 1 + ltm->tm_mon<< endl; 
cout << "日: "<< ltm->tm_mday << endl; 
cout << "时间: "<< ltm->tm_hour << ":"; 
cout << ltm->tm_min << ":"; 
cout << ltm->tm_sec << endl;
```


基本输入输出

| 头文件                                                                 | 函数和描述                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [iostream](https://www.runoob.com/cplusplus/cpp-libs-iostream.html) | 该文件定义了 **cin、cout、cerr** 和 **clog** 对象，分别对应于标准输入流、标准输出流、非缓冲标准错误流和缓冲标准错误流。 |
| [iomanip](https://www.runoob.com/cplusplus/cpp-libs-iomanip.html)   | 该文件通过所谓的参数化的流操纵器（比如 **setw** 和 **setprecision**），来声明对执行标准化 I/O 有用的服务。     |
| [fstream](https://www.runoob.com/cplusplus/cpp-libs-fstream.html)   | 该文件为用户控制的文件处理声明服务。我们将在文件和流的相关章节讨论它的细节。                                    |
所以良好的编程实践告诉我们，使用 cerr 流来显示错误消息，而其他的日志消息则使用 clog 流来输出。


 C++ vector 容器

C++ 中的 vector 是一种序列容器，它允许你在运行时动态地插入和删除元素。
vector 是基于数组的数据结构，但它可以自动管理内存
```cpp

std::vector<int> vec2 = {1, 2, 3, 4}; // 初始化一个包含元素的 vector

myVector.push_back(7); // 将整数 7 添加到 vector 的末尾

//可以使用下标操作符 [] 或 at() 方法访问 vector 中的元素：
int x = myVector[0]; // 获取第一个元素
int y = myVector.at(1); // 获取第二个元素

int size = myVector.size(); // 获取 vector 中的元素数量

//可以使用迭代器遍历 vector 中的元素：
for (auto it = myVector.begin(); it != myVector.end(); ++it) {
    std::cout << *it << " ";
}

//可以使用 erase() 方法删除 vector 中的元素：

myVector.erase(myVector.begin() + 2); // 删除第三个元素


//可以使用 clear() 方法清空 vector 中的所有元素：
myVector.clear(); // 清空 vector

```


## 面向对象

私有区域定义数据，在公有区域定义相关的函数

```cpp
# 创建一个Box类
class Box {
 public: double length; // 盒子的长度 
double breadth;// 盒子的宽度 
double height; // 盒子的高度 };

#创建一个Box类的Box对象
Box Box1;

```

c++的类的成员函数得在里面声明，在外面定义
```c++
class Box { 
public: 
double length; 
void setWidth( double wid );
 double getWidth( void ); 
 private:
  double width; };
  
 // 成员函数定义

  double Box::getWidth(void) { return width ; }
```

多父类继承

```cpp
class <派生类名>:<继承方式1><基类名1>,<继承方式2><基类名2>,…
{
<派生类类体>
};
```

## C++ 中的函数重载

在同一个作用域内，可以声明几个功能类似的同名函数，但是这些同名函数的形式参数（指参数的个数、类型或者顺序）必须不同。您不能仅通过返回类型的不同来重载函数。

下面的实例中，同名函数 **print()** 被用于输出不同的数据类型：

## 实例
```C++
#include <iostream> 
using namespace std;
 class printData 
 { public: 
 void print(int i) 
 { cout << "整数为: " << i << endl; }
  void print(double f) 
  { cout << "浮点数为: " << f << endl; }
   void print(char c[]) 
   { cout << "字符串为: " << c << endl; } }; 
   
   
   int main(void) { 
   printData pd; 
   
   // 输出整数 
   pd.print(5);
   
    // 输出浮点数 
    pd.print(500.263);
     
    // 输出字符串 
    char c[] = "Hello C++"; 
    pd.print(c); 
    
    return 0; }
```

|**成员函数**|**非成员函数（全局函数）**|
|---|---|---|
|**比喻**|类**自带的技能**|一个**外部的独立工具**|
|**调用形式**|`box1 + box2` -> `box1.operator+(box2)`|`box1 + box2` -> `operator+(box1, box2)`|
|**参数个数**|**1 个** (另一个是 `this` 指针，即对象自己)|**2 个** (需要明确提供所有操作数|









