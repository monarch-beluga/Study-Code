#include<stdio.h>			//���Ҹ���
int main()
{
	int a[10]={12,456,24,12,365,15,35,48,15,24};
	static int count,i,x;
	scanf("%d",&x);
	for(;i<10;i++)
		if(a[i]==x) count += 1;
	if(count==0)
		printf("û��Ҫ�ҵ�����");
	else
		printf("��������%d��",count);
	return 0;
} 
/*
#include<stdio.h>			//����λ��
int main()
{
	int a[10]={12,23,34,45,56,67,78,89,91,98};
	static int count,i,x,y=9,t,z;
	scanf("%d",&t);
	for(x=5;i<y;x=(int)(y+i)/2)
	{
		if(a[x]!=t)
			a[x]>t?y=x-1:i=x+1;
		else {z=1;break;}
	}
	if(z) printf("�����е�λ��Ϊ��%d\n",x);
	else printf("û���ҵ���\n");
	return 0;
} 