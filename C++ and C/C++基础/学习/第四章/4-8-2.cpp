#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

int main()
{
	for (int i=1; i<=8; i++)
	{
		for (int j=1; j<=i; j++)
			cout<<" ";
		for (int j=1; j<=18-i; j++)
			cout << "# ";
		cout << endl;
	}
	return 0;
}