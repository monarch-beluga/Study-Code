#include<stdio.h>
int main()
{
	FILE* f, * f1, * f2;
	int i, j;
	double x, y;
	errno_t err;
	err = fopen_s(&f, "E:/temp/CEVSA_CN/Basic_inputs/inpt/CO2annual.txt", "r");
	err = fopen_s(&f1, "E:/temp/CEVSA_CN/Basic_inputs/inpt/cong", "w");
	for (i = 0;i < 59;i++)
	{
		fscanf_s(f, "%d%lf%*[^\n]", &j, &x);
		if (j > 1979)
			fprintf(f1, "%.2lf\n", x / 10);
		printf("%d\n", i);
	}
	return 0;
}