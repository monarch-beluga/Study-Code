#include<iostream>
using namespace std;
#include<vector>


void DFS(int k, int *vis, vector<int> *cs)
{
    ++vis[k];
    for (int i = 0; i < (int)cs[k].size(); ++i)
        if(vis[cs[k][i]] != vis[0])
            DFS(cs[k][i], vis, cs);
}

int DFScount(int n, int k, int *vis, vector<int> *cs)
{
    int count = -1;
    ++vis[k];
    for (int i = 1; i <= n; ++i)
        if (vis[i] != vis[0])
        {
            ++count;
            DFS(i, vis, cs);
        }
    return count;
}

int main()
{
    int n, m, k, s, e;
    cin >> n >> m >> k;
    vector<int> *cs = new vector<int>[n+1];
    int  *vis = new int[n+1];
    for (int i = 0; i < m; ++i)
    {
        cin >> s >> e;
        cs[s].push_back(e);
        cs[e].push_back(s);
    }
    for (int i = 0; i < k; ++i)
    {
        cin >> s;
        ++vis[0];
        cout << DFScount(n ,s, vis, cs) << endl;
    }
    return 0;
}
