#include<stdio.h>
#include<string.h>		//����strcmp��strcpy����
int main()
{
	char a[11]={"I am a boy"};		//�ַ��������ַ�����ʽ��ֵ
	char b[]="a boy";
	if(strcmp(a,b)==0)printf("���\n");//strcmp�Ƚ��ַ����Ƿ����
	else puts("�����");
	(strcpy(a,b));			//strcpy��������ַ����鸴�Ƹ�ǰ���
	puts(a),puts(b);
	if(strcmp(a,b)==0)printf("���\n");
	else puts("�����");
	return 0;
}