#include<stdio.h>
int max(int a,int b);
int main()
{
	extern int x,y;				//�����⸳ֵ
	printf("%d\n",max(x,y));
	return 0;
}
int max(int a,int b)		//�Զ��庯���ȴ�С
{
	if(a > b)
		return a;
	else
		return b;
}
int x=13,y = 23;