#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ofstream pout("stock.txt");
	if (!pout)
	{
		cout << "cannot open phone file\n";
		return 1;
	}
	pout << "shen fa zhan 000001\n";
	pout << "shanghai qi che 600104\n";
	pout << "Guang ju neng yuan 000096\n";

	pout.close();

	cout << "д����ɣ���� stock.txt �ļ��鿴��\n";
	return 0;
}