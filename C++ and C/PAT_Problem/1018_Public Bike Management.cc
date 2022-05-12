/*
深度优先+回溯 求加权最短路径
*/
#include<iostream>
using namespace std;
#include<vector>
#define inf 9999999

typedef struct road
{
    int l, e;
    road *next;
}R;

typedef struct station
{
    int bs;
    road *head;
}ST;

int Cmax, n, Sp, m;
vector<int> minpath, path;
int *fina, minl = inf, minsent = inf, minback = inf;
ST *ss;

void dfs(int s, int l, int sent, int back)
{
    fina[s] = 0;
    path.push_back(s);
    if(l > minl) return;
    if(s == Sp)
    {
        if(l < minl)
            minl=l, minsent=sent, minback=back, minpath=path;
        else if(l == minl&&minsent > sent)
            minsent=sent, minback=back, minpath=path;
        else if(l == minl&&minsent == sent&&minback > back)
            minback=back, minpath=path;
        return;
    }
    R *p = ss[s].head;
    int v;
    while(p != NULL)
    {
        v = p->e;
        if (fina[v])
        {
            if(back + ss[v].bs <= Cmax/2)
                dfs(v, l+p->l, sent + Cmax/2 - ss[v].bs - back, 0);
            else
                dfs(v, l+p->l, sent, back + ss[v].bs - Cmax/2);
            fina[v] = 1;
            path.pop_back();
        }
        p = p->next;
    }
}

int main()
{
    int s, e, l;
    R *p;
    cin >> Cmax >> n >> Sp >> m;
    ++n;
    ss = new station[n];
    fina = new int [n];
    ss[0].head = NULL;
    for (int i = 1; i < n; ++i)
    {
        cin >> ss[i].bs;
        ss[i].head = NULL;
        fina[i] = 1;
    }
    for (int i = 0; i < m; ++i)
    {
        cin >> s >> e >> l;
        p = new road;
        p->l = l;
        p->e = e;
        p->next = ss[s].head;
        ss[s].head = p;
        p = new road;
        p->l = l;
        p->e = s;
        p->next = ss[e].head;
        ss[e].head = p;
    }
    dfs(0, 0, 0, 0);
    printf("%d %d", minsent, 0);
    for (int i = 1; i < (int)minpath.size(); ++i)
        printf("->%d", minpath[i]);
    printf(" %d", minback);
    return 0;
}
