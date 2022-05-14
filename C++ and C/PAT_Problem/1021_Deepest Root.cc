#include<iostream>
using namespace std;
#include<vector>

vector<int> *graph, droot;
int maxl, *vis, count = 0, n, *fina, flag;

void dfs(int v, int l)
{
    vis[v] = 0;
    if(l == maxl)
        droot.push_back(v);
    if (l > maxl)
    {
        maxl = l;
        droot.clear();
        droot.push_back(v);
    }
    int p;
    for (int i = 0; i < (int)graph[v].size(); ++i)
    {
        p = graph[v][i];
        if (vis[p])
        {
            dfs(p, l+1);
            if (!flag)
                vis[p] = 1;
        }
    }
        
}

void dfsCount(int v)
{
    droot.clear();
    maxl = 0;
    for (int i = 1; i < n; ++i)
        vis[i] = 1;
    if (flag)
        for (int i = 1; i < n; ++i)
        {
            fina[i] = 1;
            if (vis[i])
            {
                ++count;
                dfs(i, 0);
            }
        }
    else
        dfs(v, 0);
    for (int i = 0; i < (int)droot.size(); ++i)
            fina[droot[i]] = 0;
}

int main()
{
    int s, e;
    cin >> n;
    ++n;
    vis = new int[n];
    fina = new int[n];
    graph = new vector<int>[n];
    for (int i = 1; i < n-1; ++i)
    {
        cin >> s >> e;
        graph[s].push_back(e);
        graph[e].push_back(s);
    }
    flag = 1;
    dfsCount(1);
    if (count == 1)
    {
        flag = 0;
        dfsCount(droot[0]);
        for (int i = 1; i < n; ++i)
            if (!fina[i])
                cout << i << endl;
    }
    else
        printf("Error: %d components", count);
    return 0;
}
