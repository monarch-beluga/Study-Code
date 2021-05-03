#include <iostream>
using namespace std;

int main()
{
	int fre;
	int n;
	int* array;
	int temp;
	cin >> fre;
	for(int i = 0; i < fre; i++)
	{
		cin >> n;
		array = new int[n];
		for (int j = 0, k = n; j < k;)
		{
			cin >> temp;
			if (temp % 2 != 0)
				array[j++] = temp;
			else
				array[--k] = temp;
		}
		for (int j = 0; j < n; j++)
			cout << array[j] << ' ';
		cout << endl;
	}
}
