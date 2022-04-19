#include<iostream>
using namespace std;

int main()
{
    #if ONLINE_JUDGE
    #else
    freopen("input.txt", "r", stdin);
    #endif
    
    return 0;
}