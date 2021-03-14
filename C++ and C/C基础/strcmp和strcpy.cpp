#include<stdio.h>
#include<string.h>		//定义strcmp、strcpy函数
int main()
{
	char a[11]={"I am a boy"};		//字符数组以字符串形式赋值
	char b[]="a boy";
	if(strcmp(a,b)==0)printf("相等\n");//strcmp比较字符串是否相等
	else puts("不相等");
	(strcpy(a,b));			//strcpy将后面的字符数组复制给前面的
	puts(a),puts(b);
	if(strcmp(a,b)==0)printf("相等\n");
	else puts("不相等");
	return 0;
}