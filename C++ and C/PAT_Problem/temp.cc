#include<iostream>
using namespace std;
#include<algorithm>

typedef struct player
{
    int time, p, tag;
}Pl;
typedef struct table
{
    int e_time, tag, count;
}T;
bool cmp(Pl a, Pl b)
{
    return a.time < b.time;
}
bool cmp1(Pl a, Pl b)
{
    if (a.tag != b.tag)
        return a.tag > b.tag;
    else
        return a.time < b.time;
}

int main()
{
    #if ONLINE_JUDGE
    #else
    freopen("input.txt", "r", stdin);
    #endif
    int n, m, k, H, M, S;
    int e_time = 3600*21;
    cin >> n;
    Pl *ps = new player[n];
    for (int i = 0; i < n; ++i)
    {
        scanf("%d:%d:%d %d %d", &H, &M, &S, &ps[i].p, &ps[i].tag);
        ps[i].time = H*3600+M*60+S;
    }
    cin >> k >> m;
    T *ts = new table[k];
    for (int i = 0; i < k; ++i)
        ts[i].count = ts[i].tag = 0;
    for (int i = 0; i < m; ++i)
    {
        cin >> H;
        ts[H-1].tag = 1;
    }
    sort(ps, ps+n, cmp);
    int min_time, t, j, s, wait;
    for (int i = 0; i < n; ++i)
    {
        if (i < k)
        {
            t = i;
            s = ps[i].time;
        }
        else
        {
            min_time = ts[0].e_time;
            t = 0;
            for (j = 0; j < k && min_time > ps[i].time; ++j)
                if (min_time > ts[j].e_time)
                {
                    t = j;
                    min_time = ts[j].e_time;
                }
            if (ts[t].tag && min_time > ps[i].time)
            {
                cout << t << endl;
                for (j = i; ps[j].time <= min_time && !ps[j].tag; ++j);
                if(i != j && ps[j].tag)
                    sort(ps+i, ps+j+1, cmp1);
            }
            s = max(min_time, ps[i].time);
        }
        if (s > e_time)
            break;
        ts[t].e_time = s + ps[i].p*60;
        ++ts[t].count;
        wait = (s*1.0 - ps[i].time)/60 + 0.5;
        printf("%02d:%02d:%02d", ps[i].time/3600, (ps[i].time%3600)/60, ps[i].time%60);
        printf(" %02d:%02d:%02d %d\n", s/3600, (s%3600)/60, s%60, wait);
    }
    cout << ts[0].count;
    for (int i = 1; i < k; ++i)
        cout << " " << ts[i].count;
    return 0;
}
