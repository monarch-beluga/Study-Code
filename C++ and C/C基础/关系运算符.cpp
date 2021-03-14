#include<stdio.h>
int main()
{
	float a = 0.15;
	float b = 1.5;
	printf("%f\n%f\n",a*100,b*10);//编译器的原因
	if(a*100==15)
		printf("对\n");
	else
		printf("错\n");
	if(b*10==15)
		printf("对\n");
	else
		printf("错\n");
	return 0;
}
