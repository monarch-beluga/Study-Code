#include "学生类型.h"
#include<windows.h>

// 自定义函数声明
void Menu();						// 菜单界面函数
void Menu_select();				// 菜单界面选择函数
void Print_student(int i);			// 按顺序表数字打印学生信息函数
void Print_students();				// 打印所有学生信息函数
int Lookup(char num[]);				// 按学号查询学生顺序表数字
void Lookup_student();				// 按学号打印学生信息
void Modify_student();				// 修改学生信息
ElemType Add();						// 学生信息输入
void Add_student();					// 添加学生信息
void Delect_student();				// 删除学生信息
void Insert_student();				// 插入学生信息
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
	printf("*\t6-插入一个学生信息\t*\n");
	printf("*\t0-退出系统\t\t*\n");
	printf("*********************************\n");
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
		case 4:Add_student(Students.length);break;
		case 5:Delect_student();break;
		case 6:Insert_student();break;
		case 0:Exit_system();
	}
	// 按下后继续
	system("pause");
	// 执行完一次选择后重新回到菜单界面
	Menu();
}

void Print_student(int i)
{ 
	// 按顺序表的位置打印单个学生信息
	printf("姓名:%s\n",Students.elem[i].name);
	printf("学号:%s\n",Students.elem[i].num); 
	printf("专业班级:%s\n",Students.elem[i].classname); 
	printf("成绩:%d\n",Students.elem[i].score);
}
void Print_students()
{
	int i = 0;
	// 循环打印多个学生信息
	while(i < Students.length)
	{
		printf("\t学生%d\n",i+1);
		Print_student(i);
		printf("\n");
		i++;
	}
}

int Lookup(char num[])							// 按学号查找对应学生在顺序表的位置
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
	if (i < Students.length)				// 查找成功则打印该学生信息
		Print_student(i);
	else									// 学号错误
		printf("查找错误，没有该学生学号。");
}

void Modify_student()
{
	int i;
	char num[13];
	printf("请输入需要修改学生的学号:\n");
	scanf("%s",num);
	i = Lookup(num);						// 修改学生信息前先要查询学生位置
	if (i < Students.length)				// 如果该学号存在执行修改
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
		save++;								// 表示学生信息顺序表修改过一次，sava大于0则在退出程序时会将顺序表重新写入文件
	}										// 不存在则提醒
	else
		printf("查找错误，没有该学生学号。");
}

ElemType Add()
{
	int i;
	ElemType student;						// 声明学生结构体用于添加学生
	// 输入学生信息
	printf("请输入学生名字:\n");
	scanf("%s",student.name);
	printf("请输入学生专业班级:\n");
	scanf("%s",student.classname);
	while(1)
	{
		printf("请输入学生学号:\n");
		scanf("%s",student.num);
		// 判断学生学号是否与之前的学号重复
		i = Lookup(student.num);
		if (i < Students.length)
			printf("添加失败，该学号已存在\n");
		else
			break;
	}
	printf("请输入学生成绩:\n");
	scanf("%d",&student.score);
	return student;
}

void Add_student()
{
	// 往顺序表最后面插入学生信息
	Students.elem[Students.length] = Add();
	Students.length++;
	save++;
}

void Delect_student()
{
	int i;
	int flag;
	// 按学号查找需要删除的学生信息
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
			save++;
		}
	}
	else
		printf("查找错误，没有该学生学号。");
}

void Insert_student()
{
	int position;
	ElemType student;
	ElemType temp;
	while(1)
	{
		printf("当前学生人数为%d,请输入需要插入的位置:\n", Students.length);
		scanf("%d", &position);
		if(position > Students.length || position < 1)
			printf("位置不和法，请输入1~%d中的数字:\n", Students.length+1);
		else
			break;
	}
	student = Add();					// 获取学生信息
	for (int i = Students.length; i >= position; --i)		// 调整顺序表
		Students.elem[i] = Students.elem[i-1];
	Students.elem[position-1] = student;
	Students.length++;
	save++;
}

void Exit_system()
{
	if(save != 0)						// 判断顺序表是否发生改变
		SaveInFile();
	exit(0);							// 退出程序
}

void SaveInFile()
{
	int i = 0;
	FILE *f = fopen("Students.txt","w");							// 使用相对路径建立文件
	while(i < Students.length)										// 循环写出学生信息
	{
		fprintf(f, "%s\t", Students.elem[i].name);
		fprintf(f, "%s\t", Students.elem[i].num);
		fprintf(f, "%s\t", Students.elem[i].classname);
		fprintf(f, "%d\n", Students.elem[i].score);
		i++;
	}
	fclose(f);														// 关闭文件
}