#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int *arr = new int[n];
    for (int i = 0; i < n; ++i)
        cin >> arr[i];
    sort(arr, arr+n);
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
    delete[] arr;
    return 0;
}
