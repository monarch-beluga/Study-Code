#include<stdio.h>
static char a[9];			//建立空数组
void f()		
{
	for(int i=0;i<9;i++)
		a[i]=' ';
}
void Ccb()			//打印棋盘
{
	printf("%c%c%c\n",a[0],a[1],a[2]);
	puts("-+-+-");
	printf("%c%c%c\n",a[3],a[4],a[5]);
	puts("-+-+-");
	printf("%c%c%c\n",a[6],a[7],a[8]);
}
int win(int i)		//判断胜负
{
	int x=0;
	char ch;
	if(i%2==1) ch='#';
	else ch='$';
	if(a[0]==ch&&a[1]==ch&&a[2]==ch)x=1;
	if(a[3]==ch&&a[4]==ch&&a[5]==ch)x=1;
	if(a[8]==ch&&a[7]==ch&&a[6]==ch)x=1;
	if(a[0]==ch&&a[3]==ch&&a[6]==ch)x=1;
	if(a[1]==ch&&a[4]==ch&&a[7]==ch)x=1;
	if(a[2]==ch&&a[5]==ch&&a[8]==ch)x=1;
	if(a[0]==ch&&a[4]==ch&&a[8]==ch)x=1;
	if(a[6]==ch&&a[4]==ch&&a[2]==ch)x=1;
	return x;
}
int main()
{
	int n=0,m;
	puts("规则：先下者为甲执$,后下者为乙执#，横竖斜三为同一者胜！");
	f();
	Ccb();
	do
	{
		do
		{
			printf("请输入1~9棋子的位置：");
			scanf("%d",&m);
		}while(a[m-1]!=' ');
		if(n%2==0)a[m-1]='$';
		else a[m-1]='#';
		Ccb();
		win(n);
		n++;
	}while(n<9&&win(n-1)==0);
	if(win(n-1)==0)puts("平局！");
	else if(n%2==1)puts("甲胜！");
	else puts("乙胜！");
}