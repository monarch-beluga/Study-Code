//---------------------
//    ch8_15.cpp
//---------------------
#include<iostream>
#include<string.h>  //�õ�memcpy()
using namespace std;
//---------------------
int main()
{
	char src[10] = "*********";
	char dest[10];
	char* pc = (char*)memcpy(dest, src, 10);
	cout << pc << endl;
	return 0;
}//--------------------
