#include<iostream>
#include<ctime>
#include <iomanip>
#include<cmath>
using namespace std;

long add1(long n)					//����1��forѭ���ۼӷ�
{
	long sum = 0;
	for (int i = 1;i <= n;i++)
		sum += i;
	return sum;
}
void AddTime1(long n)				//����1����ʱ��ͳ��
{
	clock_t t;
	long sum;
	t = clock();
	sum = add1(n);					//����add1����
	t = clock() - t;				//���㷽��2����ʱ��
	cout << "����1��" << endl;
	cout << "	�����1~" << n << "֮�ͣ�" << sum << endl;
	cout << "	��ʱ��" << fixed << setprecision(6) << (float(t) / CLOCKS_PER_SEC) << "��" << endl;
}
long add2(long n)					//����2����˹��
{
	return n * (n + 1) / 2;
}
void AddTime2(long n)				//����2����ʱ��ͳ��
{
	clock_t t;
	long sum;
	t = clock();
	sum = add2(n);					//����add2����
	t = clock() - t;				//���㷽��2����ʱ��
	cout << "����2��" << endl;
	cout << "	�����1~" << n << "֮�ͣ�" << sum << endl;
	cout << "	��ʱ��" << fixed << setprecision(6) << (float(t) / CLOCKS_PER_SEC) << "��" << endl;
}

int main()							//������
{
	int n;
	cout << "n(����1000000)��";
	cin >> n;
	if (n < 1000000)
		return 0;
	AddTime1(n);						//����AddTime1����
	AddTime2(n);						//����AddTime2����
	return 1;
}

