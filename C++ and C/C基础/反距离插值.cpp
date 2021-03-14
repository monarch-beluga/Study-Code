# include<stdio.h>
# include<stdlib.h>
# include<string.h>
# include<math.h>
# include"IDW.h"
int main()
{
	double a1[5][38],a[38];
	int i,j,k = 0;
	FILE *f1,*f2;
	char YE39[39],YEAR[5];
	for(int year=2003;year<2018;year++)
	{
		printf("-------------%d-------------",year);
		INTYR(year,YEAR);
		str1(YE39,"E:/temp/CEVSA_CN/Basic_inputs/tas/",YEAR);
		f1 = fopen(YE39,"r");
		str1(YE39,"E:/temp/CEVSA_CN/Basic_inputs/Tav/",YEAR);
		f2 = fopen(YE39,"w");
		for(j = 0;j<96899;j++,k=0)
		{
			printf("%d\n",j);
			if(j<5)
			{
				for(i = 0;i < 38;i++)
				{
					fscanf(f1,"%lf",&a[i]);
					fprintf(f2,"%8.2lf",a[i]);
				}
				fprintf(f2,"\n");
				copy(a1[j],a);
			}
			else
			{
				for(i = 0;i < 38;i++)
					fscanf(f1,"%lf",&a[i]);
				for(i = 2;i < 38;i++)
				{
					if(fabs(a[i]) >= 100.0)
					{
						k = 1;
						break;
					}
				}
				if(k == 1)
					IDW(a,a1);
				for(i=0;i<4;i++)
					copy(a1[i],a1[i+1]);
				copy(a1[4],a);
				for(i = 0;i < 38;i++)
					fprintf(f2,"%8.2lf",a[i]);
				fprintf(f2,"\n");
			}
		}
		fclose(f1);
		fclose(f2);
	}
	printf("end");
	return 0;
}