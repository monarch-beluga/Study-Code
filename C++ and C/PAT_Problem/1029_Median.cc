#include<iostream>
using namespace std;
#include<algorithm>
#include<vector>

int main()
{
    vector<int> arr;
    int n1, n2, t;
    cin >> n1;
    for (int i = 0; i < n1; ++i)
    {
        cin >> t;
        arr.push_back(t);
    }
    cin >> n2;
    for (int i = 0; i < n2; ++i)
    {
        cin >> t;
        arr.push_back(t);
    }
    n1+=n2;
    sort(arr.begin(), arr.end());
    if (n1 % 2)
        cout << arr[n1/2];
    else
        cout << arr[n1/2-1];
    return 0;
}
