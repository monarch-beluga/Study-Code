#include<iostream>
#include<ctime>
#include <iomanip>
#include<cmath>
using namespace std;

long add1(long n)					//方法1：for循环累加法
{
	long sum = 0;
	for (int i = 1;i <= n;i++)
		sum += i;
	return sum;
}
void AddTime1(long n)				//方法1所用时间统计
{
	clock_t t;
	long sum;
	t = clock();
	sum = add1(n);					//调用add1函数
	t = clock() - t;				//计算方法2所用时间
	cout << "方法1：" << endl;
	cout << "	结果：1~" << n << "之和：" << sum << endl;
	cout << "	用时：" << fixed << setprecision(6) << (float(t) / CLOCKS_PER_SEC) << "秒" << endl;
}
long add2(long n)					//方法2：高斯法
{
	return n * (n + 1) / 2;
}
void AddTime2(long n)				//方法2所用时间统计
{
	clock_t t;
	long sum;
	t = clock();
	sum = add2(n);					//调用add2函数
	t = clock() - t;				//计算方法2所用时间
	cout << "方法2：" << endl;
	cout << "	结果：1~" << n << "之和：" << sum << endl;
	cout << "	用时：" << fixed << setprecision(6) << (float(t) / CLOCKS_PER_SEC) << "秒" << endl;
}

int main()							//主函数
{
	int n;
	cout << "n(大于1000000)：";
	cin >> n;
	if (n < 1000000)
		return 0;
	AddTime1(n);						//调用AddTime1函数
	AddTime2(n);						//调用AddTime2函数
	return 1;
}

