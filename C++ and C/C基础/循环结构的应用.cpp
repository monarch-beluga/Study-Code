#include <stdio.h>	//100以内3的倍数且个位是6
int main()
{
	int a;
	for (a=1;a <= 100;a++)
		if(a%3 == 0 && a%10 == 6)
			printf("%d ",a);
	return 0;
}
/*#include <stdio.h>	//九九乘法口诀
int main()
{
	int a,b;
	for (a=1;a <= 9;a++)
	{
		for(b=1;b <= 9;b++)
			printf("%-2d×%-2d=%-2d ",b,a,a*b);
		printf("\n");
	}
	return 0;
}