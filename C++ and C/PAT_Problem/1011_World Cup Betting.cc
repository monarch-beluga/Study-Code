#include<iostream>
using namespace std;
int main()
{
    int iMax = 0;
    float Max = -1, t, profit = 1;
    char p[3] = {'W', 'T', 'L'};
    for (int i = 0; i < 3; ++i, Max = -1)
    {
        for (int j = 0; j < 3; ++j)
        {
            cin >> t;
            if (Max < t)
                Max = t, iMax = j;
        }
        profit *= Max;
        cout << p[iMax] << " ";
    }
    printf("%.2f", (profit*0.65-1)*2);
    return 0;
}