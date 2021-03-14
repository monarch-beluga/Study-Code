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
		if (i != 1)
			cout << setw(4*i-4) << " ";
		for (int j=i; j<=9; j++)
			cout << setw(4) << i*j;
		cout << endl;
	}
	return 0;
}