# C语言刷题集

关山难编写


题目多来自牛客竞赛、洛谷、鹏哥



____
![2025-07-01-18-06-29](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-01-18-06-29.png)

## 简单

### 练习：ASCII码
BoBo教KiKi字符常量或字符变量表示的字符在内存中以ASCII码形式存储。BoBo出了一个问题给KiKi，转换以下ASCII码为对应字符并输出他们。
73, 32, 99, 97, 110, 32, 100, 111, 32, 105, 116 , 33
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
 
int main()
{
    int arr[] = {73, 32, 99, 97, 110, 32, 100, 111, 32, 105, 116 , 33 };
    int i = 0;
    int cda = sizeof(arr) / sizeof(arr[0]);
    while (i < cda)
    {
        printf("%c", arr[i]);
        i++;
    }
    return 0;
}
```

### 练习：计算n的阶乘
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	int result = 1;
	int i = 1;
	int n = 1;
	scanf("%d", &n);
	while (i <= n)
	{
		result = result * i;
		i++;
	}
	printf("%d", result);
}
```
### 练习：计算1!+2!+3!.....+n!
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int sjc(int w)//求阶乘，这个函数是给一个w，输出w的阶乘wj
{
	int i = 1;
	int wj = 1;
	while (i <= w)
	{
		wj = wj * i;
		i++;
	}
	return wj;
}

int main()
{ 
	int result = 0;
	int n = 1;
	int k = 1;

	scanf("%d", &n);
	while (k <= n)//让k从一开始，让result保存结果
	{
		result = result + sjc(k);
		k++;
	}
	printf("%d", result);
}
```
### 练习：有序列表二分查找
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int fun_BinSea(int arr[], int  k, int  cd)//二分查找函数
{
	int	left = 0;
	int  right = cd - 1;

	while (left <= right)
	{
		int mid = left + (right - left) / 2;//其实就是取平均数
		if (arr[mid] < k) {
			left = mid + 1;
		}
		else if (arr[mid] > k) {
			right = mid - 1;
		}
		else { return mid; }
	}
	return -1;
}
	int main()
{
	int arr[] = { 1,2,3,4,5,6,7,8,9,10 };
	int k = 7;
	int cd = sizeof(arr) / sizeof(arr[0]);
	int ret = fun_BinSea(arr, k, cd);
	if (ret == -1)
	{
		printf("找不到\n");
	}
	else
	{
		printf("找到了，下标是：%d", ret);
	}
	return 0;
}
```


### 练习：用大小来猜数字
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>//srand需要的头文件
#include <time.h>//time函数需要的头文件
#include <Windows.h>
int fun_random()
{
	return (rand() % 100 + 1);
}
int game()
{
	int guess = fun_random();
	int input = 0;
	printf("已经生成随机数%d\n", guess);

	while (1)
	{    
		printf("请猜数字：>");
		scanf("%d", &input);
		if (input > guess) { printf("猜大了\n"); }
		else if (input < guess) { printf("猜小了\n"); }
		else { printf("猜对了\n"); Sleep(1000); system("cls"); break; }
	}
}
int menu()
{
	printf("******************\n");
	printf("****1.开始游戏*****\n");
	printf("****0.退出程序*****\n");
	printf("******************\n");
}
int main()
{
	srand((unsigned int)time(NULL));
	int choose = 0;
	do {
		menu();

		scanf("%d", &choose);
		switch (choose)
		{
		case 1: Sleep(500); system("cls"); game();  break;
		case 0:system("cls"); printf("退出游戏成功\n"); Sleep(1000);  break;
		default:system("cls"); printf("选择错误，重新选择\n"); Sleep(1000); system("cls"); break;
		}
	} while (choose);

	return 0;
}
```
```C
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
//求两个数的最大公约数
int main()
{
	int a = 0;
	int b = 0;
	scanf("%d %d", &a, &b);
	int min = (a < b) ? a : b;
	int m = min;
	while ((a%m != 0 )|| (b % m != 0))
	{
		m--;
	
	}
	printf("%d\n", m);
	return 0;
}
```
### 求十个数中的最大值

```C

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
//求十个数中的最大值
int main()
{
	int arr[] = { 1,2,3,4,5,6,7,8,9,11 };
	int max = arr[0];
	int cd = (sizeof(arr) / sizeof(arr[0])) - 1;
	int i = 0;
	while (i<=cd)
	{
		if (arr[i] >= max)
		{
			max = arr[i];
			i++;
		}
	}
	printf("%d", max);
	return 0;

}
```


```C
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<assert.h>
#include<errno.h>
#include<stdlib.h>

struct Student
{
	char cName[20];
	int iNumber;
	struct Student* pNext;
};

int iCount;
struct Student* Create()
{
	struct Student* pHead = NULL;
	struct Student* pEnd, *pNew;
	iCount = 0;
	pEnd = pNew = (struct Student*)malloc(sizeof(struct Student));
	printf("请输入第一号名字，和号数\n");
	scanf("%s %d", &pNew->cName, &pNew->iNumber);
	while (pNew->iNumber!=0)
	{
		iCount++;
		if (iCount == 1)
		{
			pNew->pNext = pHead;
			pEnd = pNew;
			pHead = pNew;
		}

		else
		{
			pNew->pNext = NULL;
			pEnd->pNext = pNew;
			pEnd = pNew;
		}

		pNew = (struct Student*)malloc(sizeof(struct Student));
		scanf("%s", &pNew->cName);
		scanf("%d", &pNew->iNumber);
	}
	free(pNew);
	return pHead;
}

void Print(struct Student* pHead)
{
	struct Student* pTemp;
	int ilndex = 1;
	printf("有 %d 个成员：\n", iCount);
	pTemp = pHead;
	while(pTemp!=NULL)
	{
		printf("NO%d 成员：\n", ilndex);
		printf("姓名：%s\n", pTemp->cName);
		printf("学号：%d\n", pTemp->iNumber);
		printf("\n");
		pTemp = pTemp->pNext;
		ilndex++;
	}
}

int main()
{
	struct Student* pHead;
	pHead = Create();
	Print(pHead);
	return 0;
}
