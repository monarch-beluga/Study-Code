#include <stdio.h>
int main()		//������
{
	int b,c;
	char a;
	scanf("%d%c%d",&b,&a,&c);
	switch(a)
	{
		case '-':printf("%d%c%d = %d",b,a,c,b-c);break;
		case '+':printf("%d%c%d = %d",b,a,c,b+c);break;
		case '*':printf("%d%c%d = %d",b,a,c,b-c);break;
		case '/':printf("%d%c%d = %d",b,a,c,b-c);break;
		default:printf("ֻ�ܽ��мӼ��˳���");
	}
	return 0;
}
/*#include <stdio.h>		//����
int main()
{
	int b,c;
	printf("���������");
	scanf("%d",&c);
	if(c>=0&&c<=100)
	{
		b = c/10;
		switch(b)
		{
			case 10:
			case 9:printf("����\n");break;
			case 8:printf("����\n");break;
			case 7:printf("�е�\n");break;
			case 6:printf("����\n");break;
			default:printf("������\n");
		}
	}
	else
		printf("��ʽ����ȷ��\n");
	return 0;
}
*/