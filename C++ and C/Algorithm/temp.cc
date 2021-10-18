#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;

int main()
{
        #if ONLINE_JUDGE
#else
    freopen("input.txt", "r", stdin);
#endif
    int k, n, pre;
    int sum[3][3] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    int c1;
    cin >> k;
    cin >> n;
    if(n < 0)
        c1 = 0;
    else
        c1 = 1;
    sum[0][0] = sum[c1][0] = sum[0][1] = sum[c1][1] = n;
    for(int i = 1; i < k; i++)
    {
        pre = n;
        cin >> n;
        if(n*pre < 0)
        {
            if(n < 0)
            {
                sum[0][2] = sum[c1][2] = pre;
                if(c1 == 2)
                {
                    c1 = sum[0][0] > sum[1][0]?(sum[0][0]>=sum[2][0]?0:2):(sum[1][0]>=sum[2][0]?1:2);
                    if(c1 == 2)
                    {
                        for(int j = 0; j < 3; j++)
                            sum[0][j] = sum[1][j] = sum[2][j];
                    }
                    sum[2][0] = 0;
                    c1 = 2;
                }
            }
            else 
            {
                if(c1 == 0)
                    sum[0][0] = 0;
                c1++;
                sum[c1][1] = sum[0][1] = n;
            }
        }
        sum[0][0] += n;
        if(n > 0)
            sum[c1][0] += n;
    }
    if(c1 == 0)
        cout << 0 << " " << sum[0][1] << " " << n;
    else
    {
        c1 = sum[0][0] > sum[1][0]?(sum[0][0]>=sum[2][0]?0:2):(sum[1][0]>=sum[2][0]?1:2);
        cout << sum[c1][0] << " " << sum[c1][1] << " " << sum[c1][2];
    }
    return 0;
}
