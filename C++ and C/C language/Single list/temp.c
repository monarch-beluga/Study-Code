#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node
{	//节点类型定义
	int data;     //数据域 
	struct node* next; //指针域
}LNode,*LinkList;
LinkList pHead;   
LNode *p;
//函数声明
LinkList CreateList()
{
	pHead = (LinkList)malloc(sizeof(LNode));
	pHead->next = NULL;
	return pHead;
}
void InsertNode(LinkList head, LNode* p)
{
	LNode* p1 = head;
	while(p1->next != NULL)
		p1 = p1->next;
	p1->next = p;
	p->next = NULL;
}
void PrintList(LinkList head)
{
	LNode* p1 = head->next;
	while(p1 != NULL)
	{
		printf("%d->", p1->data);
		p1 = p1->next;
	}
	printf("\n");
}
void iteration(LinkList head)
{
	LNode* next;
	LNode* prev = NULL;
	LNode* curr = head->next;
	while (curr != NULL){
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    head->next = prev;
}
int main()
{
	pHead = CreateList();
	for (int i = 0; i < 6; ++i)
	{
		p = (LNode*)malloc(sizeof(LNode));
		p->data = i;
		InsertNode(pHead, p);
	}
	PrintList(pHead);
	iteration(pHead);
	PrintList(pHead);
	return 0;
}
