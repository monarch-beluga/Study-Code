#include <windows.h>
void set1(int x,int y)
{
    COORD coord;
    coord.X = x;
    coord.Y = y;
    HANDLE ConsoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleCursorPosition(ConsoleHandle, coord);
}
void frame()
{
	set1(30,0);
	for(int i=0;i<=44;i++)
	{
		if(i%2 == 0) printf("-");
		else printf("*");
	}
	set1(30,15);
	for(int i=0;i<=44;i++)
	{
		if(i%2 == 0) printf("-");
		else printf("*");
	}
	for(int i = 1;i<15;i++)
	{
		set1(30,i);
		printf("*");
		set1(74,i);
		printf("*");
	}
}