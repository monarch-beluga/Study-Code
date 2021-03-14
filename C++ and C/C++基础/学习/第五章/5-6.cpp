#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	double x, y;
	x = 3.14159 / 4;
	do
	{
		y = x;
		x = cos(x);
	} while (fabs(x - y) > 1e-6);
	cout << x << endl;
	return 0;
}
