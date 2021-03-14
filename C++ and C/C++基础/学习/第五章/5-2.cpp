#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;

const double eps = 1e-7;
double f(double x)
{
	return exp(x) / (1 + x * x);
}
double integral(double a, double b)
{
	int n = 1;
	double h, tn, t2n, i2n, in = 0, sigma, x;
	h = b - a;
	t2n = i2n = h * (f(a) + f(b)) / 2;
	for (; fabs(i2n - in) >= eps; n *= 2, h /= 2)
	{
		tn = t2n;
		in = i2n;
		sigma = 0;
		for (int k = 0; k < n; k++, sigma += f(x))
			x = a + (k + 0.5) * h;
		t2n = (tn + h * sigma) / 2.0;
		i2n = (4 * t2n - tn) / 3.0;
	}
	return i2n;
}

int main()
{
	double a = 0, b = 1;
	cout << "the integral of f(x) from"
		<< a << " to " << b << " is:\n"
		<< fixed
		<< setprecision(8)
		<< setw(8) << integral(a, b) << endl;
	return 0;
}
