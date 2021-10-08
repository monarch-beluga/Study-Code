#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	fstream in("file1.txt", ios::in);
	if (!in)
	{
		cerr << "Error open file";
		return 1;
	}
	fstream out("file2.txt", ios::out);
	if (!out)
	{
		cerr << "Error open file";
		return 2;
	}
	char ch;
	while ((ch = in.get()) != EOF)
		out << char(toupper(ch));

	in.close();
	out.close();

	return 0;
}