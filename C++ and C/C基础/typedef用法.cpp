#include <stdio.h>
int main()
{
	typedef struct data
	{
		int i;
		char ch;	
	}A,*P;				
	A a;      //相当于struct data a;
	P p;		//相当于struct data *p;用A *p效果一样
	a.i = 12;
	p = &a;
	(*p).ch = 'a';
	printf("%c,%d",(*p).ch,a.i);
	return 0;
}