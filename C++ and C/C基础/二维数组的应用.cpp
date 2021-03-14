#include<stdio.h>			//奇数阶数组魔法
int main()
{
	int a[15][15];
	static int x,y,i,n;
	while(n%2==0||n>15)
	{
		printf("请输入一个奇数:");
		scanf("%d",&n);
	}
	y=(n-1)/2;
	for(i=1;i<=n*n;i++)
	{
		a[x][y]=i;
		if(i%n==0) x++;
		else y++,x--;
		if(x<0)x=n-1;
		if(y>n-1)y=0;
	}
	for(x=0;x<n;x++)
	{
		for(y=0;y<n;y++)
			printf("%-5d",a[x][y]);
		printf("\n");
	}
	return 0;
}