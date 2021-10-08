#include "stdafx.h"
#include<stdio.h>
int main()
{
	int year,x = 1;
	while (x == 1)
	{
		printf("开始输入1，结束输入0：");
		scanf("%d",&x);
		if(x == 1)
			printf("开始！\n");
		else
			break;
		printf("请输入年份：");
		scanf("%d",&year);
		if((year % 100 == 0 && year % 400 == 0)||year % 4 == 0)
			printf("是闰年");
		else
			printf("不是闰年");	
	}
	return 0;
}
