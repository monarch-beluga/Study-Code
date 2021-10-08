#include<stdio.h>
#include<stdlib.h>
#define FINITY 5000
#define M 20
typedef struct
{
	char vexs[M];
	int edges[M][M];
	int n, e;
} Mgraph;

char* f1 = "无向图.txt";
Mgraph g1;

void creat(Mgraph *g,char *filename,int c);
void print(Mgraph g);
void Menu();
void Menu_select();

int main()
{
	Menu();
	return 0;
}

void Menu()
{
	system("cls");					// 清屏
	// 打印界面
	printf("\n********连通图邻接表存储*********\n");
	printf("*\t1-创建邻接矩阵\t\t*\n");
	printf("*\t2-打印邻接矩阵\t\t*\n");
	printf("*\t0-退出\t\t\t*\n");
	printf("*********************************\n");
	// 菜单选择
	Menu_select();
}

void Menu_select()
{
	int a; 
	printf("请选择<Select>:\n");
	scanf("%d",&a);
	switch(a)
	{
		case 1:
		creat(&g1, f1, 0);
		printf("邻接矩阵创建成功！！！\n");
		break;
		case 2:
		printf("邻接矩阵：\n");
		print(g1);
		break;
		case 0:exit(0);
	}
	// 按下后继续
	system("pause");
	// 执行完一次选择后重新回到菜单界面
	Menu();
}

void creat(Mgraph *g,char *filename,int c)
{ 
	int i,j,k;
	FILE *fp;
	fp=fopen(filename,"r");
	if (fp)
	{
		fscanf(fp,"%d%d",&g->n,&g->e);              /*读入顶点数与边数*/
		
		for(i=0;i<g->n;i++)
		    fscanf(fp,"%1s",&g->vexs[i]);    /*读入顶点信息*/
		for (i = 0; i < g->n; ++i)
			for (j = 0; j < g->n; ++j)
				g->edges[i][j] = 0;
		for (k = 0; k < g->e; k++)
		{
			fscanf(fp,"%d%d",&i,&j);
			g->edges[i][j] = 1;
			if (c==0)
				g->edges[j][i] = 1;
		}
		fclose(fp);
	}
	else
		g->n=0;
}

void print(Mgraph g)
{
	int i, j;
	for (i = 0; i < g.n; ++i)
	{
		printf("%c: ", g.vexs[i]);
		for (j = 0; j < g.n; ++j)
			printf("%d\t", g.edges[i][j]);
		printf("\n");
	}
}
