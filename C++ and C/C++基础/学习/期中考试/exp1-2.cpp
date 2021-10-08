#include<iostream>
#include <iomanip>
#include<cmath>
using namespace std;

double log2(double n)					//����log2(n)
{
	return log10(n) / log10(2);
}
long exponent(int n)					//����2^n
{
	long s = 1;
	for (int i = 1;i <= n; i++)
		s *= 2;
	return s;
}
long factorial(int n)					//����n!
{
	long s = 1;
	for (int i = 1;i <= n; i++)
		s *= i;
	return s;
}
void fun(int n)							//��ӡ���
{
	cout << "log2(n) sqrt(n)	 n	nlog2(n)  n^2	    n^3	     2^n		n!" << endl;
	cout << "= = = == = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =" << endl;
	for (int i = 1;i <= n;i++)
	{
		cout << setw(5) << fixed << setprecision(2) << log2(double(i)) << "\t";			//����log2����
		cout << setw(5) << fixed << setprecision(2) << sqrt(i) << "\t";
		cout << setw(2) << i << "\t";
		cout << setw(7) << fixed << setprecision(2) << i * log2(double(i)) << "\t";		//����log2����
		cout << setw(5) << i * i << "\t";
		cout << setw(7) << i * i * i << "\t";
		cout << setw(8) << exponent(i) << "\t";			//����exponent����
		cout << setw(10) << factorial(i) << endl;		//����factorial����
	}
}

int main()							//������
{
	int n = 10;
	fun(n);							//����fun����
	return 1;
}

