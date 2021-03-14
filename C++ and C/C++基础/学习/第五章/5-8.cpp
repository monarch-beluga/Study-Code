#include<iostream>
using namespace std;

long cattle(int n)
{
	if (n <= 0)
		return 0;
	if (n <= 3)
		return 1;
	return cattle(n - 1) + cattle(n - 3);
}

int main()
{
	int n;
	cout << "plase input a number:\n";
	cin >> n;
	cout << cattle(n) << endl;
	return 0;
}
