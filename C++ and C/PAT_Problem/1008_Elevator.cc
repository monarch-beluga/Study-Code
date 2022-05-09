#include<iostream>
using namespace std;
int main()
{
    int n, pre, next, ts = 0, d;
    cin >> n;
    next = 0;
    for (int i = 0; i < n; ++i)
    {
        pre = next;
        cin >> next;
        d = next - pre;
        if (d > 0)
            ts += d*6;
        else
            ts -= d*4;
        ts += 5;
    }
    cout << ts;
    return 0;
}