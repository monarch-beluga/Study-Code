#include <stdio.h>
long fac(int x)
{
	long y;
	if(x==0||x==1)y = 1;
	else y = fac(x-1)*x;		//�ݹ����
	return y;
}
int main()
{
	printf("%ld\n",fac(3));
	return 0;
}
/*
#include<stdio.h>			//���в��ҵĵݹ����
#define N 10
int f(int a[],int x,int i)
{
	static int m,n=N;
	x=(int)(m+n)/2;
	if(a[x]==i) return x;
	if(m>n) return -1;
	if(a[x]>i){
		n=x-1;
		return f(a,x,i);
	}
	if(a[x]<i){
		m=x+1;
		return f(a,x,i);
	}
}
int main()
{
	int a[N]={12,23,34,45,56,67,78,89,91,98};
	static int i,x,j;
	scanf("%d",&i);
	j = f(a,x,i);
	if(j!=-1)
		printf("����λ��Ϊ��%d",j);
	else printf("������û���ҵ��������");
}