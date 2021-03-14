#include<iostream>
using namespace std;

#include<string>
#include<vector>
#include<algorithm>

int main()
{
	vector<char> alphaVector;
	for (int i = 0; i < 8; i++)
		alphaVector.push_back(i + 65);
	
	int size = alphaVector.size();
	vector<char>::iterator thelterator;

	for (int j = 0; j < size; j++)
	{
		alphaVector.pop_back();
		for (thelterator = alphaVector.begin(); thelterator != alphaVector.end(); thelterator++)
			cout << *thelterator;
		cout << endl;
	}
	return 0;
}