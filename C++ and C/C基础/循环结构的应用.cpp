#include <stdio.h>	//100����3�ı����Ҹ�λ��6
int main()
{
	int a;
	for (a=1;a <= 100;a++)
		if(a%3 == 0 && a%10 == 6)
			printf("%d ",a);
	return 0;
}
/*#include <stdio.h>	//�žų˷��ھ�
int main()
{
	int a,b;
	for (a=1;a <= 9;a++)
	{
		for(b=1;b <= 9;b++)
			printf("%-2d��%-2d=%-2d ",b,a,a*b);
		printf("\n");
	}
	return 0;
}