/*������ʵ�ֲ�����Ϣ��������*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include<setjmp.h>
#include<windows.h>
typedef struct
{	char num[5];   //��� 
	char name[9];  //���� 
	char sex[3];   //�Ա� 
	char phone[13]; //�绰 
	char addr[31];  //��ַ 
}ElemType;
typedef struct node
{	//�ڵ����Ͷ���
	ElemType data;     //������ 
	struct node* next; //ָ����
}LNode,*LinkList;
LinkList pHead;
LNode *p;
jmp_buf mark;
int save = 0;
//��������
int menu_select();
LinkList CreateList(void); 
void InsertNode(LinkList head, LNode* p);
LNode* ListFind(LinkList head);
void DeleteNode(LinkList head);
void PrintList(LinkList head);

//������
int main()
{
	FILE* f;
	for(;;)
	{
		switch(menu_select())
		{
			case 1:
			printf("*******************************\n");
			printf("* ������Ϣ��Ľ���(Tab���ָ�)*\n");
			printf("*******************************\n");
			pHead = CreateList();
			break;
			case 2:
			printf("*********************************************\n");
			printf("**\t\t ������Ϣ���  \t\t   **\n");
			printf("*********************************************\n");
			printf("*��ţ�4�� ������8�� �Ա� �绰��11�� ��ַ��31��*\n");
			printf("*********************************************\n");
			p=(LNode*)malloc(sizeof(LNode));
			scanf("%s%s%s%s%s",p->data.num,p->data.name,
                   p->data.sex,p->data.phone,p->data.addr);
            InsertNode(pHead,p);
			save++;
			break;
			case 3:
			printf("*******************************\n");
			printf("**   ������Ϣ��ѯ  **\n");
			printf("*******************************\n");
			p=ListFind(pHead);
			if(p!=NULL)
			{
				printf("*��ţ�4�� ������8�� �Ա� �绰��11�� ��ַ��31�� *\n");
				printf("---------------------------------------------\n");
				printf("%s\t%s\t%s\t%s\t%s\n",p->data.num,p->data.name,
						p->data.sex,p->data.phone,p->data.addr);
				printf("*********************************************\n");
			}
			else
               printf("û�в鵽Ҫ��ѯ�Ĳ���!\n");
            break;
            case 4:
            printf("*******************************\n");
			printf("**   ������Ϣɾ��  **\n");
			printf("*******************************\n");
			DeleteNode(pHead); // ɾ���ڵ�
			save++;
			break;
			case 5:
            printf("*********************************************\n");
			printf("**\t   ������Ϣ��������  \t**\n");
			printf("*********************************************\n");
			PrintList(pHead); 
			break;
			case 0:
			if(save)
			{
				f = fopen("Patients.txt","w");			// ���
				p = pHead->next;
				while(p)
				{
					fprintf(f, "%s\t%s\t%s\t%s\t%s\n",p->data.num,p->data.name,
			                   p->data.sex,p->data.phone,p->data.addr);
					p = p->next;
				}
				fclose(f);
			}
		    printf("\t �ټ�!\n");
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
	printf("   ������Ϣ����ϵͳ\n");
	printf("=================================\n");
	printf("   1. ������Ϣ��Ľ���\n");
	printf("   2. �����ڵ�Ĳ���\n");
	printf("   3. �����ڵ�Ĳ�ѯ\n");
	printf("   4. �����ڵ��ɾ��\n");
	printf("   5. ������Ϣ������\n");
	printf("   0. �˳�����ϵͳ\n");
	printf("=================================\n");
	for(;;)
	{
		sn = setjmp(mark);
		if (!scanf("%d",&sn))
			longjmp(mark, -1);
		if(sn<0||sn>5)
			printf("\n\t ���������ѡ 0-5");
	    else
	    	break;
	}
	system("cls");
	return sn;
}
LinkList CreateList(void)  //β�巨������ͷ�ڵ�Ĳ�����Ϣ�� 
{
	LNode* p;
	FILE *f;
	pHead = (LinkList)malloc(sizeof(LNode));
	pHead->next = NULL;
	f = fopen("Patients.txt","r");
	if (f)					// �ж��ļ��Ƿ����
	{
		while(1)				// ѭ����ȡ��Ϣ
		{
			// �ļ���ȡ
			p = (LNode*)malloc(sizeof(LNode));
			fscanf(f, "%s\t%s\t%s\t%s\t%s", p->data.num, p->data.name,
					p->data.sex, p->data.phone, p->data.addr);
			if (!feof(f))			// �ж��ļ���ȡ�Ƿ����
				InsertNode(pHead,p);
			else
				break;
		}
	}
	fclose(f);
	printf("������Ϣ�����ɹ�������\n");
	return pHead;
}
void InsertNode(LinkList head, LNode* p) //��headָ��������в���ڵ� 
{
	LNode* p1;
	int flag;
	p1 = head;
	while(p1)
	{
		if (p1->next == NULL)			// β������
		{
			p->next = p1->next;
			p1->next = p;
			printf("�ڵ����ɹ�������\n");
			break;
		}
		else
		{
			if (!strcmp(p->data.num, p1->next->data.num))			// �жϱ���Ƿ�Ψһ
			{
				printf("���(%s)�Ѵ��ڣ�0-ȡ������  1-�滻�ڵ�:\n", p1->next->data.num);	
				scanf("%d", &flag);
				if(flag == 0)				// ȡ������
					printf("��ȡ������\n");
				else						// ���µ������滻ԭ��������
				{
					p->next = p1->next->next;
					p1->next = p;
					printf("�滻�ɹ�������\n");
				}
				return;
			}
		}
		p1 = p1->next;
	}
}	
LNode* ListFind(LinkList head) //���� 
{
	char i[5];
	LNode* p;
	printf("��������Ҫ��ѯ�Ľڵ���:\n");			// ����Ų���
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
		printf("��������Ҫɾ���ڵ��λ��:\n");		// ���ڵ�λ��ɾ��
		scanf("%d", &i);
		if (i > 0)
			break;
		else
			printf("���벻�Ϸ������������0��������"); 
	}
	while(1)
	{
		if(p)
		{
			if (j == i)		// ���ҵ��ڵ��ȷ���Ƿ�ɾ��
			{
				printf("*��ţ�4�� ������8�� �Ա� �绰��11�� ��ַ��31�� *\n");
				printf("---------------------------------------------\n");
			    printf("%s\t%s\t%s\t%s\t%s\n",p->data.num,p->data.name,
                    p->data.sex,p->data.phone,p->data.addr);
				printf("*********************************************\n");
                printf("�Ƿ�ɾ����ѧ����0-��\t1-��\n");
				scanf("%d",&flag);
				if (flag)
				{
					pre->next = p->next;
					free(p);
					printf("�ڵ�ɾ���ɹ�������\n");
				}
				else
					printf("ȡ��ɾ���ڵ�\n");
				return;
			}
			pre = p;
			p = p->next;
			j++;
		}
		else
		{
			printf("û��%d�ڵ�!!", i);
			return;
		}
	}
}	

void PrintList(LinkList head)
{
	LNode* p;
	p = head->next;
	printf("*��ţ�4�� ������8�� �Ա� �绰��11�� ��ַ��31�� *\n");
	printf("---------------------------------------------\n");
	while(p)			// ѭ������ڵ���Ϣ
	{
		printf("%s\t%s\t%s\t%s\t%s\n",p->data.num,p->data.name,
                   p->data.sex,p->data.phone,p->data.addr);
		p = p->next;
	}
	printf("*********************************************\n");
}	

