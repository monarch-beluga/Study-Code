#include<stdio.h>
void f(int a[],int n)		//����
{
	static int i ,j ,x;
	for(;i<n;i++)
		for(;j<n-1;j++)
			if(a[j]>a[j+1])
				x=a[j],a[j]=a[j+1],a[j+1]=x;
}
int main()
{
	int a[10]={12,456,24,12,365,15,35,48,15,24},i;
	f(&a[3],5);		//&a[3]��ʾ�ӵ��ĸ�Ԫ�ؿ�ʼ��a����
	for(i=0;i<10;i++)
		printf("%-5d",a[i]);
	printf("\n");
	return 0;
}