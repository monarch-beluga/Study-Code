#include<iostream>
using namespace std;
#include<vector>
#include<algorithm>

typedef struct rank
{
    string reg_n;
    int score, ln;
}R;
bool cmp(R a, R b)
{
    if (a.score != b.score)
        return a.score > b.score;
    else 
        return a.reg_n < b.reg_n;
}

int main()
{
    int n, k, ln;
    R *p;
    vector<R> rs;
    cin >> n;
    int fr = 0, *lr = new int[n], fpre = -1, *lpre = new int[n], *lnc = new int[n];
    for (int i = 0; i < n; ++i)
    {
        cin >> k;
        lnc[i] = lr[i] = 0;
        lpre[i] = -1;
        for (int j = 0; j < k; ++j)
        {
            p = new R;
            cin >> p->reg_n >> p->score;
            p->ln = i;
            rs.push_back(*p);
        }
    }
    k = rs.size();
    sort(rs.begin(), rs.end(), cmp);
    printf("%d\n", k);
    for (int i = 0; i < (int)rs.size(); ++i)
    {
        ln = rs[i].ln;
        ++lnc[ln];
        if (rs[i].score != fpre)
            fr = i+1, fpre = rs[i].score;
        if (rs[i].score != lpre[ln])
            lr[ln] = lnc[ln], lpre[ln] = rs[i].score;
        cout << rs[i].reg_n;
        printf(" %d %d %d\n", fr, ln+1, lr[ln]);
    }
    return 0;
}
