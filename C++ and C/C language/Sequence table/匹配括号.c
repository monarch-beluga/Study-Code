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
	int flag = 1;
	printf("�����ַ�, �س�������\n");
	L.length = 0;
	while((ch = getchar()) != '\n')      // ��ȡ����̨������ַ����жϻس����� 
	{
		if (flag)
		{
			if (L.length == 0)
			{
				L.chs[0] = ch;
				L.length++;
			}
			else 
			{
				switch(ch)
				{
					case '(':
					case '[':
					case '{':
						L.chs[L.length]=ch; L.length++;break;
					case ')':
						if (L.chs[L.length-1]=='(')
							L.length--;
						else
							flag=0;
						break;
					case ']':
						if (L.chs[L.length-1]=='[')
							L.length--;
						else
							flag=0;
						break;
					case '}':
						if (L.chs[L.length-1]=='{')
							L.length--;
						else
							flag=0;
						break;
				}
			}
		}
		else
			continue;
	};
	if ((!L.length)&&flag)
		printf("����Ϸ�����\n");
	else
		printf("���벻�Ϸ�����\n");
	return 0;
}