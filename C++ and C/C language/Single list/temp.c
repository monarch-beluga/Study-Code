#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include<windows.h>
typedef struct
{	char num[5];   //编号 
	char name[9];  //姓名 
	char sex[3];   //性别 
	char phone[13]; //电话 
	char addr[31];  //地址 
}ElemType;
typedef struct node
{	//节点类型定义
	ElemType data;     //数据域 
	struct node* next; //指针域
}LNode,*LinkList;
LinkList pHead;   LNode *p;
//函数声明
int menu_select();
LinkList CreateList(void); 
void InsertNode(LinkList head, LNode* p);
LNode* ListFind(LinkList head);
void DeleteNode(LinkList head);
void PrintList(LinkList head);
//主函数
int main()
{
	while(1)
	{
		switch(menu_select())
		{
			case 1:
			printf("*******************************\n");
			printf("**   病患信息表的建立（Tab键分隔）   **\n）");
			printf("*******************************\n");
			pHead = CreateList();
			break;
			case 2:
			printf("*******************************\n");
			printf("**   病患信息添加  **\n）");
			printf("*******************************\n");
			printf("*编号（4） 姓名（8） 性别 电话（11） 地址（31） *\n");
			printf("*******************************\n");
			p=(LNode*)malloc(sizeof(LNode));
			scanf("%s%s%s%s%s",p->data.num,p->data.name,
                   p->data.sex,p->data.phone,p->data.addr);
            InsertNode(pHead,p);
			break;
			case 3:
			printf("*******************************\n");
			printf("**   病患信息查询  **\n）");
			printf("*******************************\n");
			p=ListFind(pHead);
			if(p!=NULL)
			{
			   printf("*编号（4） 姓名（8） 性别 电话（11） 地址（31） *\n");
			   printf("--------------------------------\n");
			   printf("%s\t%s\t%s\t%s\t%s\n",p->data.num,p->data.name,
                   p->data.sex,p->data.phone,p->data.addr);
               printf("*******************************\n");
			}
			else
               printf("没有查到要查询的病人!\n");
            break;
            case 4:
            printf("*******************************\n");
			printf("**   病患信息删除  **\n）");
			printf("*******************************\n");
			DeleteNode(pHead); // 删除节点
			break;
			case 5:
            printf("*******************************\n");
			printf("**   病患信息链表的输出  **\n）");
			printf("*******************************\n");
			PrintList(pHead); 
			break;
			case 0:
		    printf("\t 再见!\n");
			return 0; 
		}
		system("pause");
	}
	return 0;
} 
int menu_select() 
{
	int sn;
	system("cls");
	printf("=================================\n");
	printf("   病患信息管理系统\n");
	printf("=================================\n");
	printf("   1. 病患信息表的建立\n");
	printf("   2. 病患节点的插入\n");
	printf("   3. 病患节点的查询\n");
	printf("   4. 病患节点的删除\n");
	printf("   5. 病患信息表的输出\n");
	printf("   0. 退出管理系统\n");
	printf("=================================\n");
	for(;;)
	{
		scanf("%d",&sn);
		if(sn<0||sn>5)
		   printf("\n\t 输入错误，重选 0-5");
        else
           break;
	}
	return sn;
}
LinkList CreateList(void)  //尾插法建立带头节点的病患信息表 
{
	LNode* head;
	head = (LNode*)malloc(sizeof(LNode));
	head->next = NULL;
	printf("患者信息表建立成功！！！\n");
	return head;
}
void InsertNode(LinkList head, LNode* p) //在head指向的链表中插入节点 
{
	int i,k;
	LNode* q;
	q = head;
	k = 0;
	printf("请输入你要插入的位置：\n");
	scanf("%d",&i);
	while(q!=NULL&&i!=k)
	{
		q = q->next;
		k++;
	}
	if(q == NULL)
	{
		printf("插入失败！\n");
	}
	p->next = q->next;
	q->next = p;
}	
LNode* ListFind(LinkList head) //查找 
{
    ElemType N;
	p = head;
	printf("请输入要查询患者编号：\n");
	scanf("%s",N.num);
	while((p->next!=NULL)&&strcmp(N.num,p->data.num))
	{
		p = p->next;
	}
	return p;
}
void DeleteNode(LinkList head)
{
	LNode* p,* q;
	ElemType M;
	if(head->next == NULL)
	{
		printf("删除失败！\n");
	}
	p = head;
	q = head->next;
	printf("请输入要删除患者的编号：\n");
	scanf("%s",M.num);
	while((q->next!=NULL)&&strcmp(M.num,q->data.num))
	{
		p = q;
		q = q->next;
	}
	if(q == NULL)
	{
		printf("没有该患者！删除失败！");
	}
	if(q)
	{
		p->next = q->next;
		free(q);
	}
}	

void PrintList(LinkList head)
{
   p = head->next;
   if(!p)
       printf("单链表为空!");
   else
   {
   	printf("各节点的值为：\n");
   	while(p)
   	   {
   	   	printf("患者编号为：");
  	    printf("%s",p->data.num);
  	    printf("\n");
  	    printf("患者姓名为：");
  	    printf("%s",p->data.name);
  	    printf("\n");
  	    printf("患者性别为：");
  	    printf("%s",p->data.sex);
  	    printf("\n");
  	    printf("患者电话为：");
  	    printf("%s",p->data.phone);
  	    printf("\n");
  	    printf("患者地址为：");
  	    printf("%s",p->data.addr);
  	    printf("\n");
  	    p = p->next;
  	    printf("\n");
	   }
   }
}
