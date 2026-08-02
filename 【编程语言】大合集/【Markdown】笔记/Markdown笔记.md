# Markdown入门教程
关山难编写
___
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-05-21-56-00.png)
### 标题编号语法教学 
<!-- 先ctrl+shift+p选定，Create Table of Contents -->
- [Markdown入门教程](#markdown入门教程)
        - [林君睿编写](#林君睿编写)
    - [标题编号语法教学](#1标题编号语法教学)
    - [标题语法教学](#标题语法教学)
    - [段落语法教学](#段落语法教学)
    - [换行语法教学](#换行语法教学)
    - [强调语法教学](#强调语法教学)
  
    - [引用语法教学](#引用语法教学)
    - [列表语法教学](#列表语法教学)
    - [代码块语法教学](#代码块语法教学)
    - [图片引用语法教学](#图片引用语法教学)
    - [链接语法教学](#链接语法教学)
    - [字体字号语法教学](#字体字号语法教学)
    - [表格语法教学](#表格语法教学)
    - [脚注和上下标语法](#脚注和上下标语法)
    - [术语定义语法教学](#术语定义语法教学)
    - [删除线语法教学](#删除线语法教学)
    - [任务框语法教学](#任务框语法教学)
    - [转义字表符教学](#转义字表符教学)
    - [警告框 ：\*\* 不要按下大红色按钮！](#警告框--不要按下大红色按钮)
    - [视频](#视频)
    - [数学公式](#数学公式)


____
### 标题语法教学 

<!-- #与后面内容间必须空一格 -->

# Heading level 1
## Hedding level 2
### Hedding level 3
#### Hedding level 4

Heading level 1
=====
Hedding level 2
-----
___
### 段落语法教学 
<!-- 需要空一行 -->
Moreover,numberous studies claim that addiction to technology is real,and it has the same effect on the brain as drug addiction.

Therefore,it is advisable for modern people to reasonably reduce their addction to technology while enjoying the convenience brought by it,Nothing should go overboard.
___
### 换行语法教学 
Therefore,it is advisable for modern people <br>to reasonably reduce their addction to technology <br>while enjoying the convenience brought by it,<br>Nothing should go overboard.

___
### 强调语法教学 
<!-- 最好用星号 -->
Therefore,it is **advisable** for *modern* people to reasonably ***reduce*** their addction to technology while enjoying the convenience brought by it,Nothing should go overboard.
___
### 引用语法教学 
>Therefore,it is advisable for modern people to reasonably reduce their addction to technology while enjoying the convenience brought by it,Nothing should go overboard.

>Therefore,it is advisable for modern people <br>to reasonably reduce their addction to technology <br>while enjoying the convenience brought by it,<br>Nothing should go overboard.

>Therefore,it is advisable for modern people
>to reasonably reduce their addction to technology
>while enjoying the convenience brought by it,
>Nothing should go overboard.

>Therefore,it is advisable for modern people
>
>> to reasonably reduce their addction to technology while enjoying the convenience brought by it,
>
>Nothing should go overboard.

>there is quotes
>
>>This is two quot
>>
>>>this is three quote
>>>this is three quote
>>
>>This is two quote
>
>This is one quote
___
### 列表语法教学 
<!-- 加空格 -->
1. 第一个
2. 第二个
    1. 第二1个
    2. 第二2个
3. 第三个

- 第一个
- 第二个
  - 第二1个
  - 第二2个
- 第三个
<br>
- 第一个
- 第二个
    第二1个
    第二2个
- 第三个
<br>
- 第一个
- 第二个
  >第二1个
>第二2个
- 第三个
<br>
- 第一个
- 第二个
 
___
### 代码块语法教学 

#### 一些常见的表情符号

开心：`(⊙ᗜ⊙)` `（‐＾▽＾‐）` ` ٩(๑òωó๑)۶` `ヾ（≧?≦）〃` `Ctrl+Alt`
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
```
    
```markdown
# Heading level 1
<!-- 表示一级标题 -->
## Hedding level 2
<!-- 表示二级标题 -->
### Hedding level 3
<!-- 表示三级标题 -->
```

___
### 图片引用语法教学 

<!-- 

./ 当前目录
../ 上级目录
/ 根目录

（慎用！不同系统可能解析不同） -->

单一声明
![this is a dog](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/dog1.jpg )
<!-- 利用html引用图片 -->
<img src="https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/dog1.jpg" alt="狗" width="50%" style="margin: 0 auto;"/>

全局说明

![][img1]
![][img2]


[img1]: https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/cat1.jpg  "蓝眼小猫"
[img2]:  https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/cat2.jpg "黄眼小猫"

___
### 链接语法教学 
这是一个[通往百度的入口](https://www.baidu.com/  "https://www.baidu.com/" )
这是一个[打开我的markdown入门教程](我的Markdown笔记.md  "我的Markdown笔记.md" )
欢迎访问<https://www.baidu.com/>
欢迎访`//www.example.com`
___
### 字体字号语法教学 

<font face="仿宋" color=red size=10 >这是宋体</font>

<style>
.usual {font-style:normal; font-size:120% ; font-family:"Times New Roman"}
</style>

<font class="usual">这是全文通用字体</font>
___

### 表格语法教学 
| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |

| |第1排|第2排|第三排|
|---|-----|-------|--|
|第一桌|小明|小红|小江|
|第二桌|小蓝|小兔|小肖|
___
### 脚注和上下标语法 

《芙蓉楼送辛渐》
寒雨连江夜入吴，平明[^1]送客[^2]楚山孤。
洛阳亲友如相问，一片冰心在玉壶。

上标：^18^H
下标：H~2~O



[^1]: 平明： 天亮的时候。
[^2]:  客： 指作者的好友辛渐。
___
### 术语定义语法教学 

well
: adv.好，出色地; 完全地，彻底地; （表示程度）多少，怎样; 很，相当; 远远地; 很可能地
adj.健康的; 情况良好的; 可取的
int.（语气词）嗯，唔; 哟; 噢，哦; 不过; 好了; 那么; 算了
n.井; 楼梯井
v.涌出，冒出; （情感）迸发
___
### 删除线语法教学 
~~世界是平坦的。~~ 我们现在知道世界是圆的。
___
### 任务框语法教学 

- [ ] 写作业
- [ ] 背单词
- [x] 打游戏
____
### 转义字表符教学
通过在前面`\`解决问题
\{}
\>
#
\#
### 警告框 ：

> :memo: **注意：** 日出很美。

> :bulb: **提示：** 记得珍惜生活中的小事。

### 视频 
<iframe height="400" width="600" src="https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/71/10/1409781071/1409781071-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1750084499&gen=playurlv2&os=bcache&oi=730828620&trid=0000740a0f4be28b4ed8a8a5e736a5287b61h&mid=0&platform=html5&og=cos&upsig=91a1c38df5610609660668f49d994f3a&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=14715&bvc=vod&nettype=0&f=h_0_0&bw=44787&logo=80000000" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>


### 数学公式 
$\sum_{i=1}^{n}{X_i^2} $
<!-- LateX在线编辑 -->
欢迎光临Latex在线编辑器<https://www.latexlive.com/home>
这个是markdown中latex的使用说明<https://www.cnblogs.com/Rosmarinus/articles/15553532.html>
关于换行的说明<https://blog.csdn.net/xiazdong/article/details/8892105>

