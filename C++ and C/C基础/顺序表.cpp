#include <stdio.h>
#define maxlen 100
typedef int datatype;
typedef struct
{
	datatype data[maxlen];
	int length;
}seqlist;
seqlist del(seqlist a,seqlist c);
void initlist(seqlist *l);		
void addlist(seqlist *l);
void printlist(seqlist l);
datatype getdode(seqlist l,int i);
int locate(seqlist l,datatype e);
seqlist deletelist(seqlist l,int i);		//ɾ��˳�����iλ�õ���
void commondate(seqlist a,seqlist b,seqlist *c);		//��ͬԪ��
seqlist merge(seqlist a,seqlist b,seqlist c);		//�ϲ�
void inversion(seqlist *l);				//����
void part(seqlist *c,seqlist l);		//��׼����
void Sort(seqlist l);			//�������У�ʹ˳�������
int main()
{
	seqlist a,b,c,l;			
	 initlist(&a);
	 addlist(&a);
	 printlist(a);
	  initlist(&b);
	 addlist(&b);
	 printlist(b);
	 initlist(&l);
	 puts("a��b�Ĺ�ͬԪ��Ϊ��");
	 commondate(a,b,&c);
	 printlist(c);
	 puts("ɾ��b�г��ֵ�Ԫ�غ��˳���a:");
	 a = del(a,c);
	 printlist(a);
	 Sort(a);
	 Sort(b);
	 printf("�ϲ����");
	 c = merge(a,b,c);
	 Sort(c);
	 puts("ԭ˳���Ϊ��");
	 printlist(c);
	 inversion(&c);
	 puts("ԭ˳���Ϊ��");
	 printlist(c);
	 part(&c,l);
	 return 0;
}
void initlist(seqlist *l)
	{
	l->length=0;
	}
void addlist(seqlist *l)
{
	datatype x;
	char h;
	do
	{
	if(l->length==maxlen)
	{
		printf("��˳�������");
		return;
	}
	scanf("%d",&x);
	l->data[l->length]=x;
	l->length++;
	printf("�Ƿ������ӣ�y or n\n");
	scanf(" %c",&h);
	}while(h=='y');
}
void printlist(seqlist l)
{
	int i;
	for(i=0;i<l.length;i++)
	printf("(%d)%d",i+1,l.data[i]);
	putchar('\n');
}

datatype getnode(seqlist l,int i)
{
	if(i<1||i>l.length)
	{
		printf("����λ�ô���");
		return -1;
	}
	return(l.data[i-1]);
}
int locate(seqlist l,datatype e)
{
	 int i;
	 for(i=0;i<l.length;i++)
	 {
	 	if(l.data[i]==e)
	 	return i+1;
	 }
	return 0;//����	
}
void commondate(seqlist a,seqlist b,seqlist *c)
{
	int i,j;
	datatype x;
	initlist(c);
	for(i=1;i<=a.length;i++)
	{
		x=getnode(a,i);
		j=locate(b,x);
		if(j&&!locate(*c,x))
		c->data[c->length++] = x;
	}
}
seqlist deletelist(seqlist l,int i)
	{	
		int j;
		if(i<1||i>l.length)
		{
		printf("λ�ò��Ϸ���");
		return l;
		}
		for(j=i;j<l.length;j++)
			l.data[j-1]=l.data[j];
		l.length--;
		return l;
	}
seqlist del(seqlist a,seqlist c)
{
	int x,j;
	for(int i = 0;i<c.length;i++)
	{
		x = c.data[i];
		j = locate(a,x);
		if(j)
			a = deletelist(a,j);
	}
	return a;
}
void Sort(seqlist l)
{
	static char ch = 'a';
	int i,j,x;
	for(i = l.length-1;i>0;i--)
		for(j = 0;j<i;j++)
			if(l.data[j]<l.data[j+1])
				x = l.data[j],l.data[j] = l.data[j+1],l.data[j+1] = x;
	printf("����˳���%cΪ��\n",ch++);
	printlist(l);
}
seqlist merge(seqlist a,seqlist b,seqlist c)
{
	int i=0,j=0,n = 0;
	initlist(&c);
	while(i<a.length)
		c.data[c.length++] = a.data[i++];
	while(j<b.length)
		c.data[c.length++] = b.data[j++];
	return c;
}
void inversion(seqlist *l)
{
	int i;
	datatype t;
	for(i=0;i<l->length/2;i++)
	{
	t=l->data[i];
	l->data[i]=l->data[l->length-1-i];
	l->data[l->length-1-i]=t;
	}
	puts("˳���������ǣ�");
	printlist(*l);
}
void part(seqlist *c,seqlist l)
{
	int t = c->data[0];
	initlist(&l);
	for(int i = 1;i<c->length;i++)
		if(c->data[i]<t) l.data[l.length++] = c->data[i];
	l.data[l.length++] = t;
	for(int i = 1;i<c->length;i++)
		if(c->data[i]>t) l.data[l.length++] = c->data[i];
	puts("����׼���ֺ��˳���");
	printlist(l);
}