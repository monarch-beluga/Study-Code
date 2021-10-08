#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
	FILE* f, * f1;
	int i, j, k;
	double a[38];
	errno_t err;
	char Y35[35], Y46[46], year[5];
	for (i = 1982;i < 2003;i++)
	{
		printf("-----------%d-------------\n", i);
		_itoa_s(i, year, 10);
		strcpy_s(Y35, "E:/temp/CEVSA_CN/lai_annually/");
		strcat_s(Y35, year);
		err = fopen_s(&f, Y35, "r");
		strcpy_s(Y46, "E:/temp/CEVSA_CN/lai_annually/lai_result_");
		strcat_s(Y46, year);
		err = fopen_s(&f1, Y46, "w");
		for (j = 0;j < 96899;j++)
		{
			for (k = 0;k < 38;k++)
			{
				fscanf_s(f, "%lf", &a[k]);
				if (a[k] < 0) a[k] = 0;
				fprintf(f1, "%9.2lf", a[k]);
			}
			fprintf(f1, "\n");
			printf("%d\n", j);
		}
		fclose(f);
		fclose(f1);
	}
	return 0;
}