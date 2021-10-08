/*单链表实现病患信息管理问题*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include<setjmp.h>
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
LinkList pHead;
LNode *p;
jmp_buf mark;
int save = 0;
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
	FILE* f;
	for(;;)
	{
		switch(menu_select())
		{
			case 1:
			printf("*******************************\n");
			printf("* 病患信息表的建立(Tab键分隔)*\n");
			printf("*******************************\n");
			pHead = CreateList();
			break;
			case 2:
			printf("*********************************************\n");
			printf("**\t\t 病患信息添加  \t\t   **\n");
			printf("*********************************************\n");
			printf("*编号（4） 姓名（8） 性别 电话（11） 地址（31）*\n");
			printf("*********************************************\n");
			p=(LNode*)malloc(sizeof(LNode));
			scanf("%s%s%s%s%s",p->data.num,p->data.name,
                   p->data.sex,p->data.phone,p->data.addr);
            InsertNode(pHead,p);
			save++;
			break;
			case 3:
			printf("*******************************\n");
			printf("**   病患信息查询  **\n");
			printf("*******************************\n");
			p=ListFind(pHead);
			if(p!=NULL)
			{
				printf("*编号（4） 姓名（8） 性别 电话（11） 地址（31） *\n");
				printf("---------------------------------------------\n");
				printf("%s\t%s\t%s\t%s\t%s\n",p->data.num,p->data.name,
						p->data.sex,p->data.phone,p->data.addr);
				printf("*********************************************\n");
			}
			else
               printf("没有查到要查询的病人!\n");
            break;
            case 4:
            printf("*******************************\n");
			printf("**   病患信息删除  **\n");
			printf("*******************************\n");
			DeleteNode(pHead); // 删除节点
			save++;
			break;
			case 5:
            printf("*********************************************\n");
			printf("**\t   病患信息链表的输出  \t**\n");
			printf("*********************************************\n");
			PrintList(pHead); 
			break;
			case 0:
			if(save)
			{
				f = fopen("Patients.txt","w");			// 输出
				p = pHead->next;
				while(p)
				{
					fprintf(f, "%s\t%s\t%s\t%s\t%s\n",p->data.num,p->data.name,
			                   p->data.sex,p->data.phone,p->data.addr);
					p = p->next;
				}
				fclose(f);
			}
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
		sn = setjmp(mark);
		if (!scanf("%d",&sn))
			longjmp(mark, -1);
		if(sn<0||sn>5)
			printf("\n\t 输入错误，重选 0-5");
	    else
	    	break;
	}
	system("cls");
	return sn;
}
LinkList CreateList(void)  //尾插法建立带头节点的病患信息表 
{
	LNode* p;
	FILE *f;
	pHead = (LinkList)malloc(sizeof(LNode));
	pHead->next = NULL;
	f = fopen("Patients.txt","r");
	if (f)					// 判断文件是否存在
	{
		while(1)				// 循环读取信息
		{
			// 文件读取
			p = (LNode*)malloc(sizeof(LNode));
			fscanf(f, "%s\t%s\t%s\t%s\t%s", p->data.num, p->data.name,
					p->data.sex, p->data.phone, p->data.addr);
			if (!feof(f))			// 判断文件读取是否结束
				InsertNode(pHead,p);
			else
				break;
		}
	}
	fclose(f);
	printf("患者信息表建立成功！！！\n");
	return pHead;
}
void InsertNode(LinkList head, LNode* p) //在head指向的链表中插入节点 
{
	LNode* p1;
	int flag;
	p1 = head;
	while(p1)
	{
		if (p1->next == NULL)			// 尾部插入
		{
			p->next = p1->next;
			p1->next = p;
			printf("节点插入成功！！！\n");
			break;
		}
		else
		{
			if (!strcmp(p->data.num, p1->next->data.num))			// 判断编号是否唯一
			{
				printf("编号(%s)已存在，0-取消插入  1-替换节点:\n", p1->next->data.num);	
				scanf("%d", &flag);
				if(flag == 0)				// 取消插入
					printf("已取消插入\n");
				else						// 用新的数据替换原来的数据
				{
					p->next = p1->next->next;
					p1->next = p;
					printf("替换成功！！！\n");
				}
				return;
			}
		}
		p1 = p1->next;
	}
}	
LNode* ListFind(LinkList head) //查找 
{
	char i[5];
	LNode* p;
	printf("请输入需要查询的节点编号:\n");			// 按编号查找
	scanf("%s", i);
	p = head;
	while(p)
	{
		if (!strcmp(p->data.num, i))
			return p;
		p = p->next;
	}
	return p;
}
void DeleteNode(LinkList head)
{
	LNode* p=head;
	LNode* pre=NULL; 
	int i,j=0,flag;
	while(1)
	{
		printf("请输入需要删除节点的位置:\n");		// 按节点位置删除
		scanf("%d", &i);
		if (i > 0)
			break;
		else
			printf("输入不合法，请输入大于0的数！！"); 
	}
	while(1)
	{
		if(p)
		{
			if (j == i)		// 查找到节点后确认是否删除
			{
				printf("*编号（4） 姓名（8） 性别 电话（11） 地址（31） *\n");
				printf("---------------------------------------------\n");
			    printf("%s\t%s\t%s\t%s\t%s\n",p->data.num,p->data.name,
                    p->data.sex,p->data.phone,p->data.addr);
				printf("*********************************************\n");
                printf("是否删除该学生：0-否\t1-是\n");
				scanf("%d",&flag);
				if (flag)
				{
					pre->next = p->next;
					free(p);
					printf("节点删除成功！！！\n");
				}
				else
					printf("取消删除节点\n");
				return;
			}
			pre = p;
			p = p->next;
			j++;
		}
		else
		{
			printf("没有%d节点!!", i);
			return;
		}
	}
}	

void PrintList(LinkList head)
{
	LNode* p;
	p = head->next;
	printf("*编号（4） 姓名（8） 性别 电话（11） 地址（31） *\n");
	printf("---------------------------------------------\n");
	while(p)			// 循环输出节点信息
	{
		printf("%s\t%s\t%s\t%s\t%s\n",p->data.num,p->data.name,
                   p->data.sex,p->data.phone,p->data.addr);
		p = p->next;
	}
	printf("*********************************************\n");
}	

