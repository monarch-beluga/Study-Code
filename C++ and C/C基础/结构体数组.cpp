#include<stdio.h>		//统计后输出参赛者成绩
#include<string.h>
struct person			//初始化结构体
{
	char name[20];
	int count;
};
int main()
{
	struct person leader[3] = {{"li",0},{"liu",0},{"wan",0}},*p;		//定义结构体数组
	char a[20];														//定义指针
	int j;
	for (int i=0;i<3;i++)				//打分及统计
	{
		printf("请输入“li”、“liu”或者“wan”：");
		scanf("%s",a);
		for(j=0;j<3;j++)
			if (strcmp(a,leader[j].name )== 0) leader[j].count++;
	}		//字符串比较函数：strcmp，需要有头文件string.h
	p  = leader;			//指针代替结构体数组
	for(int i = 0;i<3;i++)			//输出
		printf("%s	%d\n",p[i].name,p[i].count);
	return 0;
}
/*
#include<stdio.h>			//统计后输出最高者成绩
#include<string.h>
struct person
{
	char name[20];
	int count;
};
int max(int a,int b,int c)
{
	if(a<b) a = b;
	if(a>c) return a;
	else return c;
}
int main()
{
	struct person leader[3] = {{"li",0},{"liu",0},{"wan",0}};
	char a[20];
	int j;
	for (int i=0;i<3;i++)
	{
		printf("请输入“li”、“liu”或者“wan”：");
		scanf("%s",a);
		for(j=0;j<3;j++)
			if (strcmp(a,leader[j].name )== 0) leader[j].count++;
	}
	for(int i = 0;i<3;i++)
	{
		if(leader[i].count == max(leader[0].count,leader[1].count,leader[2].count))
		printf("%s	%d\n",leader[i].name,leader[i].count);
	}
	return 0;
}
*/