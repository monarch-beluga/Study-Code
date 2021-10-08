#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include<stdio.h>
#include<conio.h>
#include "ConHand.h"
using namespace std;

vector<string> text;

int main()
{
    int ch;
    while((ch = getch()) != 27)
    {
        switch(ch)
        {
            case 72:
                if (coord.Y > 0)
                    coord.Y--;
                break;
            case 80:
                if (coord.Y < text.size())
                    coord.Y--;
                break;
            case 75:
                if (coord.X < text[coord.Y].size())
                    coord.X++;
                break;
            case 77:
                if (coord.X > 0)
                    coord.X--;
                break;
            case 8:
                if (text[])
                {
                    /* code */
                }
        }
        SetConHand();
        // ch = getch();
        // printf("%d,", ch);
    }
}
