#include <stdio.h>
int main()
{
	union data    //���干ͬ��
	{
		int i;
		char ch;
	}a,*p;
	p = &a;
	(*p).ch = 'a';   //��ͬ�帳ֵ����Ϊ��ͬ�����������ݹ���һ���洢�ռ䣬���й�ͬ���ڵ�ֵΪ���ֵ��ֵ
	a.i = 12;
	printf("%c,%d",(*p).ch,a.i);
	return 0;
}