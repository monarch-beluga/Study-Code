#include <stdio.h>
int main()
{
	int i=2;
	float s=1;
	do				//先执行语句，再判断
	{
		s += 1.0/i;
		i += 2;
	}while(i <= 50);
	printf("%f\n",s);
	return 0;
}
/*#include <stdio.h>		//输出奇数
int main()
{
	int i;
	do
	{
		printf("请输入奇数：");
		scanf("%d",&i);
	}while(i%2 == 0);
	printf("i = %d\n",i);
	return 0;
}
*/