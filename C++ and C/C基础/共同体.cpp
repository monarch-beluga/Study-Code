#include <stdio.h>
int main()
{
	union data    //定义共同体
	{
		int i;
		char ch;
	}a,*p;
	p = &a;
	(*p).ch = 'a';   //共同体赋值，因为共同体内所有数据共用一个存储空间，所有共同体内的值为最后赋值的值
	a.i = 12;
	printf("%c,%d",(*p).ch,a.i);
	return 0;
}