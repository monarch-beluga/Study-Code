#include<iostream>
using namespace std;
#define inf 9999999
#include<vector>

typedef struct road
{
    int e_city, cost, l;
    road *next;
}*r;

int n, m, s, d, min_l = inf, min_cost = inf, *vis;
r *cs;
vector<int> path, minpath;

void dfs(int v, int l, int cost)
{
    vis[v] = 0;
    path.push_back(v);
    if (l > min_l)
        return;
    if (v == d)
    {
        if (l < min_l || (l == min_l&&cost < min_cost))
        {
            min_l = l;
            minpath = path;
            min_cost = cost;
        }
        return;
    }
    r p = cs[v];
    int a;
    while(p)
    {
        a = p->e_city;
        if(vis[a])
        {
            dfs(a, l+p->l, cost+p->cost);
            vis[a] = 1;
            path.pop_back();
        }
        p = p->next;
    }
}

int main()
{
    int c1, c2, distance, cost;
    r p;
    cin >> n >> m >> s >> d;
    cs = new r[n];
    vis = new int[n];
    for (int i = 0; i < n; ++i)
    {
        cs[i] = NULL;
        vis[i] = 1;
    }
    for (int i = 0; i < m; ++i)
    {
        cin >> c1 >> c2 >> distance >> cost;
        p = new road;
        p->e_city = c2;
        p->l = distance;
        p->cost = cost;
        p->next = cs[c1];
        cs[c1] = p;
        p = new road;
        p->e_city = c1;
        p->l = distance;
        p->cost = cost;
        p->next = cs[c2];
        cs[c2] = p;
    }
    dfs(s, 0, 0);
    for (int i = 0; i < (int)minpath.size(); ++i)
        cout << minpath[i] << " ";
    cout << min_l << " " << min_cost;
    return 0;
}
