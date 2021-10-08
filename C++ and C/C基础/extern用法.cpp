#include<stdio.h>
int max(int a,int b);
int main()
{
	extern int x,y;				//函数外赋值
	printf("%d\n",max(x,y));
	return 0;
}
int max(int a,int b)		//自定义函数比大小
{
	if(a > b)
		return a;
	else
		return b;
}
int x=13,y = 23;