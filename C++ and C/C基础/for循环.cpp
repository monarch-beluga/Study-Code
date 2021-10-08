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
	for(;;b *= 10)
	{
		c = a/b;
		if (c < 10) break;
	}
	for(;b >= 1;a %= b,b /= 10)
	{
		c = a/b;
		switch(c)
		{
			case 0:printf("ling ");break;
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
	}
	return 0;
}
/*#include <stdio.h>		//回文数(有缺陷)
int main()
{
	int a,c,b;
	scanf("%d",&a);
	for(c = 0;a>0;a /= 10)
		c = c*10+a%10;
	printf("%d",c);
	return 0;
}
*/