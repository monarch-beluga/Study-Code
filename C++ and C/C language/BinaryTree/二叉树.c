#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <stdbool.h> //定义true 
typedef struct{
	long stuId; // 学号 
    long memoryAdd; // 内存地址 
} Record,*RecordType;
typedef struct BiTnode{
	RecordType data;
	struct BiTnode* lchild,*rchild;
} BiTnode,*BiTree;

/*创建先序二叉树*/
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
/*先序遍历二叉树*/
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
/*根据学号查找树节点*/
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
		printf("*************请选择所需要的操作************\n");
		printf("1. 构建二叉树\n");
		printf("2. 先根遍历二叉树\n");
		printf("3. 根据学号查找内存地址\n");
		printf("4. 退出\n");
		printf("\n");
		
		ch=getchar();
		getchar();
		switch(ch)
		{
			case '1':
			{
				printf("请按照先根顺序输入节点：如果没有子节点，则输入0\n");
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
				printf("请输入学号：");
				long stuId =0;
				scanf("%ld",&stuId);
				if(stuId>0)
				{
					BiTnode* result = FindNode(tree,stuId);
					if(result!=NULL)
					{
						printf("学号 %ld 对应记录的内存地址为 %ld\n\n",stuId,result->data->memoryAdd);						 
					}
					else
					{ printf("不存在该学号\n\n"); }					
				}
				else
				    {printf("学号必须大于零\n\n");}
				break;
			}
			case '4':
			{   exit(1); break;	}
			default: 
			printf("hello");
			exit(1);			   
		}		
		_flushall(); //_flushall()清空内存 
	} while(true);	
  	return 0;
}
