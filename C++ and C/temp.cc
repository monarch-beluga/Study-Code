#include<iostream>
using namespace std;

void fun(int& p1, int &p2)
{
    p1 = p2;
}

int main()
{
    int a, b;
    int *p, *q;
    a = 3;
    b = 4;
    p = &a;
    q = &b;
    cout << *p << '\n';
    fun(p, q);
    cout << *p << '\n';
    return 0;
}
