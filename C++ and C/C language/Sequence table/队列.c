#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 20
typedef struct
{
	char name[20]; // 姓名
	char sex; //性别F为女性，M为男性
}Person; // 队列元素
typedef Person DataType;
typedef struct{
	DataType elem[MAXSIZE];
	int front,rear;
}squeuetp; // 顺序队列

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
	InitQueue(&Fdancer); // 女士初始化队列
	InitQueue(&Mdancer); // 男士初始化队列
	
	for(i=0;i<num;i++)
	{
		p = dancer[i];
		if(p.sex=='F')
		   EnQueue(&Fdancer,p); //女士入队
        else
           EnQueue(&Mdancer,p); //男士入队
	}
	printf("The dancing partners are: \n\n");
	while(!QueueEmpty(Fdancer)&&!QueueEmpty(Mdancer))
	{
		p = DelQueue(&Fdancer);//女士出队
		printf(" %s ",p.name);
    	p = DelQueue(&Mdancer);//男士出队
		printf(" %s ",p.name);			
	}
	if(!QueueEmpty(Fdancer))
	{
		printf("\n There are %d women waitin for the next round.",Size(Fdancer));
	    p = Head(Fdancer); //取队头
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
	DataType dancer[5]; // 设定5个舞者
	int i;
	for(i=0;i<5;i++)
	   scanf("%s %c",dancer[i].name,&dancer[i].sex);
	DancePartner(dancer,5);
	return 0;
}

void InitQueue(squeuetp *sq)	// 初始化 
{
	// front和rear都为0 
	sq->front = 0;	
	sq->rear = 0;
}

void EnQueue(squeuetp *sq, DataType p)	// 进入队列 
{
	// 将p赋值为elem数组中rear位置 ，然后rear加一 
	sq->elem[sq->rear] = p;
	sq->rear++;
}

int QueueEmpty(squeuetp sq)				// 判断队列是否为空 
{
	// c语言中没有布偶类型，真返回1，假返回0 
	return (sq.front == sq.rear);		// front ==  rear则队列为空， 
}

DataType DelQueue(squeuetp *sq)			// 出队列 
{
	int i = sq->front;					// 先获取front位置 
	sq->front++;						// front加1，出队 
	return sq->elem[i];					// 返回原来front位置的节点 
}

int Size(squeuetp sq)					// 获取队列大小 
{
	return sq.rear - sq.front;			// rear - front 即为队列大小 
}

DataType Head(squeuetp sq)				// 获取头节点 
{
	return sq.elem[sq.front];			// 返回front位置的节点 
}

/*
小红 F
小明 M
小王 M
小丽 F
小刘 M 
*/