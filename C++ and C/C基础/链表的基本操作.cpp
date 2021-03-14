#include <stdlib.h>			//尾插法删除结点
#include <stdio.h>
typedef struct data	
	{
		long i;
		float f;
		struct data *next;
	}A;
void list (A *head)	
{
	A *p = head;
	printf("学号		成绩\n");
	while(p)
	{
		printf("%-9ld	%-.2f\n",(*p).i,p->f);
		p = (*p).next;
	}
}
int main()
{
	int i,x;
	A *h,*j,*m,*n;
	A *p = (A *)malloc(sizeof(A));
	h = p;
	scanf("%ld%f",&p->i,&p->f);
	while(p->i != 0)
	{
		j = p;
		p = (A *)malloc(sizeof(A));
		scanf("%ld%f",&p->i,&p->f);
		if(p->i == 0)j->next = NULL;
		else j->next = p;
	}
	list(h);
	printf("请输入要删除的结点位置：");
	scanf("%d",&x);
	if(x == 1)
	{
		h = h->next;			//删除第一个结点
		list(h);
	}
	else if (x>1);
	{
		for(i = 0,m = h,n = m->next;i<x-2;i++)		//删除其他位置的结点
			m = n,n = m->next;
		m->next = n->next;
		list(h);
	}
	else printf("没有删除结点！");
	printf("请输入要插入的结点位置：");
	scanf("%d",&x);
	if(x == 1)
	{
		p = (A *)malloc(sizeof(A));			//在开头添加结点
		scanf("%ld%f",&p->i,&p->f);
		p->next = h;
		h = p;
		list(h);
	}
	else if (x>1);
	{
		for(i = 0,m = h,n = m->next;i<x-2;i++)		//在中间插入结点
			m = n,n = m->next;
		p = (A *)malloc(sizeof(A));
		scanf("%ld%f",&p->i,&p->f);
		m->next = p;
		p->next = n;
		list(h);
	}
	else printf("没有删插入结点！");
	return 0;
}