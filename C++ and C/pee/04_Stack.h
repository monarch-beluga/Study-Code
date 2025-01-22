#define MaxSize 100
#define ElemType int

typedef struct{
	ElemType data[MaxSize];
	int top;
}SqStack;

SqStack CreateStack(){
	SqStack S;
	S.top = -1;
	return S;
}

bool StackEmpty(SqStack S){
	if (S.top == -1)
		return true;
	else
		return false;
}

bool StackFull(SqStack S){
	if (S.top == MaxSize-1)
		return true;
	else
		return false;
}

bool Push(SqStack &S, ElemType x){
	if (StackFull(S))
		return false;
	S.data[++S.top] = x;
	return true;
}

bool Pop(SqStack &S, ElemType &x){
	if (StackEmpty(S))
		return false;
	x = S.data[top--];
	return true;
}

bool GetTop(SqStack S, ElemType &x){
	if (S.top == -1)
		return false;
	x = S.data[top];
	return true;
}



