#include<stdio.h>
int main()
{
	int a,b,c,x,y,m,n;
	a = 4,b = 5,c = 7;
	y = (x = a + b);
	printf("%d,%d\n",x,y);
	m = (n = c+b,b+a);
	printf("%d,%d\n",m,n);
	m = (n = a+b,b+c,a + c);//括号内第一项赋值给n，括号内最后一项赋值给m
	printf("%d,%d\n",m,n);
	m = n = a+b,b+c,15;  //没有括号时，m、n的值都为=后第一项
	printf("%d,%d\n",m,n);
	return 0;
}
