#include <stdio.h>
int main()
{
	char ch;
	FILE *fp;			//FILE为定义一个文件类型指针
	fp = fopen("E:\\study\\a.txt","w");		//打开文件
	/*
	文本文件："r"(只读)		"w"(只写)	"a"(追加)
	二进制文件的符号是文本文件符号加b*/
	for (ch = 'A';ch<='Z';ch++) fputc(ch,fp);	//写字符函数
	fclose(fp);		//关闭指针
	fp = fopen("E:\\study\\a.txt","r");
	for(ch = fgetc(fp);ch != EOF;ch = fgetc(fp)) //读字符函数，只能读取字符
		putchar(ch);
	fclose(fp);
	return 0;
}