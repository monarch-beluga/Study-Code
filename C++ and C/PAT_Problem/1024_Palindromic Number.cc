#include<iostream>
using namespace std;

int main()
{
    int pre[100] = {0}, n[100], e = -1, k, i, s, flag;
    string Sn;
    cin >> Sn >> k;
    for (i = 0; i < (int)Sn.size(); ++i)
        n[++e] = Sn[i] - '0';
    for (i = 0; i < k; ++i)
    {
        flag = 1;
        for (int j = 0; j <= e; ++j)
        {
            pre[j] = n[e-j];
            if (pre[j] != n[j])
                flag = 0;
        }
        if (flag)
            break;
        s = 0;
        for (int j = 0; j <= e; ++j)
        {
            s += pre[j] + n[j];
            n[j] = s % 10;
            s = s / 10;
        }
        if (s != 0)
            n[++e] = s;
    }
    for (int j = e; j >= 0; --j)
        cout << n[j];
    printf("\n%d", i);
    return 0;
}
