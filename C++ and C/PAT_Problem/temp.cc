#include<iostream>
using namespace std;

int main()
{
    #if ONLINE_JUDGE
    #else
    freopen("input.txt", "r", stdin);
    #endif
    char bits[14] = "0123456789ABC";
    int rgb[3];
    cin >> rgb[0] >> rgb[1] >> rgb[2];
    cout << "#";
    for (int i = 0; i < 3; ++i)
        cout << bits[rgb[i]/13] << bits[rgb[i]%13];
    return 0;
}
