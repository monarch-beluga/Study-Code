#include<iostream>
using namespace std;

class book
{
private:
	int qu, price;
public:
	book(int a, int b)
	{
		qu = a;
		price = b;
	}

	void show_money()
	{
		cout << "qu*price: " << qu * price << endl;
	}
};

int main()
{
	book ob[] = {
		book(1, 10),
		book(2, 20),
		book(3, 30),
		book(4, 40),
		book(5, 50),
	};
	book* p;
	p = &ob[4];

	for (int i = 0; i < sizeof(ob) / sizeof(ob[0]); i++)
	{
		p->show_money();
		p--;
	}
	return 0;
}
