#include<iostream>
using namespace std;

int main()
{
    int n, post[35], in[35], i;
    int s1[35], e1[35], s2[35], e2[35], front, end;
    cin >> n;
    for (i = 0; i < n; ++i)
        cin >> post[i];
    for (i = 0; i < n; ++i)
        cin >> in[i];
    front = -1, end = 0;
    s1[end] = s2[end] = 0;
    e1[end] = e2[end] = n-1;
    while(end != front)
    {
        if (front != -1)
            cout << " ";
        cout << post[e1[++front]];
        for (i = s2[front]; i <= e2[front]; ++i)
            if (in[i] == post[e1[front]])
                break;
        if (s1[front] != e1[front])
        {
            if (i > s2[front])
            {
                s1[++end] = s1[front];
                e1[end] = s1[front]+i-s2[front]-1;
                s2[end] = s2[front];
                e2[end] = i-1;
            }
            if (i < e2[front])
            {
                s1[++end] = s1[front]+i-s2[front];
                e1[end] = e1[front]-1;
                s2[end] = i+1;
                e2[end] = e2[front];
            }
        } 
    }
    return 0;
}
