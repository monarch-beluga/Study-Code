#include <stdio.h>
#include <windows.h>
int main(){
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, 0x27 );
    printf("C语言中文网\n");
    return 0;
}
//0 = 黑色    8 = 灰色    1 = 淡蓝      9 = 蓝色
//2 = 淡绿    A = 绿色    3 = 湖蓝      B = 淡浅绿  
//C = 红色    4 = 淡红    5 = 紫色      D = 淡紫  
//6 = 黄色    E = 淡黄    7 = 白色      F = 亮白