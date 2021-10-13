#include<iostream>

using namespace std;
typedef struct roads
{
    int city_end;
    int lenth;
    roads* next;
}*r;
typedef struct city
{
    int teams;
    roads* head;
} C;

int main()
{
    #if ONLINE_JUDGE
#else
    freopen("input.txt", "r", stdin);
#endif
    int n, m, c1, c2;
    int a, b, l, k;
    r p;
    cin >> n >> m >> c1 >> c2;
    C *cs = new C[n];
    int *queue = new int[n*2];
//     int v = new int[n];
    int *minD = new int[n];
    int *maxR = new int[n];
    int *path = new int[n];
    for(int i = 0; i < n; i++)
    {
        cin >> cs[i].teams;
        cs[i].head = NULL;
//         v[i] = 0;
        minD[i] = 999999;
        maxR[i] = -1;
        path[i] = 1;
    }
    minD[c1] = 0;
    maxR[c1] = cs[c1].teams;
    for(int i = 0; i < m; i++)
    {
        p = new roads;
        cin >> a >> b >> l;
        p->city_end = b;
        p->lenth = l;
        p->next = cs[a].head;
        cs[a].head = p;
        p = new roads;
        p->city_end = a;
        p->lenth = l;
        p->next = cs[b].head;
        cs[b].head = p;
    }
    a = 0;
    b = 0;
    for(queue[b++]=c1; b > a;)
    {
        k = queue[a++];
        p = cs[k].head;
        while(p!=NULL)
        {
            if(minD[k]+p->lenth < minD[p->city_end])
            {
                minD[p->city_end] = minD[k]+p->lenth;
                if(p->city_end != c2)
                    queue[b++] = p->city_end;
                path[p->city_end] = path[k];
                maxR[p->city_end] = maxR[k] + cs[p->city_end].teams;
            }
            else if((minD[k]+p->lenth == minD[p->city_end]))
            {
                if(maxR[p->city_end] < maxR[k] + cs[p->city_end].teams)
                    maxR[p->city_end] = maxR[k] + cs[p->city_end].teams;
                path[p->city_end] += path[k];
            }

            p = p->next;
        }
    }
    cout << path[c2] << " " << maxR[c2];
    delete []cs, path, maxR, minD, queue;
    return 0;
}