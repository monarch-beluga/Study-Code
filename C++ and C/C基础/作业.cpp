#include<stdio.h>
int fun(int n)
{
	int i;
	if(n == 0||n==1) return 1;
	if(n == 2) return 0;
	for(i = 2;i<n;i++)
	if(n%i == 0) return 1;
	return 0;
}
int main()
{
	int i,j,n,m = 0,x;
	for(x = 1;x<=1000;x++)
	{
		n = 0,j = 1,i = x;
		for(;i>0;i/=10)
		{
			n += i%10;
			if(fun(i%10))
			{
				j = 0;
				break;
			}
		}
		if(!fun(x)&&!fun(n)&&j == 1)
		{
			m++;
			printf("%-5d",x);
			if(m%5==0) putchar('\n');
		}
	}
	return 0;
}