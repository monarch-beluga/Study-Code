#include<iostream>
#include<stdio.h>
using namespace std;

typedef struct A
{
    int *p;
    int len;
}List;

void fun(List* l)
{
    l->len++;
    int *p = new int[l->len]();
    for (int i = 1; i < l->len-1; i++)
        p[i] = l->p[i-1] + l->p[i];

    delete[] l->p;
    l->p = p;
}


int main()
{
    // #if ONLINE_JUDGE
    // #else
    // freopen("input.txt", "r", stdin);
    // #endif
    int N, n;
    List yh;
    cin >> N;
    yh.len = 3;
    yh.p = new int[3]();
    yh.p[1] = 1;
    n = 1;
    while(1)
    {
        for (int i = 1; i < yh.len-1; i++, n++)
        {
            // cout << yh.p[i] << ' ';
            if (yh.p[i] == N)
            {
                cout << n;
                return 0;
            }
        }
        fun(&yh);
        cout << yh.len << '\n';
    }
    
    delete[] yh.p;
    return 0;
}




