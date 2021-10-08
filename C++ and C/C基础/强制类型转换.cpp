#include<stdio.h>
int main()
{
	int a;
	a = 10;
	printf("%f\n%f\n",a,(float)a);
	printf("%f\n%f\n",(float)a,a);
	return 0;
}