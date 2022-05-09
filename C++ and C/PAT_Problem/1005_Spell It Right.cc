#include<iostream>
using namespace std;
#include<cmath>
#include<string>

int main()
{
    int sum = 0, b, a;
    char ch;
    string s[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    while((ch=cin.get()) != '\n')
    	sum += ch - '0';
    if (sum < 10)
    	cout << s[sum];
    else
    {
    	b = log10(sum);
	    for (int i = b; i >= 0; i--)
	    {
	    	a = sum / (int)pow(10, i);
	    	sum = sum % (int)pow(10, i);
	    	cout << s[a];
	    	if(i)
	    		cout << " ";
	    }
    }
    return 0;
}