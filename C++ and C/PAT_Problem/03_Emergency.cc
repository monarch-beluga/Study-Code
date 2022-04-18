/*
邻接表构建无向图，然后使用迪杰斯特拉算法，计算最短路径
*/
#include<iostream>
#define inf 99999
using namespace std;

typedef struct road
{
    int city_end;
    int length;
    road* next;
}*r;
RainbowBracketstypedef struct ciRainbowBracketsty
{
    int teams;
    road* head;
} C;

int main()
{
    int n, m, c1, c2;
    int s, e, l, t, Min;
    C *citys;
    r p;
    int *fina, *ps, *minl, *maxt;
    cin >> n >> m >> c1 >> c2;
    fina = new int[n];
    ps = new int[n];
    minl = new int[n];
    maxt = new int[n];
    citys = new C[n];
    for (int i = 0; i < n; ++i)
    {
        cin >> t;
        citys[i].teams = t;
        citys[i].head = NULL;
        fina[i] = 1;
        minl[i] = inf;
        ps[i] = 1;
        maxt[i] = 0;
    }
    for (int i = 0; i < m; ++i)
    {
        cin >> s >> e >> l;
        p = new road;
        p->city_end = e;
        p->length = l;
        p->next = citys[s].head;
        citys[s].head = p;
        p = new road;
        p->city_end = s;
        p->length = l;
        p->next = citys[e].head;
        citys[e].head = p;
    }
    maxt[c1] = citys[c1].teams;
    minl[c1] = 0;
    s = c1;
    while(s != c2)
    {
        Min = inf;
        e = s;
        fina[e] = 0;
        p = citys[e].head;
        while(p != NULL)
        {
            if(fina[p->city_end])
            {
                if(minl[p->city_end] > minl[e] + p->length)
                {
                    minl[p->city_end] = minl[e] + p->length;
                    ps[p->city_end] = ps[e];
                    maxt[p->city_end] = maxt[e] + citys[p->city_end].teams;
                }
                else if(minl[p->city_end] == minl[e] + p->length)
                {
                    maxt[p->city_end] = max(maxt[p->city_end], maxt[e] + citys[p->city_end].teams);
                    ps[p->city_end] += ps[e];
                }
            }
            p = p->next;
        }
        for (int i = 0; i < n; ++i)
        {
            if (fina[i] && minl[i] < Min)
            {
                Min = minl[i];
                s = i;
            }
        }
    }
    cout << ps[c2] << " " << maxt[c2];
    return 0;
}