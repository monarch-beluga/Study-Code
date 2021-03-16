#include "学生类型.h"
#include<windows.h>

// 自定义函数声明
void Menu();						// 菜单界面函数
void Menu_select();					// 菜单界面选择函数
void Print_student(int i);			// 按顺序表数字打印学生信息函数
void Print_students();				// 打印所有学生信息函数
int Lookup(char num[]);			// 按学号查询学生顺序表数字
void Lookup_student();				// 按学号打印学生信息
void Modify_student();				// 修改学生信息
void Add_student();					// 添加学生信息
void Delect_student();				// 删除学生信息
void Exit_system();					// 退出系统
void SaveInFile();					// 将学生信息输出到文件中保存

SqList Students;					// 定义全局变量顺序表
int save = 0;						// 判断学生信息是否更新

int main()
{
	// 学生信息文件读取
	int i = 0;
	FILE *f;
	f = fopen("Students.txt","r");
	if (f == NULL)					// 如果文件不存在，就创建一个文件
		SaveInFile();
	else
	{
		while(!feof(f))				// 循环读取信息，判断文件读取是否结束
		{
			// 文件读取
			fscanf(f, "%s", Students.elem[i].name);
			fscanf(f, "%s", Students.elem[i].num);
			fscanf(f, "%s", Students.elem[i].classname);
			fscanf(f, "%d", &Students.elem[i].score);
			i++;
			// 每读取一个顺序表加1
			Students.length++;
		}
		// 因为feof(f)文件读取结束后还会再读取一次，所以要将顺序表减一
		Students.length--;
	}

	// 菜单函数，开始进入学生管理系统
	Menu();
	return 0;
} 

void Menu()
{
	system("cls");					// 清屏
	// 打印界面
	printf("\n********学生成绩管理系统*********\n");
	printf("*\t1-输出所有学生信息\t*\n");
	printf("*\t2-按学号查询学生信息\t*\n");
	printf("*\t3-修改学生数据\t\t*\n");
	printf("*\t4-添加一个学生信息\t*\n");
	printf("*\t5-删除一个学生信息\t*\n");
	printf("*\t0-退出系统\t\t*\n");
	printf("********************************\n");
	// 菜单选择
	Menu_select();
}

void Menu_select()
{
	int a; 
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
int Lookup(char num[])
{
	int i = 0;
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
	char num[13];
	printf("请输入需要查询的学号:\n");
	scanf("%s",num);
	i = Lookup(num);
	if (i < Students.length)
		Print_student(i);
	else
		printf("查找错误，没有该学生学号。");
}
void Modify_student()
{
	int i;
	char num[13];
	printf("请输入需要修改学生的学号:\n");
	scanf("%s",num);
	i = Lookup(num);
	if (i < Students.length)
	{
		Print_student(i);
		printf("请输入修改后学生名字:\n");
		scanf("%s",Students.elem[i].name);
		printf("请输入修改后学生专业班级:\n");
		scanf("%s",Students.elem[i].classname);
		printf("请输入修改后学生学号:\n");
		scanf("%s",Students.elem[i].num);
		printf("请输入修改后学生成绩:\n");
		scanf("%d",&Students.elem[i].score);
		save++;
	}
	else
		printf("查找错误，没有该学生学号。");
}
void Add_student()
{
	int i;
	ElemType student;
	printf("请输入学生名字:\n");
	scanf("%s",student.name);
	printf("请输入学生专业班级:\n");
	scanf("%s",student.classname);
	printf("请输入学生学号:\n");
	scanf("%s",student.num);
	printf("请输入学生成绩:\n");
	scanf("%d",&student.score);
	i = Lookup(student.num);
	if (i < Students.length)
		printf("添加失败，该学号已存在\n");
	else
	{
		Students.elem[Students.length] = student;
		Students.length++;
		save++;
	}
}
void Delect_student()
{
	int i;
	int flag;
	char num[13];
	printf("请输入需要删除学生的学号:\n");
	scanf("%s",num);
	i = Lookup(num);
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
		save++;
	}
	else
		printf("查找错误，没有该学生学号。");
}
void Exit_system()
{
	if(save != 0)
		SaveInFile();
	exit(0);
}
void SaveInFile()
{
	int i = 0;
	FILE *f = fopen("Students.txt","w");
	while(i < Students.length)
	{
		fprintf(f, "%s\t", Students.elem[i].name);
		fprintf(f, "%s\t", Students.elem[i].num);
		fprintf(f, "%s\t", Students.elem[i].classname);
		fprintf(f, "%d\n", Students.elem[i].score);
		i++;
	}
	fclose(f);
}