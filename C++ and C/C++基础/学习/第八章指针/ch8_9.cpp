//---------------------
//    ch8_9.cpp
//---------------------
#include<iostream>
using namespace std;
//---------------------
int main()
{
	cout << "please input a number of array:\n";
	int aSize;    //Ԫ�ظ���
	cin >> aSize;
	int* array = new int[aSize];  //������ڴ�

	for (int i = 0; i < aSize; i++)
		array[i] = i * 2;
	for (int i = 0; i < aSize; i++)
		cout << array[i] << "  ";

	cout << endl;
	delete[] array;        //�ͷŶ��ڴ�
}//--------------------
