#include <stdio.h>
#include <windows.h>
int main(){
    //������λ��
    COORD coord;
    coord.X = 3;  //��3��
    coord.Y = 3;  //��3��
    //��ȡ����̨���������
    HANDLE ConsoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    //���ù��λ��
    SetConsoleCursorPosition(ConsoleHandle, coord);
	printf("123");
    return 0;
}