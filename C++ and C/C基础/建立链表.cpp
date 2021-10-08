#include <stdlib.h>			//头插法，缺点：倒序输出
#include <stdio.h>
typedef struct data			//定义结构体
	{
		long i;
		float f;
		struct data *next;//链表的精髓
	}A;
void list (A *head)			//输出链表
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
	A *h = NULL;
	A *p = (A *)malloc(sizeof(A));
	scanf("%ld%f",&p->i,&p->f);
	while(p->i != 0)
	{
		p->next = h,h = p;		//头插法的精髓
		p = (A *)malloc(sizeof(A));
		scanf("%ld%f",&p->i,&p->f);
	}
	list(h);
	free(p);
	return 0;
}
/*
#include <stdlib.h>			//尾插法
#include <stdio.h>
typedef struct data			//定义结构体
	{
		long i;
		float f;
		struct data *next;//链表的精髓
	}A;
void list (A *head)			//输出链表
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
	A *h,*j;
	A *p = (A *)malloc(sizeof(A));
	h = p;
	scanf("%ld%f",&p->i,&p->f);
	while(p->i != 0)
	{
		j = p;						//尾插法的精髓
		p = (A *)malloc(sizeof(A));
		scanf("%ld%f",&p->i,&p->f);
		if(p->i == 0)j->next = NULL;
		else j->next = p;
	}
	list(h);
	free(p);
	return 0;
}
*/