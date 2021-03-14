#include <stdio.h>
#include <windows.h>
void set1(int x,int y)		//定义光标位置的函数
{
    COORD coord;
    coord.X = x-1;
    coord.Y = y;
    HANDLE ConsoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleCursorPosition(ConsoleHandle, coord);
}
int main()
{
	int x,y;
	while(1)
	{
		scanf("%d",&x);
		if(x == 0) break;
		scanf(",%d",&y);
		system("cls");
		set1(x,y);
		printf("*");
		Sleep(3000);
		system("cls");
	}
	return 0;
}