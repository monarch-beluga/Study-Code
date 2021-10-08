#include<iostream>
using namespace std;

int main()
{
	float s = 100, h = 100;
	for (int i=1; i<10; i++)
	{
		s += h;
		h /= 2;
	}
	cout << "共经过" << s << "米， 第10次反弹" << h << "米高.\n";
	return 0;
}