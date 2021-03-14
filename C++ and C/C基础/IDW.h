/*
 * INTYR.h
 *
 *  Created on: 2020Äê7ÔÂ22ÈÕ
 *      Author: °×¾¨
 */

#ifndef INTYR_H_
#define INTYR_H_
# include<math.h>
# include<string.h>
struct point
{
	double x;
	double y;
	double z;
	double weight;
	double distance;
};
const int r = 2;
point p[50];
point q;
void Distance()
{
	for(int i = 0; i < 5; ++i)
	p[i].distance = sqrt((q.x-p[i].x)*(q.x-p[i].x) + (q.y-p[i].y) *(q.y-p[i].y));
}
void Weight()
{
	double f = 0;
	int i = 0;
	for(i = 0; i < 5; ++i)
	f += pow(1.0 / p[i].distance, r);
	for(i = 0; i < 5; ++i)
	p[i].weight = pow(1.0 / p[i].distance, r) / f;
}
void Getval()
{
	q.z = 0;
	for(int i = 0; i < 5; ++i)
	q.z += p[i].weight * p[i].z;
}
double idw(double x1[],double y1[],double z1[],double x,double y)
{
	for(int i = 0; i < 5; ++i)
	{
		p[i].x = x1[i];
		p[i].y = y1[i];
		p[i].z = z1[i];
	}
	q.x = x;
	q.y = y;
	Distance();
	Weight();
	Getval();
	return q.z;
}
void copy(double a[],double b[])
{
	for (int i=0;i<38;i++)
		a[i] = b[i];
}
void IDW(double a[],double a1[5][38])
{
	double ax[5],ay[5],az[5];
	int i,j;
	for(i = 0; i < 5; ++i)
	{
		ax[i] = a1[i][0];
		ay[i] = a1[i][1];
	}
	for(i = 2;i<38;i++)
	{
		for(j = 0;j<5;j++)
			az[j] = a1[j][i];
		a[i] = idw(ax,ay,az,a[0],a[1]);
	}
}
void str1(char *c,char *a,char *b)
{
	strcpy(c,a);
	strcat(c,b);
}
void INTYR(int yyyy, char intyr[5])
{
	int i;
	intyr[4] = '\0';
	for(i=3;i>=0;i--,yyyy/=10)
		intyr[i] = (char)('0' + yyyy % 10);
}
#endif /* INTYR_H_ */
