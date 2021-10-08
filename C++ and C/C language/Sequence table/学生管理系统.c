#include "ѧ������.h"
#include<windows.h>

// �Զ��庯������
void Menu();						// �˵����溯��
void Menu_select();				// �˵�����ѡ����
void Print_student(int i);			// ��˳������ִ�ӡѧ����Ϣ����
void Print_students();				// ��ӡ����ѧ����Ϣ����
int Lookup(char num[]);				// ��ѧ�Ų�ѯѧ��˳�������
void Lookup_student();				// ��ѧ�Ŵ�ӡѧ����Ϣ
void Modify_student();				// �޸�ѧ����Ϣ
ElemType Add();						// ѧ����Ϣ����
void Add_student();					// ���ѧ����Ϣ
void Delect_student();				// ɾ��ѧ����Ϣ
void Insert_student();				// ����ѧ����Ϣ
void Exit_system();					// �˳�ϵͳ
void SaveInFile();					// ��ѧ����Ϣ������ļ��б���

SqList Students;					// ����ȫ�ֱ���˳���
int save = 0;						// �ж�ѧ����Ϣ�Ƿ����

int main()
{
	// ѧ����Ϣ�ļ���ȡ
	int i = 0;
	FILE *f;
	f = fopen("Students.txt","r");
	if (f == NULL)					// ����ļ������ڣ��ʹ���һ���ļ�
		SaveInFile();
	else
	{
		while(!feof(f))				// ѭ����ȡ��Ϣ���ж��ļ���ȡ�Ƿ����
		{
			// �ļ���ȡ
			fscanf(f, "%s", Students.elem[i].name);
			fscanf(f, "%s", Students.elem[i].num);
			fscanf(f, "%s", Students.elem[i].classname);
			fscanf(f, "%d", &Students.elem[i].score);
			i++;
			// ÿ��ȡһ��˳����1
			Students.length++;
		}
		// ��Ϊfeof(f)�ļ���ȡ�����󻹻��ٶ�ȡһ�Σ�����Ҫ��˳����һ
		Students.length--;
	}

	// �˵���������ʼ����ѧ������ϵͳ
	Menu();
	return 0;
} 

void Menu()
{
	system("cls");					// ����
	// ��ӡ����
	printf("\n********ѧ���ɼ�����ϵͳ*********\n");
	printf("*\t1-�������ѧ����Ϣ\t*\n");
	printf("*\t2-��ѧ�Ų�ѯѧ����Ϣ\t*\n");
	printf("*\t3-�޸�ѧ������\t\t*\n");
	printf("*\t4-���һ��ѧ����Ϣ\t*\n");
	printf("*\t5-ɾ��һ��ѧ����Ϣ\t*\n");
	printf("*\t6-����һ��ѧ����Ϣ\t*\n");
	printf("*\t0-�˳�ϵͳ\t\t*\n");
	printf("*********************************\n");
	// �˵�ѡ��
	Menu_select();
}

void Menu_select()
{
	int a; 
	printf("��ѡ��<Select>:\n");
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
	// ���º����
	system("pause");
	// ִ����һ��ѡ������»ص��˵�����
	Menu();
}

void Print_student(int i)
{ 
	// ��˳����λ�ô�ӡ����ѧ����Ϣ
	printf("����:%s\n",Students.elem[i].name);
	printf("ѧ��:%s\n",Students.elem[i].num); 
	printf("רҵ�༶:%s\n",Students.elem[i].classname); 
	printf("�ɼ�:%d\n",Students.elem[i].score);
}
void Print_students()
{
	int i = 0;
	// ѭ����ӡ���ѧ����Ϣ
	while(i < Students.length)
	{
		printf("\tѧ��%d\n",i+1);
		Print_student(i);
		printf("\n");
		i++;
	}
}

int Lookup(char num[])							// ��ѧ�Ų��Ҷ�Ӧѧ����˳����λ��
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
	printf("��������Ҫ��ѯ��ѧ��:\n");
	scanf("%s",num);
	i = Lookup(num);
	if (i < Students.length)				// ���ҳɹ����ӡ��ѧ����Ϣ
		Print_student(i);
	else									// ѧ�Ŵ���
		printf("���Ҵ���û�и�ѧ��ѧ�š�");
}

void Modify_student()
{
	int i;
	char num[13];
	printf("��������Ҫ�޸�ѧ����ѧ��:\n");
	scanf("%s",num);
	i = Lookup(num);						// �޸�ѧ����Ϣǰ��Ҫ��ѯѧ��λ��
	if (i < Students.length)				// �����ѧ�Ŵ���ִ���޸�
	{
		Print_student(i);
		printf("�������޸ĺ�ѧ������:\n");
		scanf("%s",Students.elem[i].name);
		printf("�������޸ĺ�ѧ��רҵ�༶:\n");
		scanf("%s",Students.elem[i].classname);
		printf("�������޸ĺ�ѧ��ѧ��:\n");
		scanf("%s",Students.elem[i].num);
		printf("�������޸ĺ�ѧ���ɼ�:\n");
		scanf("%d",&Students.elem[i].score);
		save++;								// ��ʾѧ����Ϣ˳����޸Ĺ�һ�Σ�sava����0�����˳�����ʱ�Ὣ˳�������д���ļ�
	}										// ������������
	else
		printf("���Ҵ���û�и�ѧ��ѧ�š�");
}

ElemType Add()
{
	int i;
	ElemType student;						// ����ѧ���ṹ���������ѧ��
	// ����ѧ����Ϣ
	printf("������ѧ������:\n");
	scanf("%s",student.name);
	printf("������ѧ��רҵ�༶:\n");
	scanf("%s",student.classname);
	while(1)
	{
		printf("������ѧ��ѧ��:\n");
		scanf("%s",student.num);
		// �ж�ѧ��ѧ���Ƿ���֮ǰ��ѧ���ظ�
		i = Lookup(student.num);
		if (i < Students.length)
			printf("���ʧ�ܣ���ѧ���Ѵ���\n");
		else
			break;
	}
	printf("������ѧ���ɼ�:\n");
	scanf("%d",&student.score);
	return student;
}

void Add_student()
{
	// ��˳�����������ѧ����Ϣ
	Students.elem[Students.length] = Add();
	Students.length++;
	save++;
}

void Delect_student()
{
	int i;
	int flag;
	// ��ѧ�Ų�����Ҫɾ����ѧ����Ϣ
	char num[13];
	printf("��������Ҫɾ��ѧ����ѧ��:\n");
	scanf("%s",num);
	i = Lookup(num);
	if (i < Students.length)
	{
		Print_student(i);
		printf("�Ƿ�ɾ����ѧ����0-��\t1-��\n");
		scanf("%d",&flag);
		if (flag)
		{
			for(;i<Students.length-1;i++)
			Students.elem[i] = Students.elem[i+1];
			Students.length--;
			printf("ɾ���ɹ�����\n");
			save++;
		}
	}
	else
		printf("���Ҵ���û�и�ѧ��ѧ�š�");
}

void Insert_student()
{
	int position;
	ElemType student;
	ElemType temp;
	while(1)
	{
		printf("��ǰѧ������Ϊ%d,��������Ҫ�����λ��:\n", Students.length);
		scanf("%d", &position);
		if(position > Students.length || position < 1)
			printf("λ�ò��ͷ���������1~%d�е�����:\n", Students.length+1);
		else
			break;
	}
	student = Add();					// ��ȡѧ����Ϣ
	for (int i = Students.length; i >= position; --i)		// ����˳���
		Students.elem[i] = Students.elem[i-1];
	Students.elem[position-1] = student;
	Students.length++;
	save++;
}

void Exit_system()
{
	if(save != 0)						// �ж�˳����Ƿ����ı�
		SaveInFile();
	exit(0);							// �˳�����
}

void SaveInFile()
{
	int i = 0;
	FILE *f = fopen("Students.txt","w");							// ʹ�����·�������ļ�
	while(i < Students.length)										// ѭ��д��ѧ����Ϣ
	{
		fprintf(f, "%s\t", Students.elem[i].name);
		fprintf(f, "%s\t", Students.elem[i].num);
		fprintf(f, "%s\t", Students.elem[i].classname);
		fprintf(f, "%d\n", Students.elem[i].score);
		i++;
	}
	fclose(f);														// �ر��ļ�
}