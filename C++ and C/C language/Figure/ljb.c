#include"ljb.h"

int visited[M];
LinkedGraph g1;
char* f1 = "无向图.txt";

void dfs(LinkedGraph g, int i);
void DfsTraverse(LinkedGraph g);
void bfs(LinkedGraph g, int i);
void BfsTraverse(LinkedGraph g);
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
	printf("*\t1-创建邻接表\t\t*\n");
	printf("*\t2-打印邻接表结构\t*\n");
	printf("*\t3-深度优先\t\t*\n");
	printf("*\t4-广度优先\t\t*\n");
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
		printf("邻接表创建成功！！！\n");
		break;
		case 2:
		printf("邻接表结构：\n");
		print(g1);
		break;
		case 3:
		printf("深度优先遍历：\n");
		DfsTraverse(g1);
		break;
		case 4:
		printf("广度优先遍历：\n");
		BfsTraverse(g1);
		break;
		case 0:exit(0);
	}
	// 按下后继续
	system("pause");
	// 执行完一次选择后重新回到菜单界面
	Menu();
}

void dfs(LinkedGraph g, int i)
{
	EdgeNode *p;
	printf("visit vertex: %c\n", g.adjlist[i].vertex);
	visited[i] = 1;
	p = g.adjlist[i].FirstEdge;
	while (p)
	{
		if (!visited[p->adjvex])
			dfs(g, p->adjvex);
		p = p->next;
	}
}

void DfsTraverse(LinkedGraph g)
{
	int i;
	for(i=0; i<g.n; i++)
		visited[i] = 0;
	for (i = 0; i < g.n; ++i)
		if (!visited[i])
			dfs(g, i);
}

void bfs(LinkedGraph g, int i)
{
	int j;
	EdgeNode *p;
	int queue[M], front, rear;
	front = 0, rear = 0;
	printf("%c ", g.adjlist[i].vertex);
	visited[i] = 1;
	queue[rear++] = i;
	while(rear > front)
	{
		j = queue[front++];
		p = g.adjlist[j].FirstEdge;
		while(p)
		{
			if (visited[p->adjvex] == 0)
			{
				printf("--> %c", g.adjlist[p->adjvex].vertex);
				queue[rear++] = p->adjvex;
				visited[p->adjvex] = 1;
			}
			p = p->next;
		}
	}
}
void BfsTraverse(LinkedGraph g)
{
	int i, count = 0;
	for(i=0; i<g.n; i++)
		visited[i] = 0;
	for (i = 0; i < g.n; ++i)
	{
		if (!visited[i])
		{
			printf("\n");
			count++;
			bfs(g, i);
		}
	}
	printf("\n该连通图共有%d个连通分量\n", count);
}
