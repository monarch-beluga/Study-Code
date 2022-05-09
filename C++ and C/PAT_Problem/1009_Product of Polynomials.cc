#include<iostream>
using namespace std;
#define Max 2010
int main()
{
    float a2[Max] = {0}, a1[11], a;
    int k = 0, k1, k2, n, n1[11], ni;
    cin >> k1;
    for (int i = 0; i < k1; ++i)
        cin >> n1[i] >> a1[i];
    cin >> k2;
    for (int i = 0; i < k2; ++i)
    {
        cin >> n >> a;
        for(int j = 0; j < k1; ++j)
        {
            ni = n + n1[j];
            if (a2[ni] != 0)
                k--;
            a2[ni] += a1[j] * a;
            if (a2[ni] != 0)
                k++;
        }
    }
    cout << k;
    for (int i = Max-1; i >= 0; --i)
        if (a2[i] != 0)
            printf(" %d %.1f", i, a2[i]);
    return 0;
}
 