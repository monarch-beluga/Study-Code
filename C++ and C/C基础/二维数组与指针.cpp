#include <stdio.h>
int main()
{
	int a[2][3],i,*p;
	p=&a[0][0];				//ע��ָ���ַ��ֵ��һλ����Ĳ�ͬ
	for(i=0;i<6;i++)
			scanf("%d",p++);
	p=&a[0][0];
	for(i=0;i<6;i++,p++)
			printf("%x *p=%d\n",p,*p);
	return 0; 
}