#include <stdio.h>
int main()
{
	int a,b = 1,c;
	scanf("%d",&a);
	if(a < 0)
	{
		printf("fu ");
		a = -a;
	}
	if(a == 0)
		printf("ling");
	while(1)
	{
		c = a/b;
		if (c < 10)
			break;
		else
			b *= 10;
	}
	while(b >= 1)
	{
		c = a/b;
		switch(c)
		{
			case 0:printf("shi ");break;
			case 9:printf("jiu ");break;
			case 8:printf("ba ");break;
			case 7:printf("qi ");break;
			case 6:printf("liu ");break;
			case 5:printf("wu ");break;
			case 4:printf("si ");break;
			case 3:printf("san ");break;
			case 2:printf("er ");break;
			case 1:printf("yi ");break;
		}
		a %= b;
		b /= 10;
	}
	return 0;
}