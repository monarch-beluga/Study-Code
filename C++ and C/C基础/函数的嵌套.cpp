#include <stdio.h>
int divisor(int x,int y)		//���庯�����Լ��
{
	int i;
	if(x < y)
		i = y,y = x,x = i;
	i = x%y;
	while(i != 0)
		x=y,y = i,i=x%y;
	return y;
}
int mulltiple(int x,int y)		//������С������
{
	int i;
	i = x*y/divisor(x,y);
	return i;
}
int main()
{
	int m,n;
	printf("������������");
	scanf("%d%d",&n,&m);
	printf("���Լ���ǣ�%d",divisor(n,m));
	printf("��С�������ǣ�%d",mulltiple(n,m));
	return 0;
}
