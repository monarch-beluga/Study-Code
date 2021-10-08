#include<stdio.h>
int main()
{
	double a[3][140];
	FILE* f1, * f2, * f3;
	errno_t err;
	err = fopen_s(&f1, "E:/temp/CEVSA_CN/result_rs - ¸±±¾/result/2003", "r");
	err = fopen_s(&f2, "E:/temp/CEVSA_CN/result_rs/result/2003", "r");
	err = fopen_s(&f3, "E:/temp/work/2003", "w");
	for (int i = 0; i < 96899; i++)
	{
		printf("%d\n", i);
		for (int j = 0; j < 140; j++)
		{
			fscanf_s(f1, "%lf", &a[0][j]);
			fscanf_s(f2, "%lf", &a[1][j]);
			a[2][j] = a[0][j] - a[1][j];
			if (j == 1) fprintf(f3, "%3d", (int)a[2][j]);
			else if (j < 2) fprintf(f3, "%6.3lf", a[2][j]);
			else if (j < 30) fprintf(f3, "%7.0lf", a[2][j]);
			else if (j < 32) fprintf(f3, "%6.2lf", a[2][j]);
			else fprintf(f3, "%6.1lf", a[2][j]);
		}
		fprintf(f3, "\n");
	}
	fclose(f1);
	fclose(f2);
	fclose(f3);
	printf("end\n");
}