#include<iostream>
using namespace std;

double poly(int n, double x)
{
	if (n == 0)
		return 1;
	else if (n == 1)
		return x;
	else
		return ((2 * n - 1) * x * poly(n - 1, x) - (n - 1) * poly(n - 2, x)) / n;
}

int main()
{
	int n;
	double x;
	cout << "plese input x and n:";
	cin >> x >> n;
	cout << "x的n阶勒让德多项式的值为：" << poly(n, x) << endl;
	return 0;
}
