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
	cout << "������" << s << "�ף� ��10�η���" << h << "�׸�.\n";
	return 0;
}