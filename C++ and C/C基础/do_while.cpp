#include <stdio.h>
int main()
{
	int i=2;
	float s=1;
	do{
		s += 1.0/i;
		i += 2;
	}while(i <= 50);
	printf("%f\n",s);
	return 0;
}
/*#include <stdio.h>		//�������
int main()
{
	int i;
	do
	{
		printf("������������");
		scanf("%d",&i);
	}while(i%2 == 0);
	printf("i = %d\n",i);
	return 0;
}
*/