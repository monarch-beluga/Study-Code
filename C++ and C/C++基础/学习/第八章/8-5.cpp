#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
	void* p = malloc(1000000);
	int i = 1;
	while (p)
	{
		p = malloc(1000000);
		i++;
	}
	cout << "������Ϊ(M):" << i * 1000000 << endl;
	free(p);
}
