#include <stdio.h>		//��д�ļ��е����ݿ�
{
	char a[][4] = {"��"},b[1][4];
	FILE *fp;
	fp = fopen("E:\\study\\a.txt","w");
	fwrite(a,4,1,fp);			//fwriteд�����ļ�����ֱ���ü��±��򿪲鿴
	fclose(fp);
	fp = fopen("E:\\study\\a.txt","r");
	fread(b,4,1,fp);			//��ȡ
	printf("%s",b[0]);
	fclose(fp);
	return 0;
}
/*
#include<stdio.h>		//��д�ļ��е��ַ���
int main()
{
	FILE *fp;
	char a[9];
	fp = fopen("E:\\study\\a.txt","w");
	fputs("�Ұ��й�\n",fp);			//д��
	fclose(fp);
	fp = fopen("E:\\study\\a.txt","r");
	for(;fgets(a,8,fp)!=NULL;)		//��ȡ
		printf("%s",a);
	fclose(fp);
	return 0;
}
#include<stdio.h>		//���ļ���ʽ����д����
int main()
{
	FILE *fp;
	char a[13] = {"�Ұ��й�"},b[13];
	fp = fopen("E:\\study\\a.txt","r+");
	fprintf(fp,"%s",a);			//д��
	fclose(fp);
	fp = fopen("E:\\study\\a.txt","r+");
	fscanf(fp,"%s",b);
	printf("%s",b);			//��ȡ
	fclose(fp);
	return 0;
}
*/