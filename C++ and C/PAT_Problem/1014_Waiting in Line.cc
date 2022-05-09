#include<iostream>
using namespace std;

typedef struct queue
{
      int *data, front;
}Q;

int main()
{
    int n, m, k, q, tmix, p;
    cin >> n >> m >> k >> q;
    Q *qs = new queue[n];
    int *qt = new int[k], *qe = new int[k];
    for (int i = 0; i < n; ++i)
    {
        qs[i].front = 0;
        qs[i].data = new int[m];
        qs[i].data[m-1] = 480;
    }
    for (int i = 0; i < k; ++i)
    {
        cin >> qe[i];
        if (i < n*m)
            tmix = i%n;
        else
        {
            tmix = 0;
            for (int j = 1; j < n; ++j)
                if (qs[j].data[qs[j].front] < qs[tmix].data[qs[tmix].front])
                    tmix = j;
        }
        qt[i] = qs[tmix].data[(qs[tmix].front+m-1)%m];
        qs[tmix].data[qs[tmix].front] = qt[i] + qe[i];
        qs[tmix].front = (qs[tmix].front+1)%m;
    }
    for (int i = 0; i < q; ++i)
    {
        cin >> p;
        --p;
        if (qt[p] < 1020)
            printf("%02d:%02d\n", (qt[p]+qe[p])/60, (qt[p]+qe[p])%60);
        else
            cout << "Sorry" << endl;
    }
    return 0;
}
