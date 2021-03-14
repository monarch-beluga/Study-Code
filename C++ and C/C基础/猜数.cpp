#include <stdio.h>
#include<time.h>
#include<stdlib.h>
#include "set1.h"
void face()
{
	set1(45,4);
	printf("1、计算机猜数");
	set1(45,6);
	printf("2、用户猜数");
	set1(45,8);
	printf("3、退出游戏");
}
void game1()
{
	int n,t,min =0,max,a;
	char s[100];
	srand((unsigned)time( NULL ) );
	while(1)
	{
		system("cls");
		frame();
		set1(35,7);
		printf("请输入要计算机猜的数：");
		scanf("%d",&n);
		t = rand();
		while(1)
		{
			if(t == n)
			{
				set1(50,8);
				puts("正确!");
				Sleep(2000);
				break;
			}
			else 
			{
				set1(50,8);
				gets(s);
			}
			if(strcmp(s,"高")==0)
				max = t-min,t = rand()%max+min;
			else if(strcmp(s,"低") == 0)
				max -= t- min,min = t+1,t = rand()%max+min;
			system("cls");
			frame();
			set1(50,7);
			printf("%d",t);
		}
		system("cls");
		frame();
		set1(47,6);
		printf("1、退出");
		set1(47,8);
		printf("2、重新开始");
		set1(35,10);
		printf("输入序号以选择类型：");
		scanf("%d",&a);
		if(a == 1) break;
	}
}
void game2()
{
	int a,t,s[5][3];
	srand((unsigned)time( NULL ) );
	char s1[] = "随机数   猜测次数   是否猜中\n";
	FILE *fp;
	fp = fopen("E:\\study\\a.txt","a");
	fputs(s1,fp);
	while(1)
	{
		for(int i = 0;i<5;i++)
		{
			s[i][2] = 0;
			s[i][0] = rand()%100+1;

			for(s[i][1] = 5;s[i][1]>0;s[i][1]--)
			{
				system("cls");
				frame();
				set1(44,2);
				printf("该数的范围为1~100");
				set1(40,4);
				printf("猜第%d个数，你还有%d次机会！",i+1,s[i][1]);
				set1(35,6);
				printf("请输入你猜的数：");
				scanf("%d",&t);
				if(t == s[i][0])
				{
					set1(50,8);
					printf("猜中了！");
					s[i][2] = 1;
					Sleep(1000);
					break;
				}
				else if(t<s[i][0])
				{
					set1(50,8);
					printf("低了！");
				}
				else
				{
					set1(50,8);
					printf("高了");
				}
				Sleep(1000);
			}
			s[i][1] = 5-s[i][1];
			set1(50,12);
			if(i<4)
				printf("接下来猜第%d个数",i+2);
			else printf("游戏结束，正在结算...");
			Sleep(2000);
		}
		for(int i = 0,j;i<5;i++)
		{
			for(int j = 0;j<3;j++)
			{
				putw(s[i][j],fp);
				fputs("        ",fp);
			}
			fputc('\n',fp);
		}
		system("cls");
		frame();
		set1(35,3);
		printf("%s",s1);
		for(int i = 0;i<5;i++)
		{
			set1(35,i+4);
			printf("%-6d   %-8d   %-8d",s[i][0],s[i][1],s[i][2]);
		}
		set1(32,9);
		printf("1、退出");
		set1(60,9);
		printf("2、重新开始");
		set1(35,10);
		printf("输入序号以选择类型：");
		scanf("%d",&a);
		if(a == 1) break;
	}
	fclose(fp);
}
int main()
{
	int a;
	while(1)
	{
		system("cls");
		frame();
		face();
		set1(35,10);
		printf("输入序号以选择类型：");
		scanf("%d",&a);
		if(a == 1) game1();
		else if(a == 2) game2();
		else break;
	}
	return 0;
}