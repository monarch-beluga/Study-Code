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
			cout << "�ڻ����ж�����麯����";
			cout << "Ϊ�������ṩһ�������ӿڣ�";
			cout << "�Ա������������Ҫ���¶����麯����" << endl;
		}
};

class Square :public Figure
{
	Square(double a, double b) :Figure(a, b)
	{};
	void area()
	{
		cout << "���εĳ��ǣ�" << x << "������:" << y;
		cout << ",����ǣ�" << x * y << endl;
	}
};

class Triangle :public Figure
{
	Triangle(double a, double b) :Figure(a, b)
	{};
	void area()
	{
		cout << "�����εĸ��ǣ�" << x << "������:" << y;
		cout << ",����ǣ�" << 0.5 * x * y << endl;
	}
};

class Triangle:public Figure
{
	Triangle(double a, double b) :Figure(a, b)
	{};
	void area()
	{
		cout << "�����εĸ��ǣ�" << x << "������:" << y;
		cout << ",����ǣ�" << 0.5 * x * y << endl;
	}
};