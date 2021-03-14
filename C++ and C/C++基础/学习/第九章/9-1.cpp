# include<iostream>
using namespace std;


const int Size = 10;
void findmax(int* a, int n, int i, int &pk)
{
	if (i < n)
	{
		if (a[i] > a[pk])
			pk = i;
		findmax(a, n, i + 1, pk);
	}
}

int main()
{
	int a[Size], n = 0;
	cout << "please input " << Size << "datas:\n";
	for (int i = 0; i < Size;i++)
		cin >> a[i];
	findmax(a, Size, 0, n);
	cout << "the maximum is " << a[n] << endl
		 << "It is index is " << n << endl;
	return 0;
}