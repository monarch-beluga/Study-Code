#include<stdio.h>
#include <stdafx.h>
int main()
{
	int a,score[5] = {5,4,8,7,8};		//����ĸ�ֵ
	//�������Ԫ���������鳤�ȣ���ô�����Ԫ��Ϊ0
	a = score[4];		//��������ã��±��0��ʼ
	//һ��ֻ��ʹ��һ������Ԫ�أ�������һ��������������
	printf("%d",a);
	return 0;
}
/*
#include<stdio.h>		//����10������Ȼ�������
int main()
{
	int i,temp[10];
	for(i=0;i<10;i++)
		scanf("%d",&temp[i]);
	for(i=9;i>=0;i--)
		printf("%d ",temp[i]);
	return 0;
}
#include<stdio.h>		//����10��������͡�ƽ��ֵ
int main()
{
	int i,temp[10];
	static int sum;
	static float avgerage;
	for(i=0;i<10;i++)
		scanf("%d",&temp[i]);
	for(i=0;i<10;i++)
		sum+=temp[i];
	avgerage = sum/10.0;
	printf("sum=%d,avgerage=%.1f",sum,avgerage);
	return 0;
}
#include<stdio.h>		//�����������ݵ����ֵ
int main()
{
	int max,i,temp[5];
	for(i=0;i<5;i++)
		scanf("%d",&temp[i]);
	for(i=0,max=0;i<5;i++)
		max=max>temp[i]?max:temp[i];
	printf("%d\n",max);
	return 0;
}*/