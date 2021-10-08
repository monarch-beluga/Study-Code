#include <iostream>
#include <string>
#include<stdio.h>
#include<vector>
#include<stack>
using namespace std;

typedef struct Tree
{
    char data;
    Tree* l;
    Tree* r;
}*Tr;

Tr tree;

void Creat(Tr &T)
{
    char ch;
    scanf("%c", &ch);
    if(ch == '#') 
        T = NULL;
    else
    {
        T = (Tree *) malloc(sizeof(Tree));
        T->data = ch;
        Creat(T->l);
        Creat(T->r);
    }
}

void Print(Tr T)            // 后序遍历，非递归
{
    stack<Tr> S;
    Tr p = T;
    Tr pr = NULL;        // 记录已经访问的节点
    while(!S.empty() || p)
    {
        if(p)               // 先访问左节点
        {
            S.push(p);
            p = p->l;
        }
        else
        {
            p = S.top();
            S.pop();
            if(((!p->r) || (pr==p->r))) // 如果右节点为空或者已访问
            {
                cout << p->data << " ";     // 访问
                pr = p;
                p = NULL;
            }
            else                // 否则访问右节点
            {
                S.push(p); 
                p = p->r;
            }
        }
    }

}

int main()
{
#if ONLINE_JUDGE
#else
    freopen("input.txt", "r", stdin);
#endif
    Creat(tree);
    Print(tree);
    return 0;
}


