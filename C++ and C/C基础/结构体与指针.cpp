#include<stdio.h>
#include<string.h>
int main()
{
	struct a
	{
		int b;
		int c;
	}m = {12,45},*p;
	p  = &m;				//ָ��ṹ�������ָ�븳ֵ��ʽ
	printf("%d\n",(*p).b);		//ʹ�÷���
	return 0;
}