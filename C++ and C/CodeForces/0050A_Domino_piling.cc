#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int n, sum, e, count;
    cin >> n;
    sum = 0;
    count = 0;
    for (int i = 0; i < n; ++i)
    {
        cin >> e;
        sum += e;
        if (sum < 0)
        {
            ++count;
            sum = 0;
        }
    }
    cout << count << endl;
    return 0;
}
