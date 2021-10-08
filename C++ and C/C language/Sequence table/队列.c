#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 20
typedef struct
{
	char name[20]; // ����
	char sex; //�Ա�FΪŮ�ԣ�MΪ����
}Person; // ����Ԫ��
typedef Person DataType;
typedef struct{
	DataType elem[MAXSIZE];
	int front,rear;
}squeuetp; // ˳�����

void InitQueue(squeuetp *sq);
void EnQueue(squeuetp *sq, DataType p); 
int QueueEmpty(squeuetp sq);
DataType DelQueue(squeuetp *sq);
int Size(squeuetp sq);
DataType Head(squeuetp sq);

void DancePartner(DataType dancer[], int num)
{
	int i;
	DataType p;
	squeuetp Mdancer,Fdancer;
	InitQueue(&Fdancer); // Ůʿ��ʼ������
	InitQueue(&Mdancer); // ��ʿ��ʼ������
	
	for(i=0;i<num;i++)
	{
		p = dancer[i];
		if(p.sex=='F')
		   EnQueue(&Fdancer,p); //Ůʿ���
        else
           EnQueue(&Mdancer,p); //��ʿ���
	}
	printf("The dancing partners are: \n\n");
	while(!QueueEmpty(Fdancer)&&!QueueEmpty(Mdancer))
	{
		p = DelQueue(&Fdancer);//Ůʿ����
		printf(" %s ",p.name);
    	p = DelQueue(&Mdancer);//��ʿ����
		printf(" %s ",p.name);			
	}
	if(!QueueEmpty(Fdancer))
	{
		printf("\n There are %d women waitin for the next round.",Size(Fdancer));
	    p = Head(Fdancer); //ȡ��ͷ
		printf(" %s will be the first to get a partner.\n",p.name);	
		
	}
	else if(!QueueEmpty(Mdancer))
	{
		printf("\n There are %d men waitin for the next round.",Size(Mdancer));
	    p = Head(Mdancer);
		printf(" %s will be the first to get a partner.\n",p.name);	
	}
}

int main(int argc, char *argv[])
{
	DataType dancer[5]; // �趨5������
	int i;
	for(i=0;i<5;i++)
	   scanf("%s %c",dancer[i].name,&dancer[i].sex);
	DancePartner(dancer,5);
	return 0;
}

void InitQueue(squeuetp *sq)	// ��ʼ�� 
{
	// front��rear��Ϊ0 
	sq->front = 0;	
	sq->rear = 0;
}

void EnQueue(squeuetp *sq, DataType p)	// ������� 
{
	// ��p��ֵΪelem������rearλ�� ��Ȼ��rear��һ 
	sq->elem[sq->rear] = p;
	sq->rear++;
}

int QueueEmpty(squeuetp sq)				// �ж϶����Ƿ�Ϊ�� 
{
	// c������û�в�ż���ͣ��淵��1���ٷ���0 
	return (sq.front == sq.rear);		// front ==  rear�����Ϊ�գ� 
}

DataType DelQueue(squeuetp *sq)			// ������ 
{
	int i = sq->front;					// �Ȼ�ȡfrontλ�� 
	sq->front++;						// front��1������ 
	return sq->elem[i];					// ����ԭ��frontλ�õĽڵ� 
}

int Size(squeuetp sq)					// ��ȡ���д�С 
{
	return sq.rear - sq.front;			// rear - front ��Ϊ���д�С 
}

DataType Head(squeuetp sq)				// ��ȡͷ�ڵ� 
{
	return sq.elem[sq.front];			// ����frontλ�õĽڵ� 
}

/*
С�� F
С�� M
С�� M
С�� F
С�� M 
*/