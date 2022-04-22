#include<iostream>
using namespace std;
#include<string>
#include<cmath>

int charToint(char ch)
{
    int num;
    if (ch >= 'a')
        num = ch -'a' + 10;
    else
        num = ch - '0';
    return num;
}

long long stringToint(string s, long long r)
{
    long long num = 0;
    for (int i = 0; i < (int)s.size(); ++i)
        num = num*r + charToint(s[i]);
    return num;
}

long long dichotomy(string s, int num, long long start, long long end)
{
    long long mid = end, n;
    int flag = 0;
    while(!flag && (start <= end))
    {
        mid = (start + end) / 2;
        n = stringToint(s, mid);
        if (n == num)
            flag = 1;
        else if(n > num)
            end = mid-1;
        else
            start = mid+1;
    }
    if (flag)
        return mid;
    else
        return -1;
}

int maxBit(string s)
{
    int n_max = -1;
    for(int i = 0; i < (int)s.size(); i++)
            n_max = max(charToint(s[i]), n_max);
    return n_max+1;
}

int main()
{
    #if ONLINE_JUDGE
    #else
    freopen("input.txt", "r", stdin);
    #endif
    string n1, n2;
    int tag;
    long long radix1, radix2, num1=0, radix3, radix;
    cin >> n1 >> n2 >> tag >> radix1;
    if (tag != 1)
        swap(n1, n2);
    if (n1 == n2)
        cout << radix1;
    else 
    {
        num1 = stringToint(n1, radix1);
        radix3 = (long long)pow(num1/(double)charToint(n2[0]), 1.0/(n2.size()-1));
        radix2 = maxBit(n2);
        radix = dichotomy(n2, num1, radix2, radix3);
        if (radix != -1)
            cout << radix;
        else
            cout << "Impossible";
    }
    return 0;
}
 