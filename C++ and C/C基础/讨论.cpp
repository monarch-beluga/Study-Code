#include<stdio.h>
#include<math.h>

int main()
{
	int i = 0,j = 2;
	double a = 3.1415926;
	double p,l,d,x[11],y[11];
	printf("请输入中心坐标点:\n");
	printf("x[0]=");
	scanf("%lf",&x[0]);
	printf("y[0]=");
	scanf("%lf",&y[0]);
	printf("请输入第一个凸拐点坐标:\n");
	printf("x[1]=");
	scanf("%lf",&x[1]);
	printf("y[1]=");
	scanf("%lf", &y[1]);
	l = sqrt((x[1] - x[0]) * (x[1] - x[0]) + (y[1] - y[0]) * (y[1] - y[0]));
	if (y[0] - y[1] > 0)
		p = a - 0.5 * a - atan((x[0] - x[1]) / (y[0] - y[1]));
	else if (y[0] - y[1] == 0)
		p = a - atan((x[0] - x[1]) / (y[0] - y[1]));
	else
		p = a + 0.5 * a - atan((x[0] - x[1]) / (y[0] - y[1]));
	/* p 表示点 1 至点 0 的坐标方位角*/
	printf("其余四个凸拐点的坐标为：\n");
	for (i = 2; i < 6; i++)
	{
		x[i] = (x[1] - x[0]) * cos((i - 1) * 72.0 / 180.0 * a) - (y[1] - y[0]) * sin((i - 1) * 72.0 / 180.0 * a) + x[0];
		y[i] = (x[1] - x[0]) * sin((i - 1) * 72.0 / 180.0 * a) + (y[1] - y[0]) * cos((i - 1) * 72.0 / 180.0 * a) + y[0];
		/*运用向量旋转公式：
		已知 A（x1,y1）绕 B（x0,y0）旋转到 C（X,Y）且角 ABC 为 θ,则 X-x0=(x1-
		x0)cosθ-（y1-y0）sinθ;
		Y-y0=(x1-x0)sinθ+（y1-y2）cosθ;
		*/
		printf("x[%d]=%.3f,y[%d]=%.3f\n", j, x[i], j++, y[i]);
	}
	printf("五个凹拐点的坐标为：\n");

	d = l * sin(54.0 / 180.0 * a) - l * cos(54.0 / 180.0 * a) * tan(36.0 / 180.0 * a);
	x[6] = x[0] - d * cos(p + 36.0 / 180.0 * a);
	y[6] = y[0] - d * sin(p + 36.0 / 180.0 * a);
	/*运用坐标方位角知识，左折角为 36°*/
	printf("x[6]=%.3f,y[6]=%.3f\n", x[6], y[6]);
	j = 7;

	for (i = 7; i < 11; i++)
	{
		x[i] = (x[6] - x[0]) * cos((i - 6) * (72.0 / 180.0) * a) - (y[6] - y[0]) * sin((i - 6) * (72.0 / 180.0) * a) + x[0];
		y[i] = (x[6] - x[0]) * sin((i - 6) * (72.0 / 180.0) * a) + (y[6] - y[0]) * cos((i - 6) * (72.0 / 180.0) * a) + y[0];
		/*方法同上，旋转*/
		printf("x[%d]=%.3f,y[%d]=%.3f\n", j, x[i], j++, y[i]);
	}
	return 0;
}