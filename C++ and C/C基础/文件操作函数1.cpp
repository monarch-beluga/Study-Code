#include <stdio.h>
int main()
{
	char ch;
	FILE *fp;			//FILEΪ����һ���ļ�����ָ��
	fp = fopen("E:\\study\\a.txt","w");		//���ļ�
	/*
	�ı��ļ���"r"(ֻ��)		"w"(ֻд)	"a"(׷��)
	�������ļ��ķ������ı��ļ����ż�b*/
	for (ch = 'A';ch<='Z';ch++) fputc(ch,fp);	//д�ַ�����
	fclose(fp);		//�ر�ָ��
	fp = fopen("E:\\study\\a.txt","r");
	for(ch = fgetc(fp);ch != EOF;ch = fgetc(fp)) //���ַ�������ֻ�ܶ�ȡ�ַ�
		putchar(ch);
	fclose(fp);
	return 0;
}