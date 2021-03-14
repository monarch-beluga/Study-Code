#include <stdio.h>
int main()
{
	int a;
	printf("请输入分数：");
	scanf("%d",&a);
	if(a > 90)
		printf("优秀!");
	else if(80 <= a)		//不可以用80 <= a <= 90
		printf("良好");
	else if(a  >= 70)
	{
		printf("中等");		//多条语句需要{}
		printf("d");
	}
	else if(a  >= 60)
		printf("及格");
	else
		printf("不及格");
	return 0;
}