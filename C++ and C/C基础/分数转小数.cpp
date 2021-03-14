#include <stdio.h>
int main()
{
	int a,b,n;
	int d = 1;
	printf("输入一个分数：");
	while(1)
	{
		scanf("%d/%d",&a,&b);
		if (a > b)
		{
			n = a/b;
			a = a%b;
		}
		printf("%d.",n);
		for(int c = 1;d <= 200&&c!= 0;a = a*10%b,d++)
		{
			c = a*10/b;
			printf("%d",c);
		}
		printf("\n");
		break;
	}
	return 0;
}