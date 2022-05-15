#include<iostream>
using namespace std;
#include<string>
#include<algorithm>

typedef struct book
{
    string infor[6];
}*B;
bool cmp(book a, book b)
{
    return a.infor[0] < b.infor[0];
}

int main()
{
    int n, m, q, flag;
    string s;
    scanf("%d\n", &n);
    B bs = new book[n];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < 6; ++j)
            getline(cin, bs[i].infor[j]);
    sort(bs, bs+n, cmp);
    cin >> m;
    for (int i = 0; i < m; ++i)
    {
        flag = 1;
        scanf("%d: ", &q);
        getline(cin, s);
        cout << q << ": "+s << endl;
        for (int j = 0; j < n; ++j)
        {
            if ((q != 3 && s == bs[j].infor[q]) || (q == 3 && bs[j].infor[3].find(s) != s.npos))
            {
                cout << bs[j].infor[0] << endl;
                flag = 0;
            }
        }
        if (flag)
            cout << "Not Found" << endl; 
    }
    return 0;
}
