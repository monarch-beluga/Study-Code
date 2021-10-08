#include"ljb.h"

int visited[M];
LinkedGraph g1;
char* f1 = "����ͼ.txt";

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
	system("cls");					// ����
	// ��ӡ����
	printf("\n********��ͨͼ�ڽӱ�洢*********\n");
	printf("*\t1-�����ڽӱ�\t\t*\n");
	printf("*\t2-��ӡ�ڽӱ�ṹ\t*\n");
	printf("*\t3-�������\t\t*\n");
	printf("*\t4-�������\t\t*\n");
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
		printf("�ڽӱ����ɹ�������\n");
		break;
		case 2:
		printf("�ڽӱ�ṹ��\n");
		print(g1);
		break;
		case 3:
		printf("������ȱ�����\n");
		DfsTraverse(g1);
		break;
		case 4:
		printf("������ȱ�����\n");
		BfsTraverse(g1);
		break;
		case 0:exit(0);
	}
	// ���º����
	system("pause");
	// ִ����һ��ѡ������»ص��˵�����
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
	printf("\n����ͨͼ����%d����ͨ����\n", count);
}
