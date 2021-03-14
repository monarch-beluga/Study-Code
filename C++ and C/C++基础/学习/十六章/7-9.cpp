#include<iostream>
#include<iomanip>
using namespace std;

double fact(int n)
{
	double factor = 1;
	for (int i = n; i >= 1; i--)
		factor *= i;
	return factor;
}

int main()
{
	cout << "---------------------------------" << endl;
	for (int  n = 1; n < 10; n++)
		cout << "\t" << setw(2) << n << "\t ! " << fact(n) << endl;
	cout << "---------------------------------" << endl;
	return 0;
}