# include<iostream>
# include<cstdlib>
# include<cstring>
using namespace std;

int CompIntBitSum(const void *a, const void *b)
{
	int ia = *(int*)a, ib = *(int*)b;
	int suma = 0, sumb = 0;
	for(; ia; ia /=10)
		suma += ia % 10;
	for(; ib; ib /= 10)
		sumb += ib % 10;
	return suma - sumb;
}
int CompFloat(const void *a, const void *b)
{
	return *(float*)a - *(float*)b;
}
int CompStrLen(const void *a, const void *b)
{
	if(strlen(*(char**)a) == strlen(*(char**)b))
		return strcmp(*(char**)a, *(char**)b);
	return strlen(*(char**)a) - strlen(*(char**)b);
}

int main()
{
	int a[] = {12, 32, 42, 51, 8, 16, 21, 19, 9};
	int anum = sizeof(a) / sizeof(*a);
	cout << "\n ÅÅÐòÇ°:" << endl;
	for(int i = 0; i < anum; i++)
		cout << a[i] << " ";
	cout << endl;
	qsort(a, anum, sizeof(*a), CompIntBitSum);
	cout << "ÅÅÐòºó:" << endl;
	for(int i = 0; i < anum; i++)
		cout << a[i] << " ";
	cout << endl;

	float f[] = {32.1, 456.87, 332.67, 442.0, 98.12, 451.79, 340.12, 54.55, 99.87, 72.5};
	int fnum = sizeof(f) / sizeof(*f);
	cout << "\n ÅÅÐòÇ°:" << endl;
	for(int i = 0; i < fnum; i++)
		cout << f[i] << " ";
	cout << endl;
	qsort(f, fnum, sizeof(*f), CompFloat);
	cout << "ÅÅÐòºó:" << endl;
	for(int i = 0; i < fnum; i++)
		cout << f[i] << " ";
	cout << endl;

	const char *str[] = {"enter", "number", "size", "begin", "of", "cat", "case", "program", "certain", "a"};
	int strnum = sizeof(str) / sizeof(*str);
	cout << "\n ÅÅÐòÇ°:" << endl;
	for (int i = 0; i < strnum; i++)
		cout << str[i] << " ";
	cout << endl;
	qsort(str, strnum, sizeof(*str), CompStrLen);
	cout << "ÅÅÐòºó:" << endl;
	for (int i = 0; i < strnum; i++)
		cout << str[i] << " ";
	cout << endl;
	
	return 0;
}
