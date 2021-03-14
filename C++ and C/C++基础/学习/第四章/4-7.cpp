#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

int main()
{
	double x, a;
	cout << "please input a value:\n";
	cin >> a;
	x = a;
	while(fabs((x-a/x)/2) > 1e-13)
		x = (x+a/x) / 2;
	cout << setprecision(13) << a << "的平方根是" << x << endl;
	return 0;
}