#include<iostream>
using namespace std;

int main()
{
	int n;
	long a=1, b=1, c=1, temp;
	cout << "please input a value:\n";
	cin >> n;
	for (int i=4; i<=n; i++)
	{
		temp = a+c;
		a = b;
		b = c;
		c = temp;
	}
	cout << c << endl;
	return 0;
}