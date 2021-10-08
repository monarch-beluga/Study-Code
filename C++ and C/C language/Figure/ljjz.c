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

char* f1 = "����ͼ.txt";
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
	system("cls");					// ����
	// ��ӡ����
	printf("\n********��ͨͼ�ڽӱ�洢*********\n");
	printf("*\t1-�����ڽӾ���\t\t*\n");
	printf("*\t2-��ӡ�ڽӾ���\t\t*\n");
	printf("*\t0-�˳�\t\t\t*\n");
	printf("*********************************\n");
	// �˵�ѡ��
	Menu_select();
}

void Menu_select()
{
	int a; 
	printf("��ѡ��<Select>:\n");
	scanf("%d",&a);
	switch(a)
	{
		case 1:
		creat(&g1, f1, 0);
		printf("�ڽӾ��󴴽��ɹ�������\n");
		break;
		case 2:
		printf("�ڽӾ���\n");
		print(g1);
		break;
		case 0:exit(0);
	}
	// ���º����
	system("pause");
	// ִ����һ��ѡ������»ص��˵�����
	Menu();
}

void creat(Mgraph *g,char *filename,int c)
{ 
	int i,j,k;
	FILE *fp;
	fp=fopen(filename,"r");
	if (fp)
	{
		fscanf(fp,"%d%d",&g->n,&g->e);              /*���붥���������*/
		
		for(i=0;i<g->n;i++)
		    fscanf(fp,"%1s",&g->vexs[i]);    /*���붥����Ϣ*/
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
