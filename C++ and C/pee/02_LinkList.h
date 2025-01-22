#define ElemType int

// 单链表定义
typedef struct LNode{
	ElemType data;
	struct LNode *next;
}LNode, *LinkList;

// 创建带头节点的单链表
LinkList CreateList(){
	LinkList L;
	L = new LNode();
	L->next = NULL;
	return L;
}

// 头插法
LinkList List_HeadInsert(LinkList L, ElemType e){
	LNode *s;
	s = new LNode();
	s->data = e;
	s->next = L->next;
	L->next = s;
	return L;
}

// 尾插法
LinkList List_TailInsert(LinkList L, LNode *&r, ElemType e){
	LNode *s;
	s = new LNode();
	s->data = e;
	r->next = s;
	r = s;
	r->next = NULL;
	return L;
}


// 元素查找
LNode* LocateElem(LinkList L, ElemType e){
	LNode *p = L->next;
	while(p != NULL && p->data != e)
		p = p->next;
	return p;
}





