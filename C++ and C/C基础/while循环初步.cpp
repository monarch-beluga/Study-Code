#include <stdio.h>	//1~100的和
int main()
{
	int i = 1,sum = 0;
	while(i <= 100)
	{
		sum += i;
		i++;
	}
	printf("%d\n",sum);
	return 0;
}

/*#include <stdio.h>		//阶乘
int main()
{
	int i = 1,s = 1,y;
	while (x == 1)
	{
		printf("输入想求的阶乘:");
		scanf("%d",&y);
		while(i <= y)
		{
			s *= i;
			i++;
		}
		printf("%d\n",s);
	}
	return 0;
}

#include <stdio.h>		//回文数(有缺陷)
int main()
{
	int n;
	scanf("%d",&n);
	while(n > 0)
	{
		printf("%d",n%10);
		n /= 10;
	}
	return 0;
}