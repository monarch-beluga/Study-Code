#include<iostream>
#include<string>
using namespace std;

class student
{
	private:
		int no;
		string name;
		double deg;
		static double sum;
		static int num;

	public:
		student(int n, string na, double d)
		{
			no = n;
			deg = d;
			name = na;
			sum += d;
			num++;

		}

		static double avg()
		{
			return sum / num;

		}
		static int total()
		{
			return num;
		}
		void disp()
		{
			cout << "\t" << no << "\t" << name << "\t" << deg << endl;
		}

};
double student::sum = 0;
int student::num = 0;

int main()
{
	student s1(1001, "ZHOU", 97);
	student s2(1002, "ZHAN", 65);
	student s3(1003, "ZHANG", 87);
	student s4(1004, "WANG", 77);
	student s5(1005, "LONG", 99);

	cout << "--------------------------" << endl;
	cout << "\t" << "学号" << "\t" << "姓名" << "\t" << "成绩" << endl;
	cout << "----------------------------" << endl;
	s1.disp();
	s2.disp();
	s3.disp();
	s4.disp();
	s5.disp();

	cout << "-----------------------------" << endl;
	cout << "\t学生人数=" << student::total() << endl;
	cout << "\t平均成绩=" << student::avg() << endl;
	cout << "-------------------------------the end---------------------------" << endl;

	return 0;
}
