//---------------------
//    ch8_7.cpp
//---------------------
#include<iostream>
#include<cstdlib>   // �õ�mllaoc()
using namespace std;
//---------------------
int main()
{
	cout << "please input a number of array:\n";
	int aSize;    //Ԫ�ظ���
	cin >> aSize;

	int *ap = (int*)malloc(aSize*sizeof(int)); //���ڴ����

	for (int cnt = 0; cnt < aSize; cnt++)
		ap[cnt] = cnt * 2;
	for (int cnt = 0; cnt < aSize; cnt++)
		cout << ap[cnt] << "    ";

	cout << endl;
}//--------------------
