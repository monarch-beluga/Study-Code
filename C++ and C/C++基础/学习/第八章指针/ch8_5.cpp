//---------------------
//    ch8_5.cpp
//---------------------
#include<iostream>
using namespace std;
//---------------------
int main()
{
    int iArray[10];
    int* iPtr=iArray;    //��������iArray��ָ���ʼ��

    for (int i = 0; i < 10; i++)    //�����鸳ֵ
        iArray[i] = i * 2;
    for (int idx = 0; idx < 10; idx++, iPtr++) //�ۼ�����Ԫ��
        cout << "&Array[" << idx << "]:" << iPtr
        << "=>" << *iPtr << endl;
}//--------------------
