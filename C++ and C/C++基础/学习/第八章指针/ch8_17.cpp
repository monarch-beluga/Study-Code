//---------------------
//    ch8_17.cpp
//---------------------
#include<iostream>
using namespace std;
//---------------------
int main()
{
	char buffer[10] = "ABC ";
	char* pc;
	pc = "hello";   //ok: ���ַ����������׵�ַ����ָ��
	cout<<pc<<endl;
	pc++;
	cout<<pc<<endl;
	cout<<*pc<<endl;
	pc=buffer;
	cout<<pc<<endl;
}//--------------------
