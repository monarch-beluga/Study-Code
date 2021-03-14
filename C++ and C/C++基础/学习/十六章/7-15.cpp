#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int flag = 0, flag2 = 0;
	int sum = 0;
	char ch;

	fstream in("file15.txt", ios::in);
	if (!in)
	{
		cerr << "Error open file";
		return 1;
	}

	while ((ch = in.get()) != EOF)
	{
		if (ch == ' ')
		{
			if (flag != 1)
				flag = 1;
		}
		else
		{
			if (flag == 1 && ch == 'i')
				flag2 = 1;
			if (flag2 == 1 && ch == 's')
			{
				sum++;
				flag2 = 0;
			}
			flag = 0;
		}
	}
	cout << sum << endl;
	in.close();

	return 0;
}