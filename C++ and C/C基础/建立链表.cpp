#include <stdlib.h>			//ͷ�巨��ȱ�㣺�������
#include <stdio.h>
typedef struct data			//����ṹ��
	{
		long i;
		float f;
		struct data *next;//����ľ���
	}A;
void list (A *head)			//�������
{
	A *p = head;
	printf("ѧ��		�ɼ�\n");
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
		p->next = h,h = p;		//ͷ�巨�ľ���
		p = (A *)malloc(sizeof(A));
		scanf("%ld%f",&p->i,&p->f);
	}
	list(h);
	free(p);
	return 0;
}
/*
#include <stdlib.h>			//β�巨
#include <stdio.h>
typedef struct data			//����ṹ��
	{
		long i;
		float f;
		struct data *next;//����ľ���
	}A;
void list (A *head)			//�������
{
	A *p = head;
	printf("ѧ��		�ɼ�\n");
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
		j = p;						//β�巨�ľ���
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