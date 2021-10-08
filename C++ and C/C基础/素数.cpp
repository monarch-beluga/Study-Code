#include <stdio.h>		//求素数
int main()
{
	int a,b,c;
	for (a=1;a <= 10;a++)
	{
		c = 1;
		for(b=2;b < a;b++)
			if(a%b == 0) 
			{
				c = 0;
				break;
			}
		if (c == 1)
			printf("%d ",a);
	}
	return 0;
}
/*
#include <stdio.h>		//素数求和
int main()
{
	int a,b,c;
	long x,y,n = 0,m = 0;
	scanf("%d%d",&x,&y);
	for (a=2;a <= 200;a++)
	{
		c = 1;
		for(b=2;b < a;b++)
			if(a%b == 0) 
			{
				c = 0;
				break;
			}
		if (c == 1)
		{
			n += 1;
			if(n>=x&&n<=y)
				m += a;
		}
	}
	printf("%ld",m);
	return 0;
}