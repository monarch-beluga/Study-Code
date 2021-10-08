#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	fstream in;
	in.open("file4.txt", ios::in);
	if (!in)
	{
		cerr << "Error open file";
		return 1;
	}
	fstream out;
	out.open("file41.txt", ios::out);
	if (!out)
	{
		cerr << "Error open file";
		return 1;
	}

	char ch;
	while ((ch = in.get()) != EOF)
		out << ch;

	in.close();
	out.close();
	cout << "文件操作执行完毕" << endl;

	return 0;
}