#include<iostream>
using namespace std;

int main()
{
    int arr[21] = {0}, n = 0, s = 0, flag = 1, count[10] = {0};
    char ch;
    while((ch = cin.get()) != '\n')
    {
        arr[++n] = ch - '0';
        ++count[arr[n]];
    }
    for (int i = n; i > 0; --i)
    {
        s = arr[i] * 2 + s;
        arr[i] = s % 10;
        s = s / 10;
        --count[arr[i]];
    }
    arr[0] += s;
    for (int i = 0; i < 10; ++i)
        if (count[i])
            flag = 0;
    if (!arr[0] && flag)
        printf("Yes\n");
    else
        printf("No\n");
    if (arr[0])
        cout << arr[0];
    for (int i = 1; i <= n; ++i)
        cout << arr[i];
    return 0;
}
