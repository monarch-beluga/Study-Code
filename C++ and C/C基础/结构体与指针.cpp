#include<stdio.h>
#include<string.h>
int main()
{
	struct a
	{
		int b;
		int c;
	}m = {12,45},*p;
	p  = &m;				//指向结构体变量的指针赋值方式
	printf("%d\n",(*p).b);		//使用方法
	return 0;
}