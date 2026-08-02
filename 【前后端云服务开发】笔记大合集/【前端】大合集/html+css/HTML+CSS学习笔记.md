·# HTML+CSS学习笔记
关山难编写

_____

### 快捷键使用

*Vscode* 用 *!* 自动生成html骨架

*cirl + /*   注释

*cirl + g*   跳转指定行

*shift + alt + 下箭头* 快速复制

*cirl +f*  查找

*cirl +alt + 上箭头/下箭头* 多光标

*shift +alt +鼠标* 选中区块

*alt + f* 格式化

![2025-07-30-22-29-49](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-30-22-29-49.png)

![2025-07-30-20-06-56](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-30-20-06-56.png)

**Web3标准**

*html* 结构

*css* 装饰

*js* 动作

## HTML基础上

|        标签名        |   定义   |              说明               |
| :---------------: | :----: | :---------------------------: |
|  `<html></html>`  | HTML标签 |       页面中最大的标签，我们称为根标签        |
|  `<head></head>`  | 文档的头部  |  注意在head标签中我们必须要设置的标签是title   |
| `<title></title>` | 文档的标题  |       让页面拥有一个属于自己的网页标题        |
|  `<body></body>`  | 文档的主体  | 元素包含文档的所有内容，页面内容基本都是放到body里面的 |

基本骨架

![2025-07-30-20-10-30](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-30-20-10-30.png)


### 标签

*文档类型声明标签*

![2025-07-30-20-41-09](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-30-20-41-09.png)

*使用语言*

![2025-07-30-20-43-37](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-30-20-43-37.png)

en 为英文
zh-CN 为中文

但定义没什么，主要是提醒开发人员


*字符集*

![2025-07-30-20-47-23](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-30-20-47-23.png)

UTF-8 是万国码储存了几乎所有的字符集，否则有乱码情况 ，最普遍


### 常用标签


```html
<h1>这是一个标题</h1>

<a href="https://www.runoob.com">这是一个链接</a>

<img src="/images/logo.png" width="258" height="39" />

<p>这是另外一个段落。</p>

<br> //换行

<html> 元素定义了整个 HTML 文档。
```


### 全局属性

全局属性是所有 HTML 元素都可以使用的属性。
```html

id：为元素指定唯一的标识符。

<div id="header">This is the header</div>

class：为元素指定一个或多个类名，用于 CSS 或 JavaScript 选择。

<p class="text highlight">This is a highlighted text.</p>

style：用于直接在元素上应用 CSS 样式。

<p style="color: blue; font-size: 14px;">This is a styled paragraph.</p>

title：为元素提供额外的提示信息，通常在鼠标悬停时显示。

<abbr title="HyperText Markup Language">HTML</abbr>

data-*：用于存储自定义数据，通常通过 JavaScript 访问。

<div data-user-id="12345">User Info</div>

```

### HTML 文本格式化标签

| 标签                                                     | 描述     |
| :----------------------------------------------------- | :----- |
| [b](https://www.runoob.com/tags/tag-b.html)            | 定义粗体文本 |
| [em](https://www.runoob.com/tags/tag-em.html)          | 定义着重文字 |
| [i](https://www.runoob.com/tags/tag-i.html)            | 定义斜体字  |
| [small](https://www.runoob.com/tags/tag-small.html)    | 定义小号字  |
| [strong](https://www.runoob.com/tags/tag-strong.html)  | 定义加重语气 |
| [sub](https://www.runoob.com/tags/tag-sub.html)        | 定义下标字  |
| [sup](https://www.runoob.com/html/m/tags/tag-sup.html) | 定义上标字  |
| [ins](https://www.runoob.com/tags/tag-ins.html)        | 定义插入字  |
| [del](https://www.runoob.com/tags/tag-del.html)        | 定义删除字  |

## CSS教程

###  选择器

CSS 中 id 选择器以 "#" 来定义。

在 CSS 中，类选择器以一个点 . 号显示

```css
#para1 { text-align:center; color:red; }
```

合并选择器
```css
p,h3 { text-align:center; color:red; }
```
### 三种引入方式

![20260126145935](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260126145935.png)

1. 内部样式（多个页面间容易混乱）
```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        #para1

        {

            text-align:center;

            color:red;

        }

    </style>

</head>

<body>

    <p id="para1">这是一个段落</p>

</html>
```


2. 内联样式 （不同标签间混乱）


```html
<p style="text-align:center; color:red;">这是一个段落</p>
```

3. 外部样式

.css文件
```css
#para1{

    text-align:center;

    color:red;

}
```

.html文件
```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <link rel="stylesheet" href="1.css">

</head>

<body>

    <p id="para1">这是一个段落</p>

</html>
```

![20260126150920](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260126150920.png)

\*为全局选择器

###  CSS 背景

CSS 属性定义背景效果:

- background-color
- background-image
- background-repeat
- background-attachment
- background-position 从图片的哪个区域选

```html
<body style="background-image: url('https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260126151500.png');">
```
如果你不想让图像平铺，你可以使用 background-repeat 属性:


```css
body  
{  
background-image:url('img_tree.png');  
background-repeat:no-repeat;  
}
```

- background-size
[CSS3 background-size 属性 | 菜鸟教程](https://www.runoob.com/cssref/css3-pr-background-size.html)
### 文本
```css
/*文字的颜色*/
body {color:red;}
h1 {color:#00ff00;}
h2 {color:rgb(255,0,0);}

/*文本的对齐方式*/
h1 {text-align:center;}
p.date {text-align:right;}
p.main {text-align:justify;}

/*用来删去链接的下划线*/
a {text-decoration:none;}


h1 {text-decoration:overline;}
h2 {text-decoration:line-through;}
h3 {text-decoration:underline;}

/*文本缩进属性*/
p {text-indent:50px;}
```

### 字体
```css

/*字体家族*/
p{font-family:"Times New Roman", Times, serif;}

/*斜体设置*/
p.normal {font-style:normal;}  
p.italic {font-style:italic;}  
p.oblique {font-style:oblique;}

/*字体大小*/
h1 {font-size:40px;}
/*字体粗细*/
p.normal {font-weight:normal;} 
p.thick {font-weight:bold;} 
p.thicker {font-weight:900;}
```

### 表格
```css
table { border-collapse:collapse; } 
table,th, td { border: 1px solid black; }


table { width:100%; } th { height:50px; }


如需控制边框和表格内容之间的间距，应使用td和th元素的填充属性：
td { padding:15px; }
```

### 盒子

![20260126160848](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260126160848.png)

- **Margin(外边距)** - 清除边框外的区域，外边距是透明的。
- **Border(边框)** - 围绕在内边距和内容外的边框。
- **Padding(内边距)** - 清除内容周围的区域，内边距是透明的。
- **Content(内容)** - 盒子的内容，显示文本和图像。

[CSS Border(边框) | 菜鸟教程](https://www.runoob.com/css/css-border.html)

### 轮廓

轮廓（outline）是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用。

轮廓（outline）属性指定元素轮廓的样式、颜色和宽度。

### 外边距

**margin:25px 50px;**

- 上下边距为25px
- 左右边距为50px

### 关系选择器
```css
p{ }: 为所有 **p** 元素指定一个样式。
.marked{ }: 为所有 **class="marked"** 的元素指定一个样式。
.marked p{ }: 为所有 **class="marked"** 元素内的 **p** 元素指定一个样式。 p.marked{ }: 为所有 **class="marked"** 的 **p** 元素指定一个样式。


后代选择器
ul li{
}

子代选择器
div>p{
}

相邻兄弟选择器
h3+p{
}
只有p生效，且在html中向下选择一个

通用兄弟选择器
h3~p{
}
下面的p生效
```


### 所有CSS 尺寸 (Dimension)属性

| 属性                                                                   | 描述         |
| -------------------------------------------------------------------- | ---------- |
| [height](https://www.runoob.com/cssref/pr-dim-height.html)           | 设置元素的高度。   |
| [line-height](https://www.runoob.com/cssref/pr-dim-line-height.html) | 设置行高。      |
| [max-height](https://www.runoob.com/cssref/pr-dim-max-height.html)   | 设置元素的最大高度。 |
| [max-width](https://www.runoob.com/cssref/pr-dim-max-width.html)     | 设置元素的最大宽度。 |
| [min-height](https://www.runoob.com/cssref/pr-dim-min-height.html)   | 设置元素的最小高度。 |
| [min-width](https://www.runoob.com/cssref/pr-dim-min-width.html)     | 设置元素的最小宽度。 |
| [width](https://www.runoob.com/cssref/pr-dim-width.html)             | 设置元素的宽度。   |
### CSS Display(显示) 与 Visibility（可见性）

visibility:hidden可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被隐藏了，但仍然会影响布局。

display:none可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元素原本占用的空间也会从页面布局中消失。

### 如何改变一个元素显示
```css
li {display:inline;}
  
span {display:block;}
```


### 浮动

![20260126170849](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260126170849.png)
### 清除浮动

.text_line { clear:both; }

### 定位
#### 相对定位
```css
h2.pos_right { position:relative; left:20px; }
```

#### 绝对定位
```css
h2 { position:absolute; left:100px; top:150px; }
```

#### fix定位
元素的位置相对于浏览器窗口是固定位置。
即使窗口是滚动的它也不会移动：
```css
p.pos_fixed
{
    position:fixed;
    top:30px;
    right:5px;
}
```
## CSS3

### 弹性盒子

弹性容器通过设置 display 属性的值为 flex 或 inline-flex将其定义为弹性容器

`flex-direction`的值有:

- row：横向从左到右排列（左对齐），默认的排列方式。
- row-reverse：反转横向排列（右对齐，从后往前排，最后一项排在最前面。
- column：纵向排列。
- column-reverse：反转纵向排列，从后往前排，最后一项排在最上面。

justify-content 语法如下：

justify-content: flex-start | flex-end | center | space-between | space-around

各个值解析:

- **flex-start：**  
  
    弹性项目向行头紧挨着填充。这个是默认值。第一个弹性项的main-start外边距边线被放置在该行的main-start边线，而后续弹性项依次平齐摆放。
    
- **flex-end：**  
  
    弹性项目向行尾紧挨着填充。第一个弹性项的main-end外边距边线被放置在该行的main-end边线，而后续弹性项依次平齐摆放。
    
- **center：**  
  
    弹性项目居中紧挨着填充。（如果剩余的自由空间是负的，则弹性项目将在两个方向上同时溢出）。
    
- **space-between：**  
  
    弹性项目平均分布在该行上。如果剩余空间为负或者只有一个弹性项，则该值等同于flex-start。否则，第1个弹性项的外边距和行的main-start边线对齐，而最后1个弹性项的外边距和行的main-end边线对齐，然后剩余的弹性项分布在该行上，相邻项目的间隔相等。
    
- **space-around：**  
  
    弹性项目平均分布在该行上，两边留有一半的间隔空间。如果剩余空间为负或者只有一个弹性项，则该值等同于center。否则，弹性项目沿该行分布，且彼此间隔相等（比如是20px），同时首尾两边和弹性容器之间留有一半的间隔（1/2*20px=10px）。

权重
 flex: 2;
### 圆角
 border-radius

阴影
border-shadow

### 动画



- `:hover`，还有很多其他有用的伪类，例如：
- `:active`：元素被用户激活时（比如鼠标按住不放）。
- `:focus`：元素获得焦点时（常见于输入框 `<input>`）。
- `:first-child`：作为其父元素的第一个子元素时。

```css
div{

    width: 200px;

    height: 200px;

    background-color: blue;

    animation: myfirst 5s infinite;
    
    请对这个元素应用名为 `myfirst` 的动画规则，让它每次播放都持续 5 秒钟，并且无限循环地播放下去。

}

div:hover{

    animation-play-state: paused;

}

  

@keyframes myfirst{

    0%   {background: red;}

    25%  {background: yellow;}

    50%  {background: blue;}

    100% {background: green;}

}
```

opacity:0 完全透明

### 媒体查询

<meta name="viewport" content="width=device-width, initial-scale=1.0">

## JavaScript

var定义变量

### 三种引入方案

第一种 内部引用
```html
```HTML
<script>
	var a = 80977;
	console.log(a);
</script>
```

第二种 外部引用

```HTML
<script src="./2.js">

   </script>
```

在.js中这样写
```js
    var a = 80977;
     console.log(a);
```

第三种 联网引用

```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

### 注释
```html
<!--我是注释-->
```

```css
/*我是注释*/
```

```js
/*我是注释*/
//我是注释
```

### 输出方式

```js

//弹出窗口
alert("hello world");

//输出到页面中
document.write("man");

//输出到控制台
console.log("what can i say")
```

### 数据类型
#### 值类型

**值类型(基本类型)**：字符串（String）、数字(Number)、布尔(Boolean)

当您声明新变量时，可以使用关键词 "new" 来声明其类型：

var carname=new String;



```js
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
//对象相当于C的结构体

person.lastName;
//访问对象的属性

```
### 函数
定义函数

函数就是包裹在花括号中的代码块，前面使用了关键词 function

```html
<p>点击这个按钮，来调用带参数的函数。</p> 

<button onclick="myFunction('Harry Potter','Wizard')">点击这里
</button> 

<script>
 function myFunction(name,job)
 { alert("Welcome " + name + ", the " + job); } </script>

```

```html
    <script >

        var a=10;

        var b=3;

        function add(x,y){

            return x+y;

        }

        console.log(add(a,b));

    </script>
```

### 事件

格式如下

```html
<button onclick="getElementById('demo').innerHTML=Date()">现在的时间是?
</button>
```

|事件|描述|
|---|---|
|onchange|HTML 元素改变|
|onclick|用户点击 HTML 元素|
|onmouseover|鼠标指针移动到指定的元素上时发生|
|onmouseout|用户从一个 HTML 元素上移开鼠标时发生|
|onkeydown|用户按下键盘按键|
|onload|浏览器已完成页面的加载|

### 数组

```js
var arr=['132','123','12'];
console.log(arr[0]);//从零开始索引
```


```js
//多维数组
var arr=[24,'lin junrui',['man','out','what can isay']]
arr[2][2]
//输出what can i say

user.length  长度属性
有括号的叫方法，没括号的叫属性
```

#### 数组遍历

```js
  var arrr=[1,2,3,4,5];

        for(var i=0;i<arrr.length;i++){

            console.log(arrr[i]);

        }
```

#### 数组方法

```js

//isArray判断是否是数组类型
var arr=[1,2,3,4,5];

    flag=Array.isArray(arr);

    console.log(flag);

//数组末尾添加
var arr=[1,2,3,4,5];

   arr.push(6);

    console.log(arr);

//数组末尾减去
 var arr=[1,2,3,4,5];

   arr.pop();

    console.log(arr);
    
    
 //数组首位删去
   var arr=[1,2,3,4,5];

   arr.shift();

    console.log(arr);
 
 //数组首位加上
   var arr=[1,2,3,4,5];

   arr.unshift(6);

    console.log(arr);
    
    
 //清空数组
        var arr=[1,2,3,4,5];

 while(arr.length>0){

    console.log(arr.shift());

 }

 console.log('最终数组：',arr);
 
 //join连接
  var arr=[1,2,3,4,5];
    console.log(arr.join(''));
 
 //用join和split可以实现字符串和数组的互换
 
 
 //concat把多个数组合并
  var arr = [1, 2, 3, 4, 5];

        var str = [5, 6];

        console.log(arr.concat(str));
        
  //reverse 颠倒
    var arr = [1, 2, 3, 4, 5];

        console.log(arr.reverse(Array));
        
   //indexOf 存在返回下标，不存在返回-1
   
```
### 字符串

你可以使用索引位置来访问字符串中的每个字符：

你可以在字符串中使用引号，字符串中的引号不要与字符串的引号相同

可以用转义字符来实现

var character = carname[7];

可以使用内置属性 **length** 来计算字符串的长度：

换行要在末尾夹反斜杠\n

#### 字符串方法
https://www.runoob.com/js/js-strings.html#:~:text=%E5%B1%9E%E6%80%A7%E5%92%8C%E6%96%B9%E6%B3%95-,%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%96%B9%E6%B3%95,-%E6%9B%B4%E5%A4%9A%E6%96%B9%E6%B3%95%E5%AE%9E%E4%BE%8B


```js
//charAt读取
 console.log(str1.charAt(0));//读第一位                 

//concat连接
str3=str1.concat(str2)
str4=str1.concat(str2,str3)

//substring 提取,不包含第二个位置
str1.substring(1,5)

//substr 从起始索引号提取字符串中指定长度的字符
str2.substr(2,5)

//indexOf() 返回字符串中检索指定字符第一次出现的位置，不存在返回-1
 var str1="h2adawdawda";
console.log(str1.indexOf("a"));//放回2
console.log(str1.indexOf("a",5));//从第四个开始查找

//trim 移除字符串首尾空白,不改变原字符

//split
str.split("|") //按|来分割

```

### 对象

```js
  var user = {

            name: "Alice",

            age: 30,

            city: "New York",

            student_information: {

                school: "beike",

                school_id: "U21131"

            },

            getName: function () {

                console.log("Name: " + user.name);

  

            }

        }

        user.getName();//函数调用

        console.log("Age: " + user.age);

        console.log("City: " + user.city);

        console.log("School: " + user.student_information.school);//链式调用

        console.log("School ID: " + user.student_information.school_id);
```

#### math对象
```js
    var a = -1;

       console.log(Math.abs(a));//返回a的绝对值

    console.log(Math.max(...arr));//返回数组中最大值

 var b = 2.2;

       console.log(Math.floor(b));//向下取整
       
       ceil//向上取整


//生成min~max之间的随机数
function getRandomArbitrary(min, max) {

        result=Math.random() * (max - min) + min;

        console.log(result);

    }

    getRandomArbitrary(5,10);

```

### Date对象

```js

time1=Date.now();

new Date(time1);

new Date();

new Date().getMonth()+1

```

## DOM

![20260127230214](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260127230214.png)

```js
        var divs = document.getElementsByTagName("div")[0]; //用标签名
        divs.innerHTML = "Welcome";


        var text = document.getElementsByClassName("class1")[0];//用类名，0表示指定第一个
        console.log(text);


        var name = document.getElementsByName("login");//用name属性
        console.log(name)

        var root = document.getElementById("2");//用id
        console.log(root);

		var nav=document.querySelector(".nav")//用css选择器
        console.log(nav)
		
		var navs=document.querySelectorAll(".nav")[0]//用css选择器选全部
        console.log(navs)

```

创建

```js
		
		var text=document.createElement("p");//在页面上创建p节点
        var content=document.createTextNode("我是文本");//创建文本内容节点
        var id=document.createAttribute("id"); //创建一个id属性的节点
        id.value="root1";//创建一个id属性的节点的值为root
        text.appendChild(content); //把文本内容节点放入指定p节点
        text.setAttributeNode(id); //加一个id属性
        
        
        var container=document.createElement("div"); //获取页面上的div节点
        container.appendChild(text); //把text放进去
		document.body.appendChild(container);//在页面中展示

```

```html
 <style>
        .box {
            width: 200px;
            height: 200px;
        }
        .red {
            background-color: red;
        }
    </style>
<body>

  
    <div class="box" id="root">1213</div>

    <script>
        var root = document.getElementById('root');
        root.id = "root";
        root.className = "box red";
        console.log(root);
        console.log(root.classList.remove('red'));

        if (root.classList.contains('red')) {

            console.log('包含red类');

        } else {

            console.log('不包含red类');
        }

        var http = "<a href='https://www.baidu.com'>百度</a>";
        root.innerHTML = http; //读取或用来改写标签内的内容，可以识别标签
        console.log(root);
        root.innerText = http; //读取或用来改写标签内的内容，全看成字符串
        console.log(root);
    </script>

  

</body>

  

</html>
```

```js
 var http = "<a href='https://www.baidu.com'>百度</a>";

        root.innerHTML = http;
        
               root.innerText = http; //把标签识别成字符串
```

获取元素位置

![20260126160848](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260126160848.png)

```html
    <style>
        .box {
            width: 200px;
            height: 200px;
            border: 5px solid black;
            /*边框*/
            padding: 20px;
            /*内边距*/
            margin: 20px;
            /*外边距*/
            background-color: red;
        }

        .biaoti {
            height: 900px;
            background-color: rgb(42, 79, 112);
        }
    </style>
    <script>
        var root = document.getElementById('root');
        console.log(root.clientHeight); //元素的高度，包含内边距，不包含边框和外边距
        console.log(root.clientWidth); //元素的宽度，包含内边距，不包含边框和外边距
        console.log(document.documentElement.clientHeight); //可视部分高度
        console.log(document.body.clientHeight); //body主体总高度
        console.log("-------------------------");

        console.log(document.documentElement.scrollHeight); //可滚动高度
        console.log("-------------------------");
        console.log(root.offsetHeight); //元素高度包含边框
        console.log(root.offsetTop);//到父级元素的高度
    </script>

```

css操作

```html
    <script>
        //方法一，加内部样式
        var box = document.getElementById("root");
        box.setAttribute("style", "width:200px;height:200px;background:green");
        console.log(box);

        //方法二
        box.style.border = "5px solid red"
        box.style.background = "blue"

        //方案三
        box.style.cssText = "width:200px;height:200px;background:green"

    </script>
```

### 事件处理程序

#### html事件
```html

  <button onclick="clickHandle()">按钮</button>
    <script>
        function clickHandle() {
            console.log("按钮被点击了");
        }
    </script>
```

> html的缺点，js和html没有分开
#### DOM0集
```html
    <button id="btn">按钮</button>

    <script>

        var btn = document.getElementById("btn");

        btn.onclick = function () {

            console.log("按钮被点击了");

        }

    </script>
```

![20260211155253](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260211155253.png)


> 缺点，只会出现一个事件
#### DOM2级


```html
    <button id="btn">按钮</button>
    <script>
        var btn = document.getElementById("btn");
        btn.addEventListener("click",
         function () {
            console.log("按钮被点击了");
        }
    )
    </script>
```


### 鼠标事件

![20260211160035](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260211160035.png)



```html
 <style>
        .box1 {
            width: 200px;
            height: 200px;
           background-color: pink;
        }
 </style>



  

<body>
    <button id="btn1">单机</button>
    <button id="btn2">双击</button>
    <button id="btn3">按下</button>
    <button id="btn4">双击</button>
    <div id="div1" class="box1">
    </div>
    <script>
        var btn1 = document.getElementById("btn1");
        btn1.onclick = function () {
            console.log("单机事件");
        }
        var btn2 = document.getElementById("btn2");
        btn2.ondblclick = function () {
            console.log("双击事件");
        }
        var btn3 = document.getElementById("btn3");
        btn3.onmousedown = function () {
            console.log("鼠标按下事件");
        }
        var btn2 = document.getElementById("btn2");
        btn2.onmouseout = function () {
            console.log("鼠标移出事件");
        }
        var div1 = document.getElementById("div1");
        div1.onmousemove = function () {
            console.log("鼠标移动事件");
        }
    </script>
</body>
```

#### Event 事件对象
```html
<body>
  <button id="btn">按钮</button>
    <script>
        var btn = document.getElementById("btn");
        btn.onclick = function (event) {
            event.target.innerHTML = "单机了";
            console.log(event.type);
        }
    </script>
</body>
```



### JS6





```	bash

# 安装 cnpm
npm install -g cnpm --registry=https://registry.npmmirror.com
# 使用 cnpm 安装模块
cnpm install [模块名]

```

[Babel 是什么？ · Babel 中文文档 | Babel中文网](https://www.babeljs.cn/docs)



```bash
cnpm install --save-dev @babel/core
```











```json
{

  "presets": [

  ],

  "plugins": [

  ]

}
```



![20260212210611](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212210611.png)



```cmd
 cnpm install --save-dev @babel/preset-react
```

