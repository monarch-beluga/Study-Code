#include <stdlib.h>			//β�巨ɾ�����
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
	printf("ѧ��		�ɼ�\n");
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
	printf("������Ҫɾ���Ľ��λ�ã�");
	scanf("%d",&x);
	if(x == 1)
	{
		h = h->next;			//ɾ����һ�����
		list(h);
	}
	else if (x>1);
	{
		for(i = 0,m = h,n = m->next;i<x-2;i++)		//ɾ������λ�õĽ��
			m = n,n = m->next;
		m->next = n->next;
		list(h);
	}
	else printf("û��ɾ����㣡");
	printf("������Ҫ����Ľ��λ�ã�");
	scanf("%d",&x);
	if(x == 1)
	{
		p = (A *)malloc(sizeof(A));			//�ڿ�ͷ��ӽ��
		scanf("%ld%f",&p->i,&p->f);
		p->next = h;
		h = p;
		list(h);
	}
	else if (x>1);
	{
		for(i = 0,m = h,n = m->next;i<x-2;i++)		//���м������
			m = n,n = m->next;
		p = (A *)malloc(sizeof(A));
		scanf("%ld%f",&p->i,&p->f);
		m->next = p;
		p->next = n;
		list(h);
	}
	else printf("û��ɾ�����㣡");
	return 0;
}