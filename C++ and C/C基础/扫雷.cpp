#include <stdio.h>
#include<time.h>
#include<stdlib.h>
#define N 16
static int a[N][N],b[N][N];
void Ass()
{
	int i,j;
	for(i=0;i<N;i++)
		for(j=0;j<N;j++)
			b[i][j]=-1;
}
void Ccb(int b[][N])
{
	int i,j;
	printf("  ");
	for(i=1;i<=N;i++)
		printf("%2d",i);
	printf("\n");
	for(i=0;i<N;i++)
	{
		printf("%-2d",i+1);
		for(j=0;j<N;j++)
			printf("%2d",b[i][j]);
		printf("\n");
	}
}
int Lde(int x,int y)		//埋地雷，以a数组为内置棋盘
{
	int i,j,n;
	int sst[8][2]={-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};		//访问地雷旁边的八个格子所用数组
	if(a[x][y]==9) return 0;		//与后面的return 9 一起防止生成两个位置相同的地雷
	a[x][y]=9;				//地雷用9表示
	for(n=0;n<8;n++)
	{
		i=x+sst[n][0];		//访问旁边八个格子
		j=y+sst[n][1];
		if(i<N&&j<N&&i>=0&&j>=0&&a[i][j]<9)a[i][j]++;		//防止越界
	}
	return 9;
}
void display(int x,int y)		//将内置棋盘a按游戏规则赋值给b
{
	int i,j,n;
	int sst[8][2]={-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};
	if(a[x][y]==0&&b[x][y]==-1)
	{
		b[x][y]=a[x][y];
		for(n=0;n<8;n++)
		{
			i=x+sst[n][0];
			j=y+sst[n][1];
			if(i<N&&j<N&&i>=0&&j>=0) display(i,j);		//递归思想
		}
	}
	else b[x][y]=a[x][y];
}
int mark()			//操作方式
{
	int type,x,y;
	printf("输入操作类型：0 标记数字 1 标记地雷 2 取消地雷标记：");
	scanf("%d",&type);
	printf("输入行、列号（1~%d）：",N);
	scanf("%d%d",&x,&y);
	if(type==0)
	{
		if(a[x-1][y-1]==9) return 0;
		else display(x-1,y-1);
	}
	else if(type==1) b[x-1][y-1]=9;
	else  b[x-1][y-1]=-1;
	return 1;
}
int end()			//游戏结束方式
{
	int x,y;
	for(x=0;x<N;x++)
		for(y=0;y<N;y++)
			if(b[x][y]==-1) return 1;			//当显示棋盘b中无-1，时结束
	return 0;
}
int main()
{
	int Number,i,j,n,x,y,err=0;
	srand((unsigned)time( NULL ) );			//初始化随机器
	Number = rand()%(N)+(N-3);			//随机地雷数
	for(n=0;n<Number;n++)				//埋雷，设置内置棋盘a
	{
		x = rand()%(N-1);
		y = rand()%(N-1);
		if(Lde(x,y)==0) n--;				//防止两颗雷同一位置
	}
	Ass();
	Ccb(b);
	do						//游戏的主要操作
	{
		if(!mark())
		{
			puts("你踩到雷了1");
			continue;
		}
		system("cls");
		Ccb(b);
	}while(end());
	for(i=0;i<N;i++)			//判断胜负
		for(j=0;j<N;j++) 
			if(a[i][j]!=b[i][j]) err++;
	if(err==0)puts("你胜利了！");
	else puts("失败！你标多了！");
	return 0;
}