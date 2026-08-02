# Python笔记

编写:关山难

______

## 一、前言

#### 配置python环境


![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/592243c36f0389c4be1d649c4113a26c.png)

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/63de790b895c91fc53601d7ab69bc7dc.png)
#### 使用vscode来写python程序
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/a68cac7c09769c5500958d40d5358bc9.png)


### 使用pycharm来写python程序

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/79fbbb00904a47f39e2ffe40f83777bc.png)
## 一、基础语法
### 输出 


```python
print('b')  
print(chr(98)) #转换成对应字符  
print(chr(56)) #转换成对应字符 
  
#   在UTF-8即万国码规定中，中文字体的取值是uE400——u9fa5  

print(ord('北')) #输出北对应的U码  
  
print(chr(21271)) #输出21271对应的U码 
  
  
'''输出到文件中'''
fp=open('note.txt','w')  
  
print('北京欢迎您',file=fp)  #得用GBK编码
  
fp.close() #关闭文件


'''print的完整用法'''
print('北京',20,sep=' ',end='-->',file=None) #sep代表分隔，end代表结尾，file可以将内容输出到文件中
print('北京欢迎'+'您') #加号只能是字符串跟字符串连


```

### 输入

输入默认是字符串，需要自己强转

```python

x=input('提示文字\n')  
  
name=input('请输入姓名\n')  
print('我的姓名是:',name,sep='',end='\n')  
  
num=input('请输入数字\n')  
num=int(num) #强制类型转换  
print('您的数字是:',num,sep='',end='\n')



若一行有多个输入，空格分隔
a,b=input("").split()


```

### 注释
```python 
# coding=utf-8
# 中文声明注释,一定要写在第一行

#单行注释


'''
多行注释
'''
或者
"""
多行注释
"""

```

### 代码缩进
——python的特色，通过缩进来表示程序逻辑

### 转义字符

\n  换行符
\t  水平制表符
\\"  双引号
\‘  单引号
\\\   一个反斜杠

加前面加r或R，则该转义字符失效

### 保留字
保留字（相当于C语言中的关键字） 
```python
import keyword #引入库  
print(keyword.kwlist) #查询
''' 
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'  共35个
 '''
print(len(keyword.kwlist)) #查询保留字的个数
#保留字严格区分大小写
```

### 标识符

相当于变量名，同规范

一些规范：
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/df21e64d86feb200e3b3d83a6d1f8824.jpg)
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/27dbd165a44c79387815b990cab4674d.jpg)
### 变量

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/8b36d6f97a27e89fefb597de3a0d4ae0.jpg)
python支持动态变量，可以直接用赋值语句修改类型，不用强转

```python

a='abc'
print(type(a))#查看a此时的类型
a=5 #这样转换类型是合法的
print(type(a))

d=e=100 #这样赋值也是合法的
print(id(d))
print(id(e))#这两个函数用来查看地址，他们的地址也会相同

```



### 常量
```python

PI=3.14

```

### 运算符
#### 算术运算符
不同于C
Python的除法\\不会自动向下取整（且输出结果默认是小数），但依旧用\\\来保留这个功能
而且增加了求幂功能**
#### 逻辑运算符

&&且(与)在Python中变成了and
｜｜或在Python中中变成了or
!非在Python中变成了not



## 二、数据类型
### 1.数值类型

#### 整数类型

十进制 无
二进制 0b
八进制 0o
十六进制 0x


```python
num =987
num2=0b101010   #2进制表示
num3=0o765      #8进制表示
num4=0x87abf    #16进制表示

print(num)
print(num2)
print(num3)
print(num4)

'''
输出的是他们自动以十进制输出
——————-输出如下———————
987
42
501
555711
——————————————————
'''


```
#### 浮点数类型
```python

x=10  
y=10.0  
z=1.99E143  #科学计数法  
print("x的数据类型：",type(x))  
print("y的数据类型：",type(y))  
print("z的数据类型：",type(z))

'''
——————-输出如下———————
x的数据类型： <class 'int'>
y的数据类型： <class 'float'>
z的数据类型： <class 'float'>
——————————————————
'''

```


```python
'''
复数类型
实数用 `.real` ，虚数用`.imag` 表示
'''

x=123+456j
print("实数部分：",x.real)
print("虚数部分：",x.imag)


'''——————-输出如下———————
实数部分： 123.0
虚数部分： 456.0
——————————————————'''

```

#### 字符串类型
字符串是不可变类型
```python
city='天津'  
info='''特色：相声  
演员：郭德纲'''  
print(city)  
print(info)

s = 'abcdef'  
print(s[1:5]) #左闭右开，从零计数
输出'bcde'

a = '1'  
print(a+a) #左闭右开，从零计数
输出'11'


```

### 2.序列
#### 列表list
————C的数组+结构体的复合
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

列表用 [ ] 标识，是 python 最通用的复合数据类型。

```python
#!/usr/bin/python 
# -*- coding: UTF-8 -*- 
li = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john'] 
print li # 输出完整列表 
print li[0]# 输出列表的第一个元素
print li[1:3] # 输出第二个至第三个元素 
print li[2:] # 输出从第三个开始至列表末尾的所有元素 
print tinylist * 2 # 输出列表两次 
print li + tinylist # 打印组合的列表


'''——————-输出如下———————
['runoob', 786, 2.23, 'john', 70.2]
runoob
[786, 2.23]
[2.23, 'john', 70.2]
[123, 'john', 123, 'john']
['runoob', 786, 2.23, 'john', 70.2, 123, 'john']
——————————————————'''



```
也可以加第三个参数
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20251007191541.png)

#### 元组tuple
元组是另一个数据类型，类似于列表。

元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。


#### 切片运算符

 \[ \]用来 取 元组 、列表、字符串的一部分
\[3:5]代表从第四个数到第六个数（但不包括第六个）

#### 集合set

同数学中的定义一样，集合是一种具有无序性和唯一性的集合。
用{ }来表示
因为无序性，所以索引没有意义，进一步来说切片也没有意义

```python

a={1,2,2,3,3,4,5}

print(a)
'''——————-输出如下———————
{1,2,3,4,5}
——————————————————'''
```

####  字典dict

```python
#每一个键值对（item）都由键（key）和值（value）构成
d={'age':2,'name':'linjunrui'}  
print(type(d)
print(d['name'])//用键来访问值
'''——————-输出如下———————
<class 'dict'>
linjunrui
——————————————————'''

```

### 3.转换类型
#### 显示转换类型

```python

#简单转换
b=int(1231.11)

#字符串的转换
c=float('13.5')
但是
d=int('ad')就会报错

#序列间的转换

set([1,2,3])#将列表转换为集合
tuple({5,6,7})#将集合转换为元组
list('hello')#将字符串转换为列表

dict([1,2],[3,4])#将两个二元列表变字典
{1:2,3:4}


```

## 三、语法结构部分

### 分支结构

```python
#python中的if后面是冒号，且严格缩进，中间的分支用elif
num=5
if num>0:
	print("是正数")
elif num<0:
	print("是负数")
else:
	print("是零")
```

支持if的嵌套语句，但是要严格缩进

### 循环结构

for循环用来遍历序列，如list，tuple,string 等
```python

numbers=[6,5,3,5,131,6]
sum=0;

for val in numbers:
	sum=sum+val

print("总和是",sum)

```

```python

range(10)
range(start,stop,step_size)#start代表起始位，stop代表结束位，step_size代表步长，左闭右开

genre=['pop','rock','jazz']
for i in range(len(genre)):
	print("I like",genre[i])


```

带有else的循环

for循环也有一个可选的else块，不同于在末尾直接加一个语句，如果for循环中出现了break则会忽略这个语句。

### break，continue与pass
pass是一个占位语句，不做任何事情


## 四、面向对象

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/04f4ac18b5f182e8af2d235856aa24aa.png)



#### 面向对象技术简介

- **类(Class):** 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
- **方法：** 类中定义的函数。
- **类变量：** 类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- **数据成员：** 类变量或者实例变量用于处理类及其实例对象的相关的数据。
- **方法重写：** 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
- **局部变量：** 定义在方法中的变量，只作用于当前实例的类。
- **实例变量：** 在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
- **继承：** 即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
- **实例化：** 创建一个类的实例，类的具体对象。
- **对象：** 通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

### 类的方法


```python
#!/usr/bin/python3 
class MyClass: """一个简单的类实例""" 
	i = 12345 
	def f(self): return 'hello world' # 实例化类 
		x = MyClass() # 访问类的属性和方法 
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
```

#### 类的__init__()方法


类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法

```python
#!/usr/bin/python3

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
```
#### 类的普通方法

类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的**第一个参数名称**, 按照惯例它的名称是 self 即类自身名字的代表。

```python

class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)

# 创建一个类的实例
obj = MyClass(42) 

# 调用实例的方法
obj.display_value() # 输出 42

```


```python

#!/usr/bin/python3
 
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people('runoob',10,30)
p.speak()

```

### 类的继承

子类（派生类 DerivedClassName）会**继承**父类（基类 BaseClassName）的属性和方法。

	BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

我们一起来读两段代码大概就能明白继承的用法了

```python
class Fruit:  
    color = "绿色"  #实际上是Fruit.color
    def harvest(self, color):  
        print("水果是：" + color + "的！")  
        print("水果已经收获......")  
        print("水果原来是：" + Fruit.color+"的！")  
  
class Apple(Fruit):  
    color="红色"  #实际上是Apple.color
    def __init__(self):  
        print("\n我是苹果")  
	     #自动继承父类的非init方法
	     #相当于在这里添加一段
        #def harvest(self, color):  
	        #print("水果是：" + color + "的！")  
	        #print("水果已经收获......")  
	        #print("水果原来是：" + Fruit.color+"的！")  
        
  
class Orange(Fruit):  
    color="橙色"  
    def __init__(self):  
        print("\n我是橘子")  
  
apple=Apple()  #先在创建实例时调用init方法，又继承了 定义了harvest方法
apple.harvest(apple.color)  #调用harvest方法
orange=Orange()  
orange.harvest(orange.color)

```


```python
#!/usr/bin/python3
 
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        #相当于把上面一行代码替换成下面这一段
        #self.name = n
        #self.age = a
        #self.__weight = w
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
s = student('ken',10,60,3)##创建时自动执行init方法
s.speak()
```



## 五、模块与包


Python 中的模块（Module）是一个包含 Python 定义和语句的文件，文件名就是模块名加上 .py 后缀。

模块可以包含函数、类、变量以及可执行的代码。通过模块，我们可以将代码组织成可重用的单元，便于管理和维护。

### 模块的作用

- **代码复用**：将常用的功能封装到模块中，可以在多个程序中重复使用。
    
- **命名空间管理**：模块可以避免命名冲突，不同模块中的同名函数或变量不会互相干扰。
    
- **代码组织**：将代码按功能划分到不同的模块中，使程序结构更清晰。

### 使用import导入模块

假设已经在同级目录下创建了一个demo.py文件和demo2.py

我们就可以用import导入

demo2.py中代码如下
```python
def my_printf():  
    print("Hello World")
```

demo.py中代码如下
```python
import test  
test.my_printf()
```

但是我们不想写test.怎么办，这是就可以使用别名，用别名操控导入的模块
```python
import test as m
m.my_printf()
```

或者我们可以使用 **from...import...** 来引用

```python
from test import my_printf
my_printf()
```

如果用    **from 模块名 import\***  那么就引入这个模块中的所有函数

### 包是什么


![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/c4cb0fcbefb3fb53b2331e0235e931d4.png)


我们在一个项目中，一个入口程序，还有几个包文件夹，包文件夹下存放我们的模块
，模块中需要包含一个 **__init\_\_.py** 作为这个包的默认执行程序，只要引用了包就会执行它，它的模块名是包的名字即chap2


我们一般使用 **from 包名.模块名 import 函数** 来引入

使用 **from 包名.模块名 import \*** 来引入模块中不以下滑线(**\_**)开头的所有函数

我们有时候不想执行模块内的程序，只想引用模块内的函数怎么办

我们可以在模块内使用使用 **if** 来封装模块内的程序

```python
def my_printf():  
    print("Hello World")  
      
if __name__ == '__main__':  
    print("该模块运行无误")
```

当单独运行该模块时输出该模块运行无误

当被引用时只运行my_printf()内的的程序

### 导入标准模块

我们可以在程序中直接使用 **import 标准模块名** 来导入标准模块

更多标准模块详见
[Python3 标准库概览 | 菜鸟教程](https://www.runoob.com/python3/python3-stdlib.html)

### 第三方模块下载和安装

在终端中使用指令

**>pip 指令 参数**

```
pip install numpy #安装numpy模块即科学计算模块
```

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/3d8553d7d4ee6dea84dfedef8fc359f5.png)















接下来要学的

类型注释
模块与包
wen