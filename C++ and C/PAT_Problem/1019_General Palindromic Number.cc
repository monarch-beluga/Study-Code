#include<iostream>
using namespace std;

int main()
{
    int n, b, sum = 0, a = 0;
    int arr[100];
    cin >> n >> b;
    for (int i = n; i > 0; i /= b)
    {
        arr[a] = i % b;
        sum = sum*b + arr[a++];
    }
    if (sum == n)
        printf("Yes\n");
    else
        printf("No\n");
    for (int i = a-1; i > 0; --i)
        cout << arr[i] << " ";
    if (sum == 0)
        cout << 0;
    else
        cout << arr[0];
    return 0;
}
