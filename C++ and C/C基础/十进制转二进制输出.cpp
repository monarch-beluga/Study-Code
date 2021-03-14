#include <stdio.h>
int main()
{
	int a,b,d = 1,x=1;
	long c = 0;
	while (x == 1)
	{
		printf("开始输入1，结束输入0：");
		scanf("%d",&x);
		if(x == 1)
			printf("开始！\n");
		else
			break;
		printf("输入一个整数：");
		scanf("%d",&a);
		for(;a != 0;a /= 2)
		{
			b = a%2;
			c = c+b*d;
			d *= 10;
		}
		printf("%ld\n",c);
	}
	return 0;
}