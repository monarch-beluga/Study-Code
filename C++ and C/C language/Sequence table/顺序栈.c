#include <stdio.h>

typedef struct
{
	char chs[100];
	int length;
}List;

List L;

int main()
{
	int i;
	char ch; 
	printf("输入字符, 回车结束：\n");
	while((ch = getchar()) != '\n')      // 读取控制台输入的字符，判断回车结束 
	{
		L.chs[L.length] = ch;
		L.length++;
	};
	printf("输出：\n");
	while(L.length > 0)
	{
		printf("%c", L.chs[L.length-1]);		// 出栈 ：先入后出 
		L.length--;
	}
	return 0;
}