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
    int k, n = -1, pre, flag = 1, i = 0;
    int sum[3][3] = {{0}, {0}, {0}};
    int c1, c2;
    cin >> k;
    while(n<0&&i<k)
    {
        pre = n;
        if(!(cin >> n))
            break;
        if(i == 0)
            sum[0][1] = n;
        i++;
    }
    if(n<0)
        cout << 0 << " " << sum[0][1] << " " << n;
    else
    {
        c1 = 1;
        if (pre != 0)
            pre = n;
        sum[0][0] = sum[0][1] = sum[c1][0] = sum[c1][1] = pre;
        while(i<k)
        {
            pre = n;
            if(!(cin >> n))
                break;
            if(n*flag<0)
            {
                if(n<0)
                {
                    sum[0][2] = sum[c1][2] = pre;
                    if(c1 == 1)
                        c1++;
                    else
                    {
                        c2 = sum[0][0] > sum[1][0]?(sum[0][0]>=sum[2][0]?0:2):(sum[1][0]>=sum[2][0]?1:2);
                        for(int j = 0; j < 3; j++)
                            sum[0][j] = sum[1][j] = sum[c2][j];
                    }
                }
                else
                {
                    if(pre == 0)
                        sum[c1][1] = pre;
                    else
                        sum[c1][1] = n;
                    sum[c1][0] = 0;
                }
                flag *= -1;
            }
            sum[0][0] += n;
            if(n > 0)
                sum[c1][0] += n;
            i++;
            // cout << sum[2][0] << endl;
        }
        if(flag > 0)
            sum[0][2] = sum[c1][2] = n;
        c2 = sum[0][0] > sum[1][0]?(sum[0][0]>=sum[2][0]?0:2):(sum[1][0]>=sum[2][0]?1:2);
        // cout << c2 << " " << endl;
        cout << sum[c2][0] << " " << sum[c2][1] << " " << sum[c2][2];
    }
    return 0;
}
