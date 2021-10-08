#include<stdio.h>
int max(int a,int b);
int main()
{
	int x,y,z;
	printf("输入两个整数:");
	scanf("%d%d",&x,&y);
	z = max(x,y);
	printf("%d\n",z);
	return 0;
}
int max(int a,int b)		//自定义函数比大小
{
	if(a > b)
		return a;
	else
		return b;
}
/*
#include <stdio.h>
long fac(int n)			//自定义函数在开头可以省略函数声明
{
	long f = 1;
	for(int i =1;i <= n;i++)		//自定义函数，阶乘
		f *= i;
	return f;
}
int main()
{
	long a;
	a = fac(3)+fac(5)+fac(8);
	printf("%ld\n",a);
	return 0;
}
