//---------------------
//    ch8_2.cpp
//---------------------
#include<iostream>
using namespace std;
//---------------------
int main()
{
	int iCount = 18;
	int* iPtr = &iCount;
	*iPtr = 58;

	cout << iCount << endl;
	cout << iPtr << endl;
	cout << &iCount << endl;  //��iPtrֵ��ͬ
	cout << *iPtr << endl;    //��iCountֵ��ͬ
	cout << &iPtr << endl;    //ָ�뱾��ĵ�ַ
}//--------------------
