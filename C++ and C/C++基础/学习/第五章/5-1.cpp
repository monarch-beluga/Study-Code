#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

bool isprime(long n)
{
	int sqrtm = sqrt((long double)n);
	for(int i=2; i<=sqrtm; i++)
		if(n%i==0)
			return false;
	return true;
}

int main()
{
	long a, b, l=0;
	cout << "please input two numbers:\n";
	cin >> a >> b;
	cout << "primes from " << a << " to " << b << " is:\n";
	if (a % 2 == 0) a++;
	for (long m=a; m<=b; m+=2)
		if(isprime(m))
		{
			if(l++%10 == 0)
				cout << endl;
			cout << setw(5) << m;
		}
	cout << endl;
	return 0;
}