#define ElemType int;

typedef struct LinkNode{
	ElemType data;
	struct LinkNode *next;
}LinkNode;


typedef struct{
	LinkNode *front, *rear;
}LinkQueue;

LinkQueue CreateQueue(){
	LinkQueue Q;
	Q.front = Q.rear = new LinkNode();
	Q.front->next = NULL;
	return Q;
}

bool QueueEmpty(LinkQueue Q){
	if (Q.front == Q.rear)
		return true;
	else
		return false;
}

void EnQueue(LinkQueue &Q, ElemType x){
	LinkNode *s = new LinkNode();
	s->data = x;
	s->next = NULL;
	Q.rear->next = s;
	Q.rear = s;
}

bool DeQueue(LinkQueue &Q, ElemType &x){
	if(QueueEmpty(Q))
		return false;
	LinkNode *p = Q.front->next;
	x = p->data;
	Q.front->next = p->next;
	if(Q.rear == p)
		Q.rear = Q.front;
	delete p;
	return true;
}

