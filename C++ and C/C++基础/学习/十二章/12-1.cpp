#include<iostream>
using namespace std;

class cylinder
{
	private:
		double r, h, volume;
	public:
		cylinder(double a, double b);
		void vol();
};

cylinder::cylinder(double a, double b)
{
	r = a;
	h = b;
	volume = 3.14159065 * r * r * h;
}
void cylinder::vol()
{
	cout << "volume is : " << volume << endl;
}

int main()
{
	cylinder x(2.2, 8.09);
	x.vol();
	return 0;
}
