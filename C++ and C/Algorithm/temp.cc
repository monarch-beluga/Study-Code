#include<iostream>
using namespace std;

int main()
{
#if ONLINE_JUDGE
#else
freopen("input.txt", "r", stdin);
#endif
    char ch;
    int sum[3], len, c, t;
    cin >> t;
    for(int te = 0; te < t; te++)
    {
        sum[0] = sum[1] = sum[2] = 0;
        len = -1;
        cin >> c;
        for(int i = 0; i < c; ++i)
        {
            cin >> ch;
            sum[ch-'a']++;
            if((sum[0] == 0 && (sum[1] > sum[0] || sum[2] > sum[0]))||(sum[1] > sum[0] && sum[2] > sum[0]))
                sum[0] = sum[1] = sum[2] = 0;
            if(sum[0] > sum[1] && sum[0] > sum[2] && sum[0] > 1)
            {
                if((sum[0]+sum[1]+sum[2])<len||len==-1)
                    len = sum[0]+sum[1]+sum[2];
                sum[0] = 1;
                sum[1] = sum[2] = 0;
            }
        }
        cout << len << endl;
    }
    return 0;
}