#include<stdio.h>
#include<windows.h>

int main()
{
	char a;
	while(1)
	{
		a = getchar();
		if (a>'0'&&a<'5')
		{
			printf("%c", a);
			break;
		}
		else if(a != '\n')
			printf("ÖØÐÂÊäÈë\n");
	}
	return 0;
}