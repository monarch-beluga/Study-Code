#include<stdio.h>
#include<math.h>
#define PAL 3.14159
int main()
{
	float x,y,z;
	printf("请输入一个数：");
	scanf("%f",&x);
	y = abs(x);
	printf("绝对值 = %f\n",y);
	y = exp(x);
	printf("ex值 = %f\n",y);
	y = sin(x/180*PAL);
	printf("正弦值 = %f\n",y);
	y = acos(x);
	printf("反余弦值 = %f\n",y);
	y = pow(x,5);
	printf("x的五次幂=%d",x);
	return 0;
}