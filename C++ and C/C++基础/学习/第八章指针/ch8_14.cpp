//---------------------
//    ch8_14.cpp
//---------------------
#include<iostream>
using namespace std;
//---------------------
int* getInt(char* str)
{    //ָ�뺯��
	int value = 20;
	cout << str << endl;
	return &value;    //warning: ���ֲ������ĵ�ַ�����ǲ��׵�
}//--------------------
void somefn(char* str)
{
	int a = 40;
	cout << str << endl;
}//--------------------
int main()
{
	int* pr = getInt("input a value:");    //��ֵȡ�Է��ص�ָ��ֵ
	cout << *pr << endl;           //��һ�����*pr
	somefn("It is uncertain.");
	cout << *pr << endl;            //�ڶ������*pr
}//--------------------
