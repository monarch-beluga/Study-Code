#include<iostream>
#include<string>
using namespace std;

class stock
{
	private:
		string stockcode;
		int quan;
		double price;
	public:
		stock()
		{
			stockcode = "000000";
		}
		stock(string code, int q = 1000, double p = 8.98)
		{
			stockcode = code;
			quan = q;
			price = p;
		}

		void print()
		{
			cout << "运行结果: " << endl;
			cout << "----------------------------------" << endl;
			cout << "\t" << this->stockcode << "\t" << this->quan << "\t" << this->price << endl;
		}
};

int main()
{
	stock st1("1000001", 3000, 5.67);
	st1.print();
	stock st2("100002");
	st2.print();
	return 0;
}
