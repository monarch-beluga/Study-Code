#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	double sum = 1, t = -1, x;
	int i = 1;
	cout << "please input a value:\n";
	cin >> x;
	do
	{
		t *= (-1) * x /i;
		sum += t;
		i++;
	}while(fabs(t) > 1e-8);
	cout << "sum=" << sum <<endl;
	return 0;
}