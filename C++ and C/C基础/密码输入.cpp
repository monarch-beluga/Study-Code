#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#define PWDLEN 20

void getpwd(char *pwd, int pwdlen);

int main(){
    char pwd[PWDLEN+1];
    printf("Input password: ");
    getpwd(pwd, PWDLEN);
    printf("The password is: %s\n", pwd);
    return 0;
}
void getpwd(char *pwd, int pwdlen){
    char ch = 0;
    int i = 0;
    while(i<pwdlen)
	{
        ch = getch();		//getch为无回显的字符输入，需要用conio.h头文件
        if(ch == '\r')
		{
            printf("\n");
            break;
		}
        if(ch=='\b' && i>0)
		{ 
            i--;
            printf("\b \b");
        }
		else if(isprint(ch))	//isprint为判断是否为可打印字符，包含在ctype.h头文件中
		{ 
            pwd[i] = ch;
            printf("*");
            i++;
        }
    }
    pwd[i] = 0;
}