#include<stdio.h>
#include<math.h>
#define PAL 3.14159
int main()
{
	float x,y,z;
	printf("������һ������");
	scanf("%f",&x);
	y = abs(x);
	printf("����ֵ = %f\n",y);
	y = exp(x);
	printf("exֵ = %f\n",y);
	y = sin(x/180*PAL);
	printf("����ֵ = %f\n",y);
	y = acos(x);
	printf("������ֵ = %f\n",y);
	y = pow(x,5);
	printf("x�������=%d",x);
	return 0;
}