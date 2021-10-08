#include <iostream>
using namespace std;

int main()
{
	int fre;
	cin >> fre;
	for(int i = 0; i < fre; i++)
	{
		int red, blue, d;
		int temp;
		cin >> red >> blue >> d;
		if (red < blue)
		{
			temp = red;
			red = blue;
			blue = temp;
		}
		temp = red / blue;
		if (red % blue != 0)
			temp++;
		if (temp-1 <= d)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
