#include <iostream>
using namespace std;

int main()
{
	int fre;
	int n, k;
	int color;
	// fre = 1;
	cin >> fre;
	for(int i = 0; i < fre; i++)
	{
		cin >> n >> k;
		int* arr = new int[n];
		for (int j = 0; j < n; j++)
		{
			color = k;
			cin >> arr[j];
			if (j != 0)
			{
				for (int k = 0; k < j; k++)
					if (arr[j] == arr[k])
						color--;
				if (color < 0)
					color = 0;
			}
			cout << color << ' ';
		}
		cout << endl;
	}
	return 0;
}

