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

	cout << "写入完成，请打开 stock.txt 文件查看！\n";
	return 0;
}