#include<iostream>
#include<ctime>
#include <iomanip>
#include<cmath>
using namespace std;

bool prime1(long n)					//����1����ͳ�����ж�������n�Ƿ�Ϊ����
{
	long i;
	for (i = 2;i < n;i++)
		if (n % i == 0)
			return false;
	return true;
}
void PrimeTime1(long n)				//ͳ�Ʒ���1����ʱ��
{
	clock_t t;
	long sum = 0;
	t = clock();
	for (int i = 2;i <= n;i++)
		if (prime1(i))				//��prime1�������ж�
			sum++;
	t = clock() - t;
	cout << "����1��" << endl;
	cout << "	�����2~" << n << "������������" << sum << endl;
	cout << "	��ʱ��" << fixed << setprecision(6) << (float(t) / CLOCKS_PER_SEC) << "��" << endl;
}
bool prime2(long n)					//����2���Ľ������ж�������n�Ƿ�Ϊ����
{
	for (long i = 2;i <= int(sqrt(n)); i++)
		if (n % i == 0)
			return false;
	return true;
}
void PrimeTime2(long n)				//ͳ�Ʒ���2����ʱ��
{
	clock_t t;
	long sum = 0;
	t = clock();
	for (int i = 2;i <= n;i++)
		if (prime2(i))				//��prime2�������ж�
			sum++;
	t = clock() - t;
	cout << "����2��" << endl;
	cout << "	�����2~" << n << "������������" << sum << endl;
	cout << "	��ʱ��" << fixed << setprecision(6) << (float(t) / CLOCKS_PER_SEC) << "��" << endl;
}
int main()							//������
{
	long n;
	cout << "n(����100000)��";
	cin >> n;
	if (n < 100000)
		return 0;
	PrimeTime1(n);					//����PrimeTime1����
	PrimeTime2(n);					//����PrimeTime2����
	return 1;
}
