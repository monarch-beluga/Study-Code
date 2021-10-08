#include<stdio.h>			//从大到小
int main()
{
	int t,i,j,temp[7];
	int swap = 1;
	for(i=0;i<7;i++)
		scanf("%d",&temp[i]);
	for(t=6;t>0&&swap;t--)
		for(i=0,swap = 0;i<t;i++)
			if(temp[i]<temp[i+1])
				j=temp[i],temp[i]=temp[i+1],temp[i+1]=j,swap=1;
	for(i=0;i<7;i++)
		printf("%d ",temp[i]);
	return 0;
} 