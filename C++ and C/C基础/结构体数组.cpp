#include<stdio.h>		//ͳ�ƺ���������߳ɼ�
#include<string.h>
struct person			//��ʼ���ṹ��
{
	char name[20];
	int count;
};
int main()
{
	struct person leader[3] = {{"li",0},{"liu",0},{"wan",0}},*p;		//����ṹ������
	char a[20];														//����ָ��
	int j;
	for (int i=0;i<3;i++)				//��ּ�ͳ��
	{
		printf("�����롰li������liu�����ߡ�wan����");
		scanf("%s",a);
		for(j=0;j<3;j++)
			if (strcmp(a,leader[j].name )== 0) leader[j].count++;
	}		//�ַ����ȽϺ�����strcmp����Ҫ��ͷ�ļ�string.h
	p  = leader;			//ָ�����ṹ������
	for(int i = 0;i<3;i++)			//���
		printf("%s	%d\n",p[i].name,p[i].count);
	return 0;
}
/*
#include<stdio.h>			//ͳ�ƺ��������߳ɼ�
#include<string.h>
struct person
{
	char name[20];
	int count;
};
int max(int a,int b,int c)
{
	if(a<b) a = b;
	if(a>c) return a;
	else return c;
}
int main()
{
	struct person leader[3] = {{"li",0},{"liu",0},{"wan",0}};
	char a[20];
	int j;
	for (int i=0;i<3;i++)
	{
		printf("�����롰li������liu�����ߡ�wan����");
		scanf("%s",a);
		for(j=0;j<3;j++)
			if (strcmp(a,leader[j].name )== 0) leader[j].count++;
	}
	for(int i = 0;i<3;i++)
	{
		if(leader[i].count == max(leader[0].count,leader[1].count,leader[2].count))
		printf("%s	%d\n",leader[i].name,leader[i].count);
	}
	return 0;
}
*/