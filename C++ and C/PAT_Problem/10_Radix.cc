#include<iostream>
#include<string>
#include<cmath>
using namespace std;
int charToInt(char ch)
{
    if(ch >= 'a')
        return ch-'a'+10;
    else
        return ch-'0';
}
long long strToInt(string s, long long redix)
{
    unsigned long long num1 = 0;
    int len = s.size();
    for(int i = 0; i < len; i++)
        num1 = num1*redix+charToInt(s[i]);
    if(num1 >= 0)
        return num1;
    else
        return -1;
}
int max_bit(string s)
{
    int n_max = -1;
    int len = s.size();
    for(int i = 0; i < len; i++)
        if(charToInt(s[i]) > n_max)
            n_max = charToInt(s[i]);
    return n_max+1;
}
int main()
{
    string n[2];
    int tag1, tag2;
    long long redix1, redix2, num[2], redix, mid;
    cin >> n[0] >> n[1] >> tag1 >> redix;
    --tag1;
    if(tag1)
        tag2=0;
    else
        tag2=1;
    num[tag1] = strToInt(n[tag1], redix);
    if(n[0] == n[2])
    {
        cout << redix;
        return 0;
    }
    redix1 = (long long)pow(num[tag1]/(double)charToInt(n[tag2][0]), 1.0/(n[tag2].size()-1));
    redix2 = max_bit(n[tag2]);
    if(redix2 < 2)
        redix2 = 2;
    mid = redix1;
    while(redix2 <= redix1)
    {
        num[tag2] = strToInt(n[tag2], mid);
        if(num[0] == num[1])
        {
            if(mid >= max_bit(n[tag2]))
                cout << mid;
            else
                break;
            return 0;
        }
        else if(num[tag1] < num[tag2] || num[tag2]==-1)
            redix1 = mid-1;
        else
            redix2 = mid+1;
        mid = (redix1+redix2)/2;
    }
    cout << "Impossible";
    return 0;
}