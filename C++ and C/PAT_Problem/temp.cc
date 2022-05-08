#include<iostream>
using namespace std;
#include<algorithm>
#include<vector>

typedef struct record
{
    string name, type, month;
    int time;
}Rc;
bool cmp(Rc a, Rc b)
{
    if(a.name != b.name)
        return a.name < b.name;
    else
        return a.time < b.time;
}

int main()
{
    #if ONLINE_JUDGE
    #else
    freopen("input.txt", "r", stdin);
    #endif
    int tolls[24], n, d, h, m, td = 0;
    for (int i = 0; i < 24; td+=tolls[i++])
        cin >> tolls[i];
    cin >> n;
    Rc *rs = new record[n];
    for (int i = 0; i < n; ++i)
    {
        cin >> rs[i].name;
        scanf("%d:%d:%d:%d", &rs[i].month, &d, &h, &m);
        cin >> rs[i].type;
        rs[i].time = d*10000+h*100+m;
    }
    sort(rs, rs+n, cmp);
    int te, ts = rs[0].time;
    for (int i = 0; i < n; ++i)
    {
        
    }
    return 0;
}
