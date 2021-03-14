#include<stdio.h>
int *f(int x,int y)			//要返回地址定义函数时要注意定义返回值的类型
{
	if(x>y) return &x;
	return &y;
}
int main()
{
	int i,j,*p;				//*p表示指针变量
	scanf("%d%d",&i,&j);
	p = f(i,j);				
	printf("%d,%d",p,*p);			//运用时p表示变量所存储的地址；*p表示该地址所表示的数
}
/*
#include<stdio.h>
int max(int x,int y)
{
	if(x>y) return x;
	return y;
}
int main()
{
	int i,j,a;
	int	(*p)(int x,int y);		//定义指向函数的指针
	scanf("%d%d",&i,&j);
	p = max;				//将函数名（即函数入口地址）赋值个给指针
	a=(*p)(i,j);			//用指向函数的指针来代替自定义函数
	printf("%d,%d,%d",i,j,a);
}