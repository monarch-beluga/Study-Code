#include <stdio.h>

long Ack(int m, int n)
{
    if (m == 0)
        return (long)(n+1);
    else if (n == 0)
        return Ack(m-1, 1);
    else
        return Ack(m-1, Ack(m, n-1));
}

int main()
{
    int m, n;
    scanf("%d%d", &m, &n);
    printf("%ld\n", Ack(m, n));
    return 0;
}


