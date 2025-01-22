#define ElemType int;
#define MaxSize 100;

typedef struct{
	ElemType data[MaxSize];
	int front, rear;
}SqQueue;

SqQueue CreateQueue(){
	SqQueue Q;
	Q.front = Q.rear = 0;
}

bool QueueEmpty(SqQueue Q){
	if (Q.front == Q.rear)
		return true;
	else
		return false;
}

bool QueueFull(SqQueue Q){
	if((Q.rear+1)%MaxSize == Q.front)
		return true;
	else
		return false;
}

bool EnQueue(SqQueue &Q, ElemType x){
	if(QueueFull(Q))
		return false;
	Q.data[Q.rear] = x;
	Q.rear = (Q.rear+1)%MaxSize;
	return true;
}

bool DeQueue(SqQueue &Q, ElemType &x){
	if(QueueEmpty(Q))
		return false;
	x = Q.data[Q.front];
	Q.front = (Q.front+1)%MaxSize;
	return true;
}

