#include<iostream>
using namespace std;
#include<algorithm>

int main()
{
    int et = 17*3600, st = 8*3600;
    int n, k, h, m, s, p, count = 0, wait = 0, t;
    cin >> n >> k;
    int *cs = new int[n];
    for (int i = 0; i < n; ++i)
    {
        scanf("%d:%d:%d %d", &h, &m, &s, &p);
        cs[i] = (h*3600 + m*60 + s)*100 + p;
    }
    sort(cs, cs+n);
    for (int i = 0; i < n; ++i)
    {
        if (cs[i]/100 > et)
            break;
        if (i < k)
            t = max(cs[i]/100, st);
        else
        {
            sort(cs+(i-k), cs+i);
            t = max(cs[i-k], cs[i]/100);
        }
        wait += t - cs[i]/100;
        cs[i] = t + (cs[i]%100)*60;
        ++count;
    }
    printf("%.1f", wait*1.0/60/count);
    return 0;
}
