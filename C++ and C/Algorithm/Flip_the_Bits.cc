#include <iostream>
#include <string>
using namespace std;

int main()
{
	int fre, n;
	string a, b;
	bool flag;
	int len0, len1;
	int eq, neq;
	int pre;
	cin >> fre;
	for(int i = 0; i < fre; i++)
	{
		len0 = 0, len1 = 0;
		eq = 0, neq = 0;
		pre = 0;
		flag = true;
		cin >> n;
		cin >> a;
		cin >> b;
		for (int j = 0; j < n; j++)
		{
			if (a[j] == '1')
				len1++;
			else
				len0++;
			if (a[j] == b[j])
				eq++;
			else
				neq++;
			if (len0 == len1)
			{
				if ((eq != 0) && (neq != 0))
				{
					flag = false;
					pre = n-1;
					break;
				}
				len0 = 0, len1 = 0;
				eq = 0, neq = 0;
				pre = j;
			}
		}
		if (pre != n-1)
			if (neq != 0)
				flag = false;
		if (flag)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}
}