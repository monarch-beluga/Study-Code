# include<iostream>
using namespace std;

int *findmax(int *array, int size, int *index)
{
	*index = 0;
	for(int i = 0; i < size; i++)
		if(array[i] > array[*index])
			*index = i;
	return &array[*index];
}

int main()
{
	int a[10] = {39, 91, 54, 67, 82, 37, 85, 63, 19, 68};
	int *maxaddr;
	int idx;
	maxaddr = findmax(a, sizeof(a) / sizeof(*a), &idx);
	cout << "the index of maximum element is " << idx << endl
		 << "the address of it is " << maxaddr << endl
		 << "the value of it is " << a[idx] << endl;
	return 0;
}