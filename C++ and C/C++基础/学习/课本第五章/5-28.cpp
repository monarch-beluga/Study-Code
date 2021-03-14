#include<iostream>
using namespace std;

class Figure
{
	protected:
		double x, y;
	public:
		Figure(double a, double b)
		{
			x = a;
			y = b;
		}
		virtual void area()
		{
			cout << "在基类中定义的虚函数，";
			cout << "为派生类提供一个公共接口，";
			cout << "以便派生类根据需要重新定义虚函数。" << endl;
		}
};

class Square :public Figure
{
	Square(double a, double b) :Figure(a, b)
	{};
	void area()
	{
		cout << "矩形的长是：" << x << "，宽是:" << y;
		cout << ",面积是：" << x * y << endl;
	}
};

class Triangle :public Figure
{
	Triangle(double a, double b) :Figure(a, b)
	{};
	void area()
	{
		cout << "三角形的高是：" << x << "，底是:" << y;
		cout << ",面积是：" << 0.5 * x * y << endl;
	}
};

class Triangle:public Figure
{
	Triangle(double a, double b) :Figure(a, b)
	{};
	void area()
	{
		cout << "三角形的高是：" << x << "，底是:" << y;
		cout << ",面积是：" << 0.5 * x * y << endl;
	}
};