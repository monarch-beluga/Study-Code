#include<stdio.h>

float ndvi_to_fpar(float ndvi)
{
	float sr = (1+ndvi)/(1-ndvi);
	float fpar_sr = (sr-0.02)*(0.95-0.001)/0.96 + 0.001;
	float fpar_ndvi = (ndvi - 0.03)*(0.95-0.001)/0.93 + 0.001;
	float fpar_v = 0.5*fpar_ndvi + 0.5*fpar_sr;
	return fpar_v / 10;
}

int main()
{
	float n = 0.5;
	printf("%f\n", ndvi_to_fpar(n));
}
