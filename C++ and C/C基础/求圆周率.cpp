#include<stdio.h>		//�������Բ���ʣ����Ƚϵͣ�
#include<math.h>
#include<stdlib.h>		//�ں�srand��rand����
#include<time.h>		//��time����
int main()
{
	int a = 10000000;			//����
	int i,b = 0;
	double x,y;
	srand((unsigned)time(0));	//�������
	for(i = 0;i < a;i++)
	{
		x = rand()%1000/1000.0;
		y = rand()%1000/1000.0;
		if(x*x+y*y <= 1)
			b++;
	}
	printf("%f",b*1.0/a*4);
	return 0;
}
/*#include<stdio.h>		//��ʽ��Բ���ʣ����Ƚϸߣ�
int main()
{
	int i,j = 1000;		//����
	double pi = 2;
	for (i = j;i > 0;i-- )
		pi = pi*i/(2*i+1)+2;	//��ʽ
	printf("%20.18f",pi);
	return 0;
}
#include<stdio.h>		//��ʽ��Բ���ʣ�����һ�㣩
int main()
{
	int i,j;
	double a = 1.0,b = 1.0,pi;
	for (i = 1;i < 1000000000;i += 4)	//����
		a += 1.0/i;
	for (j = 3;j < 1000000000;j += 4)
		b += 1.0/j;
	pi = (a-b)*4;
	printf("%20.18f",pi);
	return 0;
}
#include<stdio.h>		//����һ��
#include<math.h>
int main()
{
	double s = 1.0,y = 1,f = 1.0;
	int i = 1;
	while(fabs(y) > 1e-6)		//fabsΪ���������ݵľ���ֵ������
	{
		f = -f;
		y = f/(2*i+1);
		s += y;
		i++;
	}
	printf("%20.18f\n",4*s);
	return 0;
}*/