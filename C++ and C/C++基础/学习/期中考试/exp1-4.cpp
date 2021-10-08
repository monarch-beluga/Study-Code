#include<iostream>
#include <iomanip>
using namespace std;

long Sum(int n)						//计算连续整数阶乘和
{
	long sum = 0, fact = 1;
	for (int i = 1;i <= n;i++)
	{
		fact *= i;					//求出的fact为i！
		sum += fact;				//求出的sum为1! + 2! + …… + i!
	}
	return sum;
}
int main()							//主函数
{
	int n;
	cout << "n(3 - 20):";
	cin >> n;
	if (n < 3 || n>20)
		return 0;
	cout << "1! + 2! + …… + " << n << "!= " << Sum(n) << endl;			//调用Sum函数
	return 1;
}
