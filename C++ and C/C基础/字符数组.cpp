#include<stdio.h>
#include<string.h>		//����strlen����
int main()
{
	char a[11]={"I am a boy"};		//�ַ��������ַ�����ʽ��ֵ
	char b[]="I am a boy";
	char c[10];					//�����ַ������趨��洢����
	scanf("%s",c);		//���Բ���&
	printf("%s������%dռ%d�ֽ�\n",a,strlen(a),sizeof(a));		//strlenֻ�ܲ��ַ����ĳ���
	printf("%s������%dռ%d�ֽ�\n",b,strlen(b),sizeof(b));		//sizeof����ռ�ֽ���
	printf("%s",c);
	return 0;
}