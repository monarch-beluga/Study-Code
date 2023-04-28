#include<iostream>
#include<stdio.h>
using namespace std;

#define SIZE 100

typedef struct 
{
    int num[SIZE];
    int len = 0;
}age;

void ListInsert(age *ar, int i, int e)
{
    ar->num[i] = e;
    ar->len++;
    printf("%d\n", ar->num[i]);
}


int main()
{
    // #if ONLINE_JUDGE
    // #else
    // freopen("input.txt", "r", stdin);
    // #endif
    age a;
    ListInsert(&a, 1, 5);
    printf("%d", a.num[1]);
    return 0;
}
