#include "学生类型.h"
#include<windows.h>

void Menu();
void Menu_select();
void Print_student(int i);
void Print_students();
int Lookup();
void Lookup_student();
void Modify_student();
void Add_student();
void Delect_student();
void Exit_system();
void SaveInFile();

SqList Students;

int main()
{
	Menu();
	return 0;
} 

void Menu()
{
	system("cls");
	printf("\n********学生成绩管理系统*********\n");
	printf("*\t1-输出所有学生信息\t*\n");
	printf("*\t2-按学号查询学生信息\t*\n");
	printf("*\t3-修改学生数据\t\t*\n");
	printf("*\t4-添加一个学生信息\t*\n");
	printf("*\t5-删除一个学生信息\t*\n");
	printf("*\t0-退出系统\t\t*\n");
	printf("********************************\n");
	Menu_select();
}
void Menu_select()
{
	int a; 
	int b;
	printf("请选择<Select>:\n");
	scanf("%d",&a);
	switch(a)
	{
		case 1:Print_students();break;
		case 2:Lookup_student();break;
		case 3:Modify_student();break;
		case 4:Add_student();break;
		case 5:Delect_student();break;
		case 0:Exit_system();
	}
	system("pause");
	Menu();
}
void Print_student(int i)
{ 
	printf("姓名:%s\n",Students.elem[i].name);
	printf("学号:%s\n",Students.elem[i].num); 
	printf("专业班级:%s\n",Students.elem[i].classname); 
	printf("成绩:%d\n",Students.elem[i].score);
}
void Print_students()
{
	int i = 0;
	while(i < Students.length)
	{
		printf("\t学生%d\n",i+1);
		Print_student(i);
		printf("\n");
		i++;
	}
}
int Lookup()
{
	char num[13];
	int i = 0;
	scanf("%s",num);
	while(i < Students.length)
	{
		if(strcmp(num,Students.elem[i].num) == 0)
		{
			break;
		}
		i++;
	}
	return i;
}
void Lookup_student() 
{
	int i;
	printf("请输入需要查询的学号:\n");
	i = Lookup();
	if (i < Students.length)
		Print_student(i);
	else
		printf("查找错误，没有该学生学号。");
}
void Modify_student()
{
	int i;
	printf("请输入需要修改学生的学号:\n");
	i = Lookup();
	if (i < Students.length)
	{
		Print_student(i);
		printf("请输入修改后学生名字:\n");
		scanf("%s",Students.elem[i].name);
		printf("请输入修改后学生专业班级:\n");
		scanf("%s",&Students.elem[i].classname);
		printf("请输入修改后学生学号:\n");
		scanf("%s",&Students.elem[i].num);
		printf("请输入修改后学生成绩:\n");
		scanf("%d",&Students.elem[i].score);
	}
	else
		printf("查找错误，没有该学生学号。");
}
void Add_student()
{
	ElemType student;
	printf("请输入学生名字:\n");
	scanf("%s",student.name);
	printf("请输入学生专业班级:\n");
	scanf("%s",&student.classname);
	printf("请输入学生学号:\n");
	scanf("%s",&student.num);
	printf("请输入学生成绩:\n");
	scanf("%d",&student.score);
	Students.elem[Students.length] = student;
	Students.length++;
}
void Delect_student()
{
	int i;
	int flag;
	printf("请输入需要删除学生的学号:\n");
	i = Lookup();
	if (i < Students.length)
	{
		Print_student(i);
		printf("是否删除该学生：0-否\t1-是\n");
		scanf("%d",&flag);
		if (flag)
		{
			for(;i<Students.length-1;i++)
			Students.elem[i] = Students.elem[i+1];
			Students.length--;
			printf("删除成功！！\n");
		}
	}
	else
		printf("查找错误，没有该学生学号。");
}
void Exit_system()
{
	exit(0);
}
void SaveInFile()
{
	int i = 0;
	char[20] path = "Students.txt";
	FILE *f = fopen(path,"w");
	while(i < Students.length)
	{
		fprintf(f, "%s\t%s\t%s\t%d\n", Students.elem[i].name,Students.elem[i].num,Students.elem[i].classname,Students.elem[i].score);
		
	}
}