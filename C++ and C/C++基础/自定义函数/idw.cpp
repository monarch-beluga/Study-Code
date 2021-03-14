# include<stdio.h>
# include"IDW.h"
int main()
{
	FILE* f, * f1, * f2;
	int i, j;
	double x;
	double a[3][5];
	//errno_t err;
	for (i = 2013; i < 2018;i++)
	{
		a[0][i - 2013] = double(i);
		a[1][i - 2013] = 0.12;
		scanf_s("%lf", &a[2][i - 2013]);
	}
	x = idw(a[0], a[1], a[2], double(2018), 0.12);
	for (i = 0;i < 5;i++)printf("%.2lf\n", a[2][i]);
	printf("%.2lf", x);
	return 0;
}