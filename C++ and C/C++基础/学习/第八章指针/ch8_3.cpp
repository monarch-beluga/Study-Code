//---------------------
//    ch8_3.cpp
//---------------------
#include<iostream>
using namespace std;
//---------------------
int main()
{
    float f=34.5;
    float* fPtr=&f;         //����ָ��
    int* iPtr=(int*)&f;     //warning: ����������ĵ�ַ��������ָ��

    cout << f << endl
        << "iPtr:" << iPtr << "=>" << *iPtr << "\n"
        << "fPtr:" << fPtr << "=>" << *fPtr << "\n\n";
    *iPtr=*fPtr;            //��ʽ����ת��
    cout << f << endl
        << *iPtr << endl
        << *fPtr << endl;
}//--------------------
