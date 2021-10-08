/*********************************************/
/*    �ڽӱ�洢�ṹ   �ļ�����ljb.h     	 */
/*********************************************/

#include <stdio.h>
#include <stdlib.h>
#define M 20					/*Ԥ����ͼ����󶥵���*/
typedef char DataType;  /*������Ϣ��������*/
typedef struct node{    /*�߱���*/
   int adjvex;                  /*�ڽӵ�*/
   struct node *next;
}EdgeNode;

typedef struct vnode{   /*ͷ�������*/
   DataType vertex;         /*������Ϣ*/
   EdgeNode *FirstEdge; /*�ڽ�����ͷָ��*/
}VertexNode;

typedef struct{           /*�ڽӱ�����*/
 VertexNode adjlist[M];  /*���ͷ����˳���*/
 int n,e;                 /*ͼ�Ķ����������*/
}LinkedGraph;


/*�������ܣ�����ͼ���ڽӱ�
  �����������ڽӱ�ָ�����g�����ͼ��Ϣ���ļ���filename;ͼ�����Ͳ���c��c=0��ʾ��������ͼ�������ʾ��������ͼ 
  ��������ֵ����
*/ 
void creat(LinkedGraph *g,char *filename,int c)
{ 
	int i,j,k;
	EdgeNode *s, *p;
	FILE *fp;
	fp=fopen(filename,"r");
	if (fp)
	{
		fscanf(fp,"%d%d",&g->n,&g->e);              /*���붥���������*/
		
		for(i=0;i<g->n;i++)
		{
		    fscanf(fp,"%1s",&g->adjlist[i].vertex);    /*���붥����Ϣ*/
		    g->adjlist[i].FirstEdge=NULL;         /*�߱���Ϊ�ձ�*/
		}
		
		for(k=0;k<g->e;k++)                     /*ѭ��e�ν����߱�*/
		{
		    fscanf(fp,"%d%d",&i,&j);                 /*��������ԣ�i,j��*/
		    s=(EdgeNode *)malloc(sizeof(EdgeNode));
		    s->adjvex=j;                         /*�ڽӵ����Ϊj*/
		    // s->next=g->adjlist[i].FirstEdge;
		    if (g->adjlist[i].FirstEdge == NULL)
		    {
		    	s->next=g->adjlist[i].FirstEdge;
		    	g->adjlist[i].FirstEdge=s;
		    }
		    else
		    {
		    	p = g->adjlist[i].FirstEdge;
			    while(p)
			    {
			    	if (p->next == NULL)
			    	{
			    		p->next = s;
			    		s->next = NULL;
			    	}
			    	p = p->next;
			    }
		    }
		    
		    // g->adjlist[i].FirstEdge=s;           /*���½��*s���붥��vi�ı߱�ͷ��*/
		    if (c==0)                            /*����ͼ*/ 
		    {
			    s=(EdgeNode *)malloc(sizeof(EdgeNode));
			    s->adjvex=i;                         /*�ڽӵ����Ϊi*/
			    s->next=g->adjlist[j].FirstEdge;
			    if (g->adjlist[j].FirstEdge == NULL)
			    {
			    	s->next=g->adjlist[j].FirstEdge;
			    	g->adjlist[j].FirstEdge=s;
			    }
			    else
			    {
			    	p = g->adjlist[j].FirstEdge;
				    while(p)
				    {
				    	if (p->next == NULL)
				    	{
				    		p->next = s;
				    		s->next = NULL;
				    	}
				    	p = p->next;
				    }
			    }
			    // g->adjlist[j].FirstEdge=s;           /*���½��*s���붥��vj�ı߱�ͷ��*/
			}
		}
		fclose(fp);
	}
	else
		g->n=0;
}
/*---����print():����ڽӱ�洢�ṹ---*/
void print(LinkedGraph  g)
{  
	EdgeNode *p;
	int i;
	for (i=0;i<g.n;i++)
	{   
		printf("%c",g.adjlist[i].vertex);
		p=g.adjlist[i].FirstEdge;
		while (p)
		{   
			printf("-->%d",p->adjvex);
			p=p->next;
		}
		printf("\n");
	}
}
