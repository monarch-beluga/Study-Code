//---------------------
//    ch8_6.cpp
//---------------------
#include<iostream>
using namespace std;
//---------------------
int iArray[]={1,4,2,7,13,32,21,48,16,30};    //ȫ������
//---------------------
int main()
{
    int sum1=0,sum2=0,sum3=0,sum4=0,sum5=0;//���ÿ�ַ����Ľ��
    int size = sizeof(iArray)/sizeof(*iArray);    //Ԫ�ظ���
    for (int n = 0; n < size; n++)    //����1
        sum1 += iArray[n];

    int* iPtr = iArray;
    for (int n = 0; n < size; n++)    //����2
        sum2 += *iPtr++;

    iPtr=iArray;       //�˾䲻��ʡ�ԣ���Ϊ����2�޸���iPtr
    for (int n = 0; n < size; n++)    //����3
        sum3 += *(iPtr + n);

    iPtr=iArray;      //�˾����ʡ�ԣ���Ϊ����3û���޸�iPtr
    for (int n = 0; n < size; n++)    //����4
        sum4 += iPtr[n];

    for (int n = 0; n < size; n++)    //����5
        sum5 += *(iArray + n);

    cout << sum1 << endl
        << sum2 << endl
        << sum3 << endl
        << sum4 << endl
        << sum5 << endl;
}//--------------------
