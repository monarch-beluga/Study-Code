#include<stdio.h>
int *f(int x,int y)			//Ҫ���ص�ַ���庯��ʱҪע�ⶨ�巵��ֵ������
{
	if(x>y) return &x;
	return &y;
}
int main()
{
	int i,j,*p;				//*p��ʾָ�����
	scanf("%d%d",&i,&j);
	p = f(i,j);				
	printf("%d,%d",p,*p);			//����ʱp��ʾ�������洢�ĵ�ַ��*p��ʾ�õ�ַ����ʾ����
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
	int	(*p)(int x,int y);		//����ָ������ָ��
	scanf("%d%d",&i,&j);
	p = max;				//������������������ڵ�ַ����ֵ����ָ��
	a=(*p)(i,j);			//��ָ������ָ���������Զ��庯��
	printf("%d,%d,%d",i,j,a);
}