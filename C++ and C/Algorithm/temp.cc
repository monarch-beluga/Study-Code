#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

typedef struct yue
{
    int k, j;
    float m;
}Yue;

bool cmp(Yue a, Yue b)
{
    return a.m > b.m;
}

int main()
{
#if ONLINE_JUDGE
#else
    freopen("input.txt", "r", stdin);
#endif
    string s = "123456";
    s = &s[1];
    cout << s;
    return 0;
}