#include <stdio.h>
int main()
{
	typedef struct data
	{
		int i;
		char ch;	
	}A,*P;				
	A a;      //�൱��struct data a;
	P p;		//�൱��struct data *p;��A *pЧ��һ��
	a.i = 12;
	p = &a;
	(*p).ch = 'a';
	printf("%c,%d",(*p).ch,a.i);
	return 0;
}