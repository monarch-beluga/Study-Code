#include<iostream>
using namespace std;

class Base
{
	public:
		virtual void func1();
		virtual void func2();
		virtual void func3();
		void func4();
};
class Derived :public Base
{
	public:
		virtual void func1();
		void func2(int x);
		void func4();
};
void Base::func1()
{
	cout << "--Base func1--\n";
}
void Base::func2()
{
	cout << "--Base func2--\n";
}
void Base::func3()
{
	cout << "--Base func3--\n";
}
void Base::func4()
{
	cout << "--Base func4--\n";
}
void Derived::func1()
{
	cout << "--Derived func1--\n";
}
void Derived::func2(int x)
{
	cout << "--Derived func2--\n";
}
void Derived::func4()
{
	cout << "--Derived func4--\n";
}

int main()
{
	Base d1, * bp;
	Derived d2;
	bp = &d2;
	bp->func1();
	bp->func2();
	bp->func4();
	cout << "sk ";
	return 0;
}