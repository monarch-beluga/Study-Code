#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int n, x, y;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> x >> y;
        x = abs(x);
        y = abs(y);
        if (x == y)
            cout << x*2 << endl;
        else
            cout << max(x, y)*2-1 << endl;
    }
    
    return 0;
}
