#include<stdio.h>
int max(int a,int b);
int main()
{
	int x,y,z;
	printf("������������:");
	scanf("%d%d",&x,&y);
	z = max(x,y);
	printf("%d\n",z);
	return 0;
}
int max(int a,int b)		//�Զ��庯���ȴ�С
{
	if(a > b)
		return a;
	else
		return b;
}
/*
#include <stdio.h>
long fac(int n)			//�Զ��庯���ڿ�ͷ����ʡ�Ժ�������
{
	long f = 1;
	for(int i =1;i <= n;i++)		//�Զ��庯�����׳�
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
