#include<stdio.h>
int main()
{
	int a,b,c,x,y,m,n;
	a = 4,b = 5,c = 7;
	y = (x = a + b);
	printf("%d,%d\n",x,y);
	m = (n = c+b,b+a);
	printf("%d,%d\n",m,n);
	m = (n = a+b,b+c,a + c);//�����ڵ�һ�ֵ��n�����������һ�ֵ��m
	printf("%d,%d\n",m,n);
	m = n = a+b,b+c,15;  //û������ʱ��m��n��ֵ��Ϊ=���һ��
	printf("%d,%d\n",m,n);
	return 0;
}
