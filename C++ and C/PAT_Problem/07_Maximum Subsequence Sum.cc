#include<iostream>
using namespace std;
int main()
{
    int pre, k, n, s, e, sum, i, start, end;
    n = -1;
    cin >> k;
    for (i = 0; i < k && n < 0; ++i)
    {
        pre = n;
        cin >> n;
        if (!i)
            start = n;
    }
    if (n < 0)
        printf("0 %d %d", start, n);
    else
    {
        start = pre = end = s = e = sum = n;
        for(; i < k; ++i)
        {
            cin >> n;
            if (pre + n < n)
                pre = s = e = n;
            else
                pre += n, e = n;
            if (sum < pre)
                sum = pre, start = s, end = e;
        }
        printf("%d %d %d", sum, start, end);
    }
    return 0;
}