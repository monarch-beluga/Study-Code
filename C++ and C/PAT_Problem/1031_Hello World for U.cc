#include<iostream>
using namespace std;

int main()
{
    int line, n2, n;
    string s;
    cin >> s;
    n = s.size();
    line = (n+2)/3-1;
    n2 = n - 2*line;
    for (int i = 0; i < line; ++i)
    {
        cout << s[i];
        for (int j = 0; j < n2-2; ++j)
            cout << " ";
        cout << s[n-i-1] << endl;
    }
    for (int i = line; i < line+n2; ++i)
        cout << s[i];
    return 0;
}
