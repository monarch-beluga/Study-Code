#include<iostream>
#include <iomanip>
using namespace std;

long Sum(int n)						//�������������׳˺�
{
	long sum = 0, fact = 1;
	for (int i = 1;i <= n;i++)
	{
		fact *= i;					//�����factΪi��
		sum += fact;				//�����sumΪ1! + 2! + ���� + i!
	}
	return sum;
}
int main()							//������
{
	int n;
	cout << "n(3 - 20):";
	cin >> n;
	if (n < 3 || n>20)
		return 0;
	cout << "1! + 2! + ���� + " << n << "!= " << Sum(n) << endl;			//����Sum����
	return 1;
}
