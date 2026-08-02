
# 一些错题

#### 1.
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/f24a21104177c4db3640b0ea0437d71c.png)

#### 2.
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/164f387820b4020f73ef4946d63812cc.png)



### 3.本地化
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/86ed840c8ce40b5d1810bcc5ed342312.png)


### 4.
实型数
a<0
写成a<1e-6
小于10的-6次方默认他为0


### 5.优先级运算

### 6.++i 与 --i

自增和自减运算符放在变量前面是前缀形式，放在后面是后缀形式。
当自增或自减作为表达式运算的一部分时，若运算符放在变量前，变量先完成自增或自减运算，再以新值参与表达式运算；就把++i加个括号（++i）

若放在变量后，变量先以原值参与表达式运算，运算完成后再进行自增或自减。

具体体现在
#### 6-1

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/5514a717d7d320b2274b8b27bfe0d84b.png)

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/3e61f85b6eb1f4d4fecee05003cdfe1b.png)

#### 6-2(极易错)

设有int x=11;,则表达式（x++ \* 1/3)的值是（）

因为++在后面，要先算x \* 1/3 =3

而++并不是让表达式加，而是 x 自身++

所以最后结果还是3



### 7.优先级


![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/95661c197de0da2bbd0953d0ad1e4ff7.png)

先a*a=144,a=1，a=12-144=-132，a=-132+-132=-264

括号>复杂>小学运算>左右移动>大等于>等于不等于>按位>赋值运算符>逗号


### 8.逻辑短路

#### 8.1


![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2ba0a92572bcd4ad85de090174ddc21a.png)

x++为自增后置，先运算后自增，-1 的逻辑值为真，依据或运算的短路 性质，++y不执行

#### 8.2
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/de7629766101e441eb0dd2288bf9a441.png)![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/18ff8a1956a322ee21e5d8be5f91f0d4.png)

x=11为真，然后或在后面运算，所以x=11已经决定了该式为真

### 9.转义字符

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/3d2ff37ae4486d5364c0c37876825b2e.png)


其实是不合法的

\ddd 例如 \65,\123 ,表示 将八进制的65变成十进制，即53,对应ascII码为5

6\*8e1+5\*8e0=53 

\xhh 例如\x34,表示将十六进制的34变成十进制，即52,对应ascii码为4

3\*16e1+4*16e0=52

### 10.常见的AscII码值

65——A

49——0

### 11.a\<b\<c
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/0a47628371297a1a0b761613904d7cbd.png)

### 12.x/3与x%3
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/3e8e57d1194e0226c9b87cb3ea40298f.png)


![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/78d8afd152c7ba490a59cc71f10b14d9.png)
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/f80c02dca61569eed570186a052a3a61.png)



### 13.float要用%f ，double要用%lf


```C
#include "stdio.h"

int main()
{
	float a[100];
	int num = 0;
	float sum = 0;
	for (int i = 0; i < 100; i++)
	{

		scanf_s("%f", &a[i]);
		if ((a[i]-(-1))<1e-5)
			break;
		num++;
	}
	for (int i = 0; i < num; i++)
	{
		sum = sum + a[i];
	}
	printf("%.2f", (float) sum / num);
}
```


一个将多位数
转换为数组的式子
```C
	int num;
	scanf_s("%d", &num);
	
	int len;//计算长度
	int n = 1;
	for (int i = 0;; i++)
	{
		n = n * 10;
		
		if ((num - n) < 0)
		{
			len = i+1;
			break;
		}
	}

	printf("%d\n", len);

	int a[100];
	for (int i = 0; i < len; i++)
	{
		a[len - i - 1] = num % 10;
		num = num / 10;
	}
	
	for (int i = 0; i < len; i++)
		printf("%d,", a[i]);
```

```C
#include "stdio.h"
#include "math.h"
int main()
{
	int num;
	scanf_s("%d", &num);

	int a[100] = {0};
	int len = 0;

	for (int i = 0;; i++)
	{
		a[i] = num % 16;
		num = num / 16;
		if (num == 0) { len = i + 1; break;  }
	}


	for (int i = len-1; i >= 0; i--)
	{
		if(a[i]<10)
		printf("%d", a[i]);
		else 
			printf("%c",(char)a[i]+55);
	}
}
```

```C
#include "stdio.h"
#include "math.h"
int main()
{
	int a, b, c,ex_a_people,ex_a_o, ex_a_b_o,ex_a_b_people;
	for (int a = 0; a <= 100; a++)
	{
		ex_a_people = 200 - a;
		ex_a_o = 200 - 2 * a;

		for (int b = 0; b <= ex_a_people; b++)
		{
			ex_a_b_o = 200 - 2 * a - b;
			ex_a_b_people = 200 - a - b;
			c = ex_a_b_people;
			if ((c / 2) >= ex_a_b_o)
				printf("%d %d %d\n", a, b, c);
		}
	}

}
```


先*再++
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/3cfebabf27d8d71ae590078e1d56b948.png)