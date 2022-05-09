#include<iostream>
using namespace std;
#include<algorithm>
#include<vector>

typedef struct record
{
    string name;
    int d, h, m, type, month;
}Rc;
bool cmp(Rc a, Rc b)
{
    if(a.name != b.name)
        return a.name < b.name;
    else
        return a.d*10000+a.h*100+a.m < b.d*10000+b.h*100+b.m;
}

int main()
{
    int tolls[24], n, h, m;
    string s;
    for (int i = 0; i < 24; ++i)
        cin >> tolls[i];
    cin >> n;
    Rc *rs = new record[n];
    for (int i = 0; i < n; ++i)
    {
        cin >> rs[i].name;
        scanf("%d:%d:%d:%d", &rs[i].month, &rs[i].d, &rs[i].h, &rs[i].m);
        cin >> s;
        if (s == "on-line")
            rs[i].type = 1;
        else
            rs[i].type = 0;
    }
    sort(rs, rs+n, cmp);
    float sum = 0, charge, flag = 1;
    for (int i = 0; i < n; ++i)
    {
        if (!i||rs[i].name!=rs[i-1].name)
        {
            flag = 1;
            if (sum != 0)
                printf("Total amount: $%.2f\n", sum);
            sum = 0;
            continue;
        }
        if(rs[i-1].type&&!rs[i].type)
        {
            if (flag)
            {
                flag = 0;
                cout << rs[i].name;
                printf(" %02d\n", rs[i].month);
            }
            charge = 0;
            h = (rs[i].d-rs[i-1].d)*24 - rs[i-1].h + rs[i].h;
            m = h*60 - rs[i-1].m + rs[i].m;
            for (int j = rs[i-1].h; j < rs[i-1].h+h; ++j)
                charge += tolls[j%24]*60;
            charge -= rs[i-1].m*tolls[rs[i-1].h]-rs[i].m*tolls[rs[i].h];
            charge /= 100;
            printf("%02d:%02d:%02d %02d:%02d:%02d %d $%.2f\n", rs[i-1].d, rs[i-1].h, rs[i-1].m, rs[i].d, rs[i].h, rs[i].m, m, charge);
            sum += charge;
        }
    }
    if (sum != 0)
        printf("Total amount: $%.2f\n", sum);
    return 0;
}
