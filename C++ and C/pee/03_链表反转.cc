#include<stdio.h>
#include<stdlib.h>
#include "02_LinkList.h"

void PrintList(LinkList L){
    LNode *p = L->next;
    while(p)
    {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}

LinkList ReverseList(LinkList L){
    LNode *prev=NULL, *next, *curr=L->next;
    while(curr)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    L->next = prev;
    return L;
}

int main(){
    LinkList L;
    L = CreateList();
    for (int i = 0; i <= 5; i++)
         L = List_HeadInsert(L, i);
    PrintList(L);
    L = ReverseList(L);
    PrintList(L);
    return 0;
}



