# include<iostream>
using namespace std;

struct Student
{
	int mathmidterm;
	int mathfinal;
};

int main()
{
	Student s;
	cout << "please input midterm and final math\n"
		 << "grade of a student:\n";
	cin >> s.mathmidterm >> s.mathfinal;
	cout << "the average grade of midterm and final math is: "
		<< (s.mathfinal + s.mathmidterm) / 2.0 << endl;
	return 0;
}