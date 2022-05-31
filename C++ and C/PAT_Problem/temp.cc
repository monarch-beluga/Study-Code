#include<iostream>
using namespace std;
#include<algorithm>

typedef struct station
{
    float p, d;
}GS;
bool cmp(GS a, GS b)
{
    return a.d < b.d;
}

int main()
{
    #if ONLINE_JUDGE
    #else
    freopen("input.txt", "r", stdin);
    #endif
    float Cmax, D, Davg, Xmax = 0, x, cost, pmin, pre_p, c = 0;
    int n, g = 0;
    cin >> Cmax >> D >> Davg >> n;
    GS *ss = new station[n];
    for (int i = 0; i < n; ++i)
        cin >> ss[i].p >> ss[i].d;
    sort(ss, ss+n, cmp);
    while(g < n)
    {
        x = Cmax * Davg + Xmax;
        if (x >= D)
        {
            cost += (D - Xmax)/Davg*pre_p;
            printf("%.2f", cost);
            return 0;
        }
        for (int i = g+1; ss[i].d <= x && i < n; ++i)
            if(ss[i].p <= pmin)
            {
                pmin = ss[i].p;
                g = i;
            }
        if (pmin > pre_p)
        {
            cost += (Cmax-c)*pre_p;
            c = Cmax - (ss[g].d - Xmax)/Davg;
        }
        else
        {
            cost += ((ss[g].d - Xmax)/Davg)*pre_p;
            c = 0;
        }
        Xmax = ss[g].d;
        printf("%d %.2f %.2f %.2f %.2f %.2f\n", g, pre_p, pmin, cost, c, Xmax);
        pre_p = ss[g].p;
        ++g;
        pmin = ss[g].p;
    }
    printf("The maximum travel distance = %.2f", x);
    return 0;
}
