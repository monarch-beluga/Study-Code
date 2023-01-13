#include<iostream>
using namespace std;

int main()
{
    int i;
    cin >> i;
    for(; i > 0; --i)
        cout << i << " Hello World!!!" << endl;
    return 0;
}
create table result (
    Student_No int(4) not null comment '学号',
    SubjectNo int(4) not null comment '课程编号',
    ExamDate datetime not null comment '考试日期',
    StudentResult int(4) not null comment '考试成绩',
    key SubjectNo (SubjectNo)
) engine=innodb charset=utf8;
