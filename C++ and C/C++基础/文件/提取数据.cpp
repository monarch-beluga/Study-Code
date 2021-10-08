#include<stdio.h>
int main()
{
	FILE* f, * f1, * f2;
	int i;
	double x, y;
	errno_t err;
	err = fopen_s(&f, "E:/temp/CEVSA_CN/Basic_inputs/Tav/2017", "r");
	//err = fopen_s(&f1, "E:/temp/lat.txt","w");
	err = fopen_s(&f2, "E:/temp/loc.txt", "w");
	for (i = 0;i < 96899;i++)
	{
		fscanf_s(f, "%lf%lf%*[^\n]", &x, &y);
		fprintf(f2, "%.2lf\t%.2lf\n", x, y);
		printf("%d\n", i);
	}
	return 0;
}