#include<iostream>
using namespace std;
#define Max 100010

int main()
{
    int w1, w2, n, address, next, ll[Max][2], p;
    char data;
    cin >> w1 >> w2 >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> address >> data >> next;
        ll[address][0] = next;
        ll[address][1] = 0;
    }
    for(p = w1; p != -1; p = ll[p][0])
        ++ll[p][1];
    for (p = w2; p != -1; p = ll[p][0])
        if (++ll[p][1] == 2)
        {
            printf("%05d", p);
            return 0;
        }
    cout << -1;
    return 0;
}
