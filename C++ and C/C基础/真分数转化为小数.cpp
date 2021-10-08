#include <stdio.h>
int main()
{
	int a,b;
	int d = 1;
	printf("输入一个真分数：");
	while(1)
	{
		scanf("%d/%d",&a,&b);
		if (a > b)
		{
			printf("格式错误，重新输入：");
			continue;
		}
		printf("0.");
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