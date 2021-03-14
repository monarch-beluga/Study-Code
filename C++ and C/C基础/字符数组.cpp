#include<stdio.h>
#include<string.h>		//定义strlen函数
int main()
{
	char a[11]={"I am a boy"};		//字符数组以字符串形式赋值
	char b[]="I am a boy";
	char c[10];					//输入字符数组需定义存储容量
	scanf("%s",c);		//可以不用&
	printf("%s长度是%d占%d字节\n",a,strlen(a),sizeof(a));		//strlen只能测字符串的长度
	printf("%s长度是%d占%d字节\n",b,strlen(b),sizeof(b));		//sizeof测所占字节数
	printf("%s",c);
	return 0;
}