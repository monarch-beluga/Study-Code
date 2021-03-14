#include<iostream>
#include <iomanip>
#include<cmath>
using namespace std;

double log2(double n)					//计算log2(n)
{
	return log10(n) / log10(2);
}
long exponent(int n)					//计算2^n
{
	long s = 1;
	for (int i = 1;i <= n; i++)
		s *= 2;
	return s;
}
long factorial(int n)					//计算n!
{
	long s = 1;
	for (int i = 1;i <= n; i++)
		s *= i;
	return s;
}
void fun(int n)							//打印表格
{
	cout << "log2(n) sqrt(n)	 n	nlog2(n)  n^2	    n^3	     2^n		n!" << endl;
	cout << "= = = == = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =" << endl;
	for (int i = 1;i <= n;i++)
	{
		cout << setw(5) << fixed << setprecision(2) << log2(double(i)) << "\t";			//调用log2函数
		cout << setw(5) << fixed << setprecision(2) << sqrt(i) << "\t";
		cout << setw(2) << i << "\t";
		cout << setw(7) << fixed << setprecision(2) << i * log2(double(i)) << "\t";		//调用log2函数
		cout << setw(5) << i * i << "\t";
		cout << setw(7) << i * i * i << "\t";
		cout << setw(8) << exponent(i) << "\t";			//调用exponent函数
		cout << setw(10) << factorial(i) << endl;		//调用factorial函数
	}
}

int main()							//主函数
{
	int n = 10;
	fun(n);							//调用fun函数
	return 1;
}

