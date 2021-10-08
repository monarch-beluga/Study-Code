#include<iostream>
using namespace std;

class Coord
{
	private:
		int x, y;
	public:
		Coord(int x1 = 0, int y1 = 0)
		{
			x = x1;
			y = y1;
		}
		friend Coord operator- (Coord& obj);
		void print();
};

Coord operator- (Coord &obj)
{
	obj.x = -obj.x;
	obj.y = -obj.y;
	return obj;
}

void Coord::print()
{
	cout << "x=" << x << " y=" << y << endl;
}

int main()
{
	Coord ob1(50, 60), ob2;
	ob1.print();
	ob2 = -ob1;
	ob2.print();
	return 0;
}
