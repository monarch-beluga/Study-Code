#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int fre;
	int n;
	int temp;
	int sq;
	bool flag;
	cin >> fre;
	for(int i = 0; i < fre; i++)
	{
		flag = false;
		cin >> n;
		for (int j = 0; j < n; j++)
		{
			cin >> temp;
			sq = (int)sqrt((double)temp);
			if (sq*sq != temp)
				flag = true;
		}
		if (flag)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}
}