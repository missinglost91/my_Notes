```cpp
#include<iostream>
#include<string>

using namespace std;

int main(void)
{
	
	int scores[3][3]=
	{
		{100,100,100},
		{90,50,100},
		{60,70,80}
	};

	string names[3] = { "张三","李四","王五" };

	for (int i = 0; i < 3; i++)
	{
		int sum = 0;
		for (int j = 0; j < 3; j++)
		{
			sum = sum + scores[i][j];

		}
		cout << names[i]<< "的总分为：" << sum << endl;

	}

}
```


```C

#include<iostream>

using namespace std;

void swap(int* x, int* y)
{
	int lin = *x;
	*x = *y;
	*y = lin;
}



int main()
{
	cout << "请输入两个数字" << endl;
	int a, b;
	cin >> a;
	cin >> b;
	swap(&a,&b);

	cout << a <<" "<< b << endl;
}


```

```Cpp

#include<iostream>

using namespace std;

void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}


void bubble_sort(int * p)
{
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10 - i - 1; j++)
		{
			if (*(p + j) > *(p + j + 1))
			{
				swap(*(p + j), *(p + j + 1));
			}

		}
	}

}


int main()
{
	int arr[10] = { 1,2,3,4,5,6,3,4,3,3, };
	bubble_sort(arr);
}
```
```C
#include<iostream>
#include<string>
using namespace std;

struct hero
{
	string name;
	int age;
	string sex;
};


void bubble_sort_by_age(struct hero par_member[], int par_len)

{
	for (int i = 0; i < par_len; i++)
	{
		for (int j = 0; j < par_len-1; j++)
		{
			if (par_member[j].age > par_member[j + 1].age)
			{
			    
				struct hero temp = par_member[j];
				par_member[j ] = par_member[j + 1];
				par_member[j + 1] = temp;
			}
		}
	}
}


void print_hero(struct hero par_member[],int par_len)
{
	for (int i = 0; i < par_len; i++)
	{
		cout << par_member[i].name << par_member[i].age << par_member[i].sex << endl;
	}
	cout << endl;
}

int main()
{
	struct hero member[5] =
	{
	{"刘备",23,"男"},
	{"关羽",22,"男"},
	{"张飞",20,"男"},
	{"赵云",21,"男"},
	{"貂蝉",19,"女"}
	};
	int len = sizeof(member) / sizeof(member[0]);
	print_hero(member, len);
	bubble_sort_by_age(member, len);
	print_hero(member, len);

}


```