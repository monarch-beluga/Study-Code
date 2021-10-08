#include<iostream>
using namespace std;
#include<map>
#include<string>

typedef struct Student
{
	int StuNumber;
	string StuName;

	bool operator<(Student const& Stu_A)const
	{
		if (StuNumber < Stu_A.StuNumber)
			return true;
		if (StuNumber == Stu_A.StuNumber)
			return StuName.compare(Stu_A.StuName) < 0;
		return false;
	}
}StudentInfo, * PStudentInfo;

int main()
{
	map < StudentInfo, int > mapStudent;
	map < StudentInfo, int >::iterator iter;

	StudentInfo studentInfo;
	studentInfo.StuNumber = 1;
	studentInfo.StuName = "周兵";
	mapStudent.insert(pair<StudentInfo, int>(studentInfo, 90));

	studentInfo.StuNumber = 2;
	studentInfo.StuName = "周敏";

	mapStudent.insert(pair<StudentInfo, int>(studentInfo, 80));

	for (iter = mapStudent.begin(); iter != mapStudent.end(); iter++)
	{
		cout << "学号：" << iter->first.StuNumber << endl;
		cout << "姓名：" << iter->first.StuName << endl;
		cout << "分数：" << iter->second << endl;
		cout << endl;
	}
	return 0;
}