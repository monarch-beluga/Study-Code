#include<stdio.h>		//从小到大
int main()
{
	int t,i,j,x,temp[7];
	int swap = 1;
	for(i=0;i<7;i++)
		scanf("%d",&temp[i]);
	for(i=0;i<6;i++)
	{
		j=i;
		for(t=i+1;t<7;t++)
			j=temp[t]<temp[j]?t:j;
		if(j!=i)		//减少步骤
			x=temp[i],temp[i]=temp[j],temp[j]=x;
	}
	for(i=0;i<7;i++)
		printf("%d ",temp[i]);
	return 0;
} 