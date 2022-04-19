#include<iostream>
using namespace std;
#include<string>

int main()
{
    int n, h, m, s, time, st = 999999, et = -1;
    string ints, outs, str;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> str;
        scanf("%d:%d:%d", &h, &m, &s);
        time = h*10000+m*100+s;
        if (time < st)
            st = time, ints = str;
        scanf("%d:%d:%d", &h, &m, &s);
        time = h*10000+m*100+s;
        if (time > et)
            et = time, outs = str;
    }
    cout << ints << " " << outs;
    return 0;
}