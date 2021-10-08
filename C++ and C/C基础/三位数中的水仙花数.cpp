#include <stdio.h>
int main()
{
	int a,b,c,d;
	for(a = 100;a<1000;a++)
	{
		for(b = a,c = 0;b>0;b /= 10,c = c+d*d*d)
			d = b%10;
		if(a == c) printf("%d\t",a);
	}
	return 0;
}