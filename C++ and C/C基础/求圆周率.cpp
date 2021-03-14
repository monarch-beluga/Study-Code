#include<stdio.h>		//随机点求圆周率（精度较低）
#include<math.h>
#include<stdlib.h>		//内含srand和rand函数
#include<time.h>		//含time函数
int main()
{
	int a = 10000000;			//精度
	int i,b = 0;
	double x,y;
	srand((unsigned)time(0));	//随机坐标
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
/*#include<stdio.h>		//公式求圆周率（精度较高）
int main()
{
	int i,j = 1000;		//精度
	double pi = 2;
	for (i = j;i > 0;i-- )
		pi = pi*i/(2*i+1)+2;	//公式
	printf("%20.18f",pi);
	return 0;
}
#include<stdio.h>		//公式求圆周率（精度一般）
int main()
{
	int i,j;
	double a = 1.0,b = 1.0,pi;
	for (i = 1;i < 1000000000;i += 4)	//精度
		a += 1.0/i;
	for (j = 3;j < 1000000000;j += 4)
		b += 1.0/j;
	pi = (a-b)*4;
	printf("%20.18f",pi);
	return 0;
}
#include<stdio.h>		//精度一般
#include<math.h>
int main()
{
	double s = 1.0,y = 1,f = 1.0;
	int i = 1;
	while(fabs(y) > 1e-6)		//fabs为浮点型数据的绝对值，精度
	{
		f = -f;
		y = f/(2*i+1);
		s += y;
		i++;
	}
	printf("%20.18f\n",4*s);
	return 0;
}*/