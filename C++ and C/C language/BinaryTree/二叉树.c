#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <stdbool.h> //����true 
typedef struct{
	long stuId; // ѧ�� 
    long memoryAdd; // �ڴ��ַ 
} Record,*RecordType;
typedef struct BiTnode{
	RecordType data;
	struct BiTnode* lchild,*rchild;
} BiTnode,*BiTree;

/*�������������*/
BiTree CreateBiTree()
{
	static long m = 10000;
	BiTree node;
	long s;
	RecordType data = (RecordType) malloc (sizeof(RecordType));
	scanf("%ld", &s);
	if (s == 0)
		node = NULL;
	else
	{
		node = (BiTree) malloc (sizeof(BiTree));
		data->memoryAdd = ++m;
		data->stuId = s;
		node->data = data;
		node->lchild = CreateBiTree();
		node->rchild = CreateBiTree();
	}
	return node;
} 
/*�������������*/
void PreOrderTraverse(BiTree t)
{
	if(t)
	{
		printf("%ld\t", t->data->stuId);
		printf("%ld\n", t->data->memoryAdd);
		PreOrderTraverse(t->lchild);
		PreOrderTraverse(t->rchild);
	}
}
/*����ѧ�Ų������ڵ�*/
BiTnode* FindNode(BiTree t,long stuId) 
{
	BiTnode* p;
	if (t->data->stuId == stuId)
			return t;
	if (t->lchild) 
        p = FindNode(t->lchild, stuId);
	if(p)
		return p;
	if (t->rchild) 
        p = FindNode(t->lchild, stuId);
    return p;
} 
int main()
{
  	char ch ='\0';
  	BiTree tree = NULL;
 	do
	    {
		printf("*************��ѡ������Ҫ�Ĳ���************\n");
		printf("1. ����������\n");
		printf("2. �ȸ�����������\n");
		printf("3. ����ѧ�Ų����ڴ��ַ\n");
		printf("4. �˳�\n");
		printf("\n");
		
		ch=getchar();
		getchar();
		switch(ch)
		{
			case '1':
			{
				printf("�밴���ȸ�˳������ڵ㣺���û���ӽڵ㣬������0\n");
				tree = CreateBiTree();
				break;
			}
			case '2':
			{
				PreOrderTraverse(tree);
				break;
			}
			case '3':
			{
				printf("������ѧ�ţ�");
				long stuId =0;
				scanf("%ld",&stuId);
				if(stuId>0)
				{
					BiTnode* result = FindNode(tree,stuId);
					if(result!=NULL)
					{
						printf("ѧ�� %ld ��Ӧ��¼���ڴ��ַΪ %ld\n\n",stuId,result->data->memoryAdd);						 
					}
					else
					{ printf("�����ڸ�ѧ��\n\n"); }					
				}
				else
				    {printf("ѧ�ű��������\n\n");}
				break;
			}
			case '4':
			{   exit(1); break;	}
			default: 
			printf("hello");
			exit(1);			   
		}		
		_flushall(); //_flushall()����ڴ� 
	} while(true);	
  	return 0;
}
