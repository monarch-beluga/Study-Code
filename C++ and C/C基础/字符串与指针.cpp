#include <stdio.h>
int f(char *p)			//定义统计小写字母的函数
{
	int sum=0;
	do
	{
		if(*p>='a' && *p<='z')
			//因为字符串的每一个元素都为字符，所以可以按ACSLL码来选择
			sum++;
		p++;
	}while(*p != '\0');		//字符串末尾为'\0'
	return sum;
}
int main()
{
	char a[50],*s = a;
	gets(a);
	printf("小写字母的个数为：%d\n",f(s));
	return 0; 
}