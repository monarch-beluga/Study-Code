#include <stdio.h>		//读写文件中的数据块
{
	char a[][4] = {"六"},b[1][4];
	FILE *fp;
	fp = fopen("E:\\study\\a.txt","w");
	fwrite(a,4,1,fp);			//fwrite写出的文件不能直接用记事本打开查看
	fclose(fp);
	fp = fopen("E:\\study\\a.txt","r");
	fread(b,4,1,fp);			//读取
	printf("%s",b[0]);
	fclose(fp);
	return 0;
}
/*
#include<stdio.h>		//读写文件中的字符串
int main()
{
	FILE *fp;
	char a[9];
	fp = fopen("E:\\study\\a.txt","w");
	fputs("我爱中国\n",fp);			//写入
	fclose(fp);
	fp = fopen("E:\\study\\a.txt","r");
	for(;fgets(a,8,fp)!=NULL;)		//读取
		printf("%s",a);
	fclose(fp);
	return 0;
}
#include<stdio.h>		//对文件格式化读写函数
int main()
{
	FILE *fp;
	char a[13] = {"我爱中国"},b[13];
	fp = fopen("E:\\study\\a.txt","r+");
	fprintf(fp,"%s",a);			//写入
	fclose(fp);
	fp = fopen("E:\\study\\a.txt","r+");
	fscanf(fp,"%s",b);
	printf("%s",b);			//读取
	fclose(fp);
	return 0;
}
*/