#include <stdio.h>
int main()
{
	int a;
	printf("�����������");
	scanf("%d",&a);
	if(a > 90)
		printf("����!");
	else if(80 <= a)		//��������80 <= a <= 90
		printf("����");
	else if(a  >= 70)
	{
		printf("�е�");		//���������Ҫ{}
		printf("d");
	}
	else if(a  >= 60)
		printf("����");
	else
		printf("������");
	return 0;
}