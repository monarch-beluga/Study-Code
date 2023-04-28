#include<iostream>
using namespace std;

class Point
{
public:
    int x;
    int y;
};


int main()
{
    int n, sep;
    int x_diff, y_diff;
    Point s, e;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        sep = 0;
        cin >> s.x >> s.y >> e.x >> e.y;
        y_diff = e.y - s.y;
        if (y_diff < 0)
            cout << -1 << endl;
        else
        {
            sep += y_diff;
            s.x += y_diff;
            x_diff = e.x - s.x;
            if (x_diff > 0)
                cout << -1 << endl;
            else
            {
                sep -= x_diff;
                cout << sep << endl;
            }
        }
    }
    return 0;
}
