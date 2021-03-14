#include <stdio.h>
int main()
{
	int n = 1;
	float a,b,x = 0;
	for(a = 2.0,b = 1.0;n <= 20;n++)
	{
		x += a/b;
		a = a+b;
		b = a-b;
	}
	printf("%.2f",x);
	return 0;
}