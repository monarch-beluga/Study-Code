#include <stdio.h>
#include <windows.h>
int main(){
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, 0x27 );
    printf("C����������\n");
    return 0;
}
//0 = ��ɫ    8 = ��ɫ    1 = ����      9 = ��ɫ
//2 = ����    A = ��ɫ    3 = ����      B = ��ǳ��  
//C = ��ɫ    4 = ����    5 = ��ɫ      D = ����  
//6 = ��ɫ    E = ����    7 = ��ɫ      F = ����