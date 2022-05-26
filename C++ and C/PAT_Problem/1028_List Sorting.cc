#include<iostream>
using namespace std;
#include<algorithm>

typedef struct student
{
    string inf[3];
    int grade;
}S;

int n, c;
bool cmp(S a, S b)
{
    if (a.inf[c-1] != b.inf[c-1])
        return a.inf[c-1] < b.inf[c-1];
    else
        return a.inf[0] < b.inf[0];
}

int main()
{
    cin >> n >> c;
    S *ss = new student[n];
    for (int i = 0; i < n; ++i)
    {
        cin >> ss[i].inf[0] >> ss[i].inf[1] >> ss[i].grade;
        ss[i].inf[2] = (char)ss[i].grade;
    }
    sort(ss, ss+n, cmp);
    for (int i = 0; i < n; ++i)
        cout << ss[i].inf[0] << " " <<  ss[i].inf[1] << " " << ss[i].grade << endl;
    return 0;
}
