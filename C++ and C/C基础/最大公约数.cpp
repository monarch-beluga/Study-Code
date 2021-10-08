#include <stdio.h>
int divisor(int x,int y)		//定义函数最大公约数
{
	int i;
	// if(x < y)
	// 	i = y,y = x,x = i;
	i = x%y;
	while(i != 0)
		x=y,y = i,i=x%y;
	return y;
}
int main()
{
	int m,n;
	printf("输入两个数：");
	scanf("%d%d",&n,&m);
	printf("最大公约数是：%d",divisor(n,m));
	return 0;
}
