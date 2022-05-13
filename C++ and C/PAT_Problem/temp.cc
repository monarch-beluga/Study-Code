#include<iostream>
using namespace std;

int main()
{
    #if ONLINE_JUDGE
    #else
    freopen("input.txt", "r", stdin);
    #endif
    int n, post[35], in[35];
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> post[i];
    for (int i = 0; i < n; ++i)
        cin >> in[i];
    return 0;
}
