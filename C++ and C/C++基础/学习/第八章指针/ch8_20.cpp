//---------------------
//    ch8_20.cpp
//---------------------
#include<iostream>
using namespace std;
//---------------------
void print(char* [], int);
//---------------------
int main()
{
    char* pn[] = { "Fred","Barney","Wilma","Betty" };
    int num = sizeof(pn) / sizeof(char*);
    print(pn, num);
}//--------------------
void print(char* arr[], int len)
{
    for (int i = 0; i < len; i++)       //������ַ���
        cout << (int)arr[i] << "  "    //����ַ�����ַ��
             << arr[i] << endl;           //����ַ���
}//--------------------
