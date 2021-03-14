#include<iostream>
using namespace std;

int main()
{
	for (int i=1, sum; i<1000; i++)
	{
		sum = 0;
		for (int j=1; j<=i/2; j++)
			if (i%j == 0)
				sum += j;
		if (sum == i)
			cout << i << "ÊÇÍêÊý.\n";
	}
	return 0;
}