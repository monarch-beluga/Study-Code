#include <stdio.h>	//1~100�ĺ�
int main()
{
	int i = 1,sum = 0;
	while(i <= 100)
	{
		sum += i;
		i++;
	}
	printf("%d\n",sum);
	return 0;
}

/*#include <stdio.h>		//�׳�
int main()
{
	int i = 1,s = 1,y;
	while (x == 1)
	{
		printf("��������Ľ׳�:");
		scanf("%d",&y);
		while(i <= y)
		{
			s *= i;
			i++;
		}
		printf("%d\n",s);
	}
	return 0;
}

#include <stdio.h>		//������(��ȱ��)
int main()
{
	int n;
	scanf("%d",&n);
	while(n > 0)
	{
		printf("%d",n%10);
		n /= 10;
	}
	return 0;
}