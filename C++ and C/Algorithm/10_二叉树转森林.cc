#include <iostream>
#include <string>
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

void Print(Tr T)            // 先序遍历，非递归
{
    stack<Tr> S;
    Tr p = T;
    while(!S.empty() || p)
    {
        if(p)
        {
            cout << p->data << " ";
            if(p->r)
                S.push(p->r);
            p = p->l;
        }
        else
        {
            p = S.top();
            S.pop();
        }
    }
}

void Print_tree(Tr T)       // 二叉树转森林
{
    Tr p = T;
    if (p)
    {
        cout << p->data << " ";
        if(p->l)
        {
            Print(p->l);
            cout << endl;
            if (p->r)
                Print_tree(p->r);
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
    Print_tree(tree);
    return 0;
}


