#include <stdio.h>
int main()
{
	int a[5][6],i,j,b[20],t,x,c,d;
	for(i = 0;i<5;i++)
		for(j = 0;j<6;j++)
			if(i == 0||i == 4||j == 0||j == 5)
				scanf("%d",&a[i][j]);
	for(i = 0;i<5;i++)
	{
		for(j = 0;j<6;j++)
		{
			if(i == 0||i == 4||j == 0||j == 5)
				printf("%-3d",a[i][j]);
			else printf("   ");
		}
		printf("\n");
	}
	i = 0,j = 0;
	b[0] = a[i][j];
	for(t = 0,x=1;x<20;x++)
	{
		switch(t%4)
		{
			case 0:j++;break;
			case 1:i++;break;
			case 2:j--;break;
			case 3:i--;break;
		}
		if(j<6&&i<5&&j>-1&&i>-1)
			b[x] = a[i][j];
		else
		{
			switch(t%4)
			{
				case 0:j--;break;
				case 1:i--;break;
				case 2:j++;break;
				case 3:i++;break;
			}
			x--;
			t++;
		}
	}
	x = b[0]+b[1]+b[2];
	for(i = 0;i<18;i++)
	{
		t = b[i]+b[i+1]+b[i+2];
		if(x<t) x = t;
	} 
	for(c = 0;c<17;c++)
		if(b[c]+b[c+1]+b[c+2] == x) break;
	i = 0,j = 0;
	for(t = 0,x=1;x<c+3;x++)
	{
		switch(t%4)
		{
			case 0:j++;break;
			case 1:i++;break;
			case 2:j--;break;
			case 3:i--;break;
		}
		if(j<6&&i<5&&j>-1&&i>-1)
		{
			if(x>=c)printf("%d,%d\n",i,j);
		}
		else
		{
			switch(t%4)
			{
				case 0:j--;break;
				case 1:i--;break;
				case 2:j++;break;
				case 3:i++;break;
			}
			x--;
			t++;
		}

	}
	return 0;
}