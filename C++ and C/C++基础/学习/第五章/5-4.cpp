#include<iostream>
using namespace std;

int main()
{
	int n;
	long a = 1, b = 1, temp;
	cout << "please input a number:\n";
	cin >> n;
	for (int i = 3; i <= n; i++)
		temp = a + b, a = b, b = temp;
	cout << b << endl;
	return 0;
}
