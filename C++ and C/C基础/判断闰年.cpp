#include "stdafx.h"
#include<stdio.h>
int main()
{
	int year,x = 1;
	while (x == 1)
	{
		printf("��ʼ����1����������0��");
		scanf("%d",&x);
		if(x == 1)
			printf("��ʼ��\n");
		else
			break;
		printf("��������ݣ�");
		scanf("%d",&year);
		if((year % 100 == 0 && year % 400 == 0)||year % 4 == 0)
			printf("������");
		else
			printf("��������");	
	}
	return 0;
}
