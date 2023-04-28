#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int num;
    int a, b;
    cin >> num;
    if (num < 0)
    {
        a = num%10;
        num /= 10;
        b = num%10;
        num = num/10*10 + max(a, b);
    }
    cout << num;
    return 0;
}
