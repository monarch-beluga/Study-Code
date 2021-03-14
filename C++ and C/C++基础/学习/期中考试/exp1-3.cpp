#include<iostream>
#include<ctime>
#include <iomanip>
#include<cmath>
using namespace std;

bool prime1(long n)					//方法1：传统方法判断正整数n是否为素数
{
	long i;
	for (i = 2;i < n;i++)
		if (n % i == 0)
			return false;
	return true;
}
void PrimeTime1(long n)				//统计方法1所用时间
{
	clock_t t;
	long sum = 0;
	t = clock();
	for (int i = 2;i <= n;i++)
		if (prime1(i))				//用prime1函数做判断
			sum++;
	t = clock() - t;
	cout << "方法1：" << endl;
	cout << "	结果：2~" << n << "的素数个数：" << sum << endl;
	cout << "	用时：" << fixed << setprecision(6) << (float(t) / CLOCKS_PER_SEC) << "秒" << endl;
}
bool prime2(long n)					//方法2：改进方法判断正整数n是否为素数
{
	for (long i = 2;i <= int(sqrt(n)); i++)
		if (n % i == 0)
			return false;
	return true;
}
void PrimeTime2(long n)				//统计方法2所用时间
{
	clock_t t;
	long sum = 0;
	t = clock();
	for (int i = 2;i <= n;i++)
		if (prime2(i))				//用prime2函数做判断
			sum++;
	t = clock() - t;
	cout << "方法2：" << endl;
	cout << "	结果：2~" << n << "的素数个数：" << sum << endl;
	cout << "	用时：" << fixed << setprecision(6) << (float(t) / CLOCKS_PER_SEC) << "秒" << endl;
}
int main()							//主函数
{
	long n;
	cout << "n(大于100000)：";
	cin >> n;
	if (n < 100000)
		return 0;
	PrimeTime1(n);					//调用PrimeTime1函数
	PrimeTime2(n);					//调用PrimeTime2函数
	return 1;
}
