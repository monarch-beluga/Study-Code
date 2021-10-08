#include<stdio.h>
int main()
{
	int a[100][100];
	int k,n,x,y,t=0;
	scanf("%d",&n);
	for(k=0;k<=n;k++)
		a[0][k]=1,a[k][n]=1,a[n+1][k]=1;
	for(x=1;x<=n;x++)
		for(y=0;y<n;y++)
			a[x][y]=0;
	x=1,y=0;
	a[x][y]=1;
	for(k=2;k<=n*n;)
	{
		switch(t%4)
		{
			case 0:x++;break;
			case 1:y++;break;
			case 2:x--;break;
			case 3:y--;break;
		}
		if(a[x][y]==0) a[x][y]=k,k++;
		else
		{
			switch(t%4)
			{
				case 0:x--;break;
				case 1:y--;break;
				case 2:x++;break;
				case 3:y++;break;
			}
			t++;
		}
	}
	for(x=1;x<=n;x++)
	{
		for(y=0;y<n;y++)
			printf("%-4d",a[x][y]);
		printf("\n");
	}
}