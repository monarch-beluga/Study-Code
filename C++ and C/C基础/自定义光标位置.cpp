#include <stdio.h>
#include <windows.h>
int main(){
    //定义光标位置
    COORD coord;
    coord.X = 3;  //第3行
    coord.Y = 3;  //第3列
    //获取控制台缓冲区句柄
    HANDLE ConsoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    //设置光标位置
    SetConsoleCursorPosition(ConsoleHandle, coord);
	printf("123");
    return 0;
}