#include <stdio.h>
int main()
{
	int a;
	printf("请输入分数：");
	scanf("%d",&a);
	a > 90?
		printf("优秀!"):
	a > 80?
		printf("良好"):
	a > 70?
		printf("中等"):
	a > 60?
		printf("及格"):
		printf("不及格");
	return 0;
}