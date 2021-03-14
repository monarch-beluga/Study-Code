# include<iostream>
# include<cstdlib>
using namespace std;

int var[10];
int& put(int n)
{
	if (n >= 10)
	{
		cerr << "range error in put value!\n";
		exit(1);
	}
	return var[n];
}
int get(int n)
{
	if (n >= 10)
	{
		cerr << "range error in put value!\n";
		exit(1);
	}
	return var[n];
}
int main()
{
	put(0) = 10;
	put(1) = 20;
	put(9) = 30;
	cout << get(0) << endl;
	cout << get(1) << endl;
	cout << get(9) << endl;
	put(12) = 1;
	return 0;
}