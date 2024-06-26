#include<iostream>
using namespace std;
int prime(int a)
{
    if(a == 1) return 0;
    if(a == 2) return 1;
    for (int i = 2; i*i <= a; ++i)
        if (a%i==0)
            return 0;
    return 1;
}
int main()
{
    int n, d, sum;
    cin >> n >> d;
    do
    {
        sum = 0;
        for(int i = n; i > 0; i /= d)
            sum = sum*d + i%d;
        if(prime(n) && prime(sum))
            cout << "Yes" << endl;
        else
            cout << "No" << endl;
        cin >> n >> d;
    }while(n >= 0);
    return 0;
}
