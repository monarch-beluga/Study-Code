#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
	cout << " *";
	for (int i=1; i<=9; i++)
		cout << setw(4) << i;
	cout << "\n---------------------------------------\n";
	for (int i=1; i<=9; i++)
	{
		cout << setw(3) << i;
		for (int j=1; j<=i; j++)
			cout << setw(4) << i*j;
		cout << endl;
	}
	return 0;
}