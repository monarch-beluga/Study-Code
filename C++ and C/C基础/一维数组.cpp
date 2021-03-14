#include<stdio.h>
#include <stdafx.h>
int main()
{
	int a,score[5] = {5,4,8,7,8};		//数组的赋值
	//如果数组元素少于数组长度，那么后面的元素为0
	a = score[4];		//数组的引用，下标从0开始
	//一次只能使用一个数组元素，而不能一次引用整个数组
	printf("%d",a);
	return 0;
}
/*
#include<stdio.h>		//输入10个数，然后倒叙输出
int main()
{
	int i,temp[10];
	for(i=0;i<10;i++)
		scanf("%d",&temp[i]);
	for(i=9;i>=0;i--)
		printf("%d ",temp[i]);
	return 0;
}
#include<stdio.h>		//输入10个数，求和、平均值
int main()
{
	int i,temp[10];
	static int sum;
	static float avgerage;
	for(i=0;i<10;i++)
		scanf("%d",&temp[i]);
	for(i=0;i<10;i++)
		sum+=temp[i];
	avgerage = sum/10.0;
	printf("sum=%d,avgerage=%.1f",sum,avgerage);
	return 0;
}
#include<stdio.h>		//求数组内数据的最大值
int main()
{
	int max,i,temp[5];
	for(i=0;i<5;i++)
		scanf("%d",&temp[i]);
	for(i=0,max=0;i<5;i++)
		max=max>temp[i]?max:temp[i];
	printf("%d\n",max);
	return 0;
}*/