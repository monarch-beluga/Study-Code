#include<iostream>
using namespace std;
#include<algorithm>
typedef struct Student
{
    int id, score[4], res, c, cmp;
}S;
bool cmp(S a, S b)
{
    return a.score[a.cmp] > b.score[b.cmp];
}
void getRes(S *ss, int n, int c)
{
    int j = 0;
    sort(ss, ss+n, cmp);
    for (int i = 0; i < n; ++i)
    {
        if (ss[i].score[c] < ss[j].score[c])
            j = i;
        if (ss[i].res > j+1)
        {
            ss[i].res = j+1;
            ss[i].c = c;
        }
        ++ss[i].cmp;
    }
}

int main()
{
    char cs[4] = {'A', 'C', 'M', 'E'};
    int n, m, sum = 0, id, flag = -1;
    cin >> n >> m;
    S *ss = new S[n];
    for (int i = 0; i < n; ++i, sum = 0)
    {
        cin >> ss[i].id;
        for (int j = 1; j < 4; ++j)
        {
            cin >> ss[i].score[j];
            sum += ss[i].score[j];
        }
        ss[i].score[0] = sum / 3;
        ss[i].res = 2010;
        ss[i].cmp = 0;
    }
    for (int i = 0; i < 4; ++i)
        getRes(ss, n, i);
    for (int i = 0; i < m; ++i, flag=-1)
    {
        if (i)
            cout << endl;
        cin >> id;
        for (int j = 0; j < n && flag==-1; ++j)
            if (ss[j].id == id)
                flag = j;
        if (flag != -1)
            printf("%d %c", ss[flag].res, cs[ss[flag].c]);
        else
            cout << "N/A";
    }
    return 0;
}
