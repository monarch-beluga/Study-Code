#include<stdio.h>
void in()					//没有返回值时用void
{
	static int x;		//只在最初值时赋值，如果没有明确赋值，则值为0
	x++;
	printf("%d\n",x);
}
int main()
{
	void in();
	in();
	in();
	in();
}