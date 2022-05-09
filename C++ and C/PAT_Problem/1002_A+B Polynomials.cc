/*
方法一：
	使用哈希表
*/

#include<iostream>
#include<cmath>
using namespace std;

int addArr(float arr[], int n)
{
    int k, a;
    float t;
    cin >> k;
    for(int i = 0; i < k; i++)
    {
        cin >> a >> t;
        if (arr[a] != 0)
            n--;
        arr[a] += t;
        if(arr[a] != 0)
            n++;
    }
    return n;
}

int main()
{
    float arr[1010] = {0};
    int n = 0;
    n = addArr(arr, n);
    n = addArr(arr, n);
    printf("%d", n);
    for(int i = 1009; i >= 0; i--)
        if(arr[i] != 0)
            printf(" %d %.1f", i, arr[i]);
    return 0;
}

/*
方法二：
	使用合并链表的方法
*/

#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int k1, k2, N1[10], N2[10], N3[20];
    double a1[10], a2[10], a3[20];
    int n1, n2 , n3;
    cin >> k1;
    for(int i = 0; i < k1; i++)
        cin >> N1[i] >> a1[i];
    cin >> k2;
    for(int i = 0; i < k2; i++)
        cin >> N2[i] >> a2[i];
    n1 = n2 = n3 = 0;
    while(n1<k1&&n2<k2)
    {
        if(N1[n1] > N2[n2])
        {
            N3[n3]=N1[n1];
            a3[n3++] = a1[n1++];
        }
        else if(N1[n1] == N2[n2])
        {
            N3[n3]=N1[n1];
            a3[n3] = a1[n1++]+a2[n2++];
            if(a3[n3]!=0)
                n3++;
        }
        else
        {
            N3[n3]=N2[n2];
            a3[n3++] = a2[n2++];
        }
    }
    if(n1 == k1)
        for(int i = n2; i < k2; i++)
        {
            N3[n3]=N2[n2];
            a3[n3++] = a2[n2++];
        }
    else
        for(int i = n1; i < k1; i++)
        {
            N3[n3]=N1[n1];
            a3[n3++] = a1[n1++];
        }
    cout << n3;
    for(int i = 0; i < n3; i++)
        printf(" %d %.1f", N3[i], a3[i]);
    return 0;
}
