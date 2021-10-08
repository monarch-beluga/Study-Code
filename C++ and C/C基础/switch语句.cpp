#include <stdio.h>
int main()		//计算器
{
	int b,c;
	char a;
	scanf("%d%c%d",&b,&a,&c);
	switch(a)
	{
		case '-':printf("%d%c%d = %d",b,a,c,b-c);break;
		case '+':printf("%d%c%d = %d",b,a,c,b+c);break;
		case '*':printf("%d%c%d = %d",b,a,c,b-c);break;
		case '/':printf("%d%c%d = %d",b,a,c,b-c);break;
		default:printf("只能进行加减乘除！");
	}
	return 0;
}
/*#include <stdio.h>		//分数
int main()
{
	int b,c;
	printf("输入分数：");
	scanf("%d",&c);
	if(c>=0&&c<=100)
	{
		b = c/10;
		switch(b)
		{
			case 10:
			case 9:printf("优秀\n");break;
			case 8:printf("良好\n");break;
			case 7:printf("中等\n");break;
			case 6:printf("及格\n");break;
			default:printf("不及格\n");
		}
	}
	else
		printf("格式不正确！\n");
	return 0;
}
*/