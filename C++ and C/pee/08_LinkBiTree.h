#include<stack>

#define ElemType int;

typedef struct BiTNode{
	ElemType data;
	struct BiTNode *lchild, *rchild;
}BiTNode, *BiTree;

void visit(BiTree T){
	printf("%d ", T->data);
}

void PreOrder(BiTree T){
	if(T != NULL){
		visit(T);
		PreOrder(T->lchild);
		PreOrder(T->rchild);
	}
}

void PreOrderStack(BiTree T){
	stack<BiTree>S;
	S.push(T);
	while(!S.empty()){
		visit(S.top());
		S.pop();
		if (T->rchild != NULL)
			S.push(T->rchild);
		if (T->lchild != NULL)
			S.push(T->lchild);
	}
}

