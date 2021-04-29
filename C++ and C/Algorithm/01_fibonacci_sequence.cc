#include <iostream>
using namespace std;

// 打印斐波那契数列的第n项
int GetFibonacciNum(int n);

int main()
{
	int n;
	int fibonacci_num;
	cout << "Please enter the number of items n:" << endl;
	cin >> n;
	fibonacci_num = GetFibonacciNum(n);
	cout << "Fibonacci Sequence term " << n << " is:";
	cout << fibonacci_num << endl;
	return 0;
}

int GetFibonacciNum(int n)
{
	if (n < 1)
	{
		return -1;
	}
	if (n < 2)
		return 1;
	else
	{
		int front[2] = {1, 1};
		int curr;
		for (int i = 2; i < n; ++i)
		{
			curr = front[0] + front[1];
			front[0] = front[1];
			front[1] = curr;
		}
		return curr;
	}
}
