#ifndef INTYR_H_
#define INTYR_H_
#pragma once
#include<Windows.h>
void set1(int x, int y)
{
    COORD coord;
    coord.X = y;
    coord.Y = x;
    HANDLE ConsoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleCursorPosition(ConsoleHandle, coord);
}
#endif