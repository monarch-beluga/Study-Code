# include<iostream>
using namespace std;

const int Size = 10;
void findmax(int* a, int n, int& pk)
{
	for (int i = 1; i < Size; i++)
		if (a[i] > a[pk])
			pk = i;
}

int main()
{
	int a[Size], n = 0;
	cout << "please input " << Size << "datas:\n";
	for (int i = 0; i < Size;i++)
		cin >> a[i];
	findmax(a, Size, n);
	cout << "the maximum is " << a[n] << endl
		<< "It is index is " << n << endl;
	return 0;
}