# include<iostream>
using namespace std;

int num, interval;
bool assign()
{
	while(1)
	{
		cout << "please input the number of boys, the interbal:" << endl;
		cin >> num >> interval;
		if(num > 1 && interval > 1 && interval < num)
			return true;
		bool sign = true;
		while(sign)
		{
			cout << "error on your input data." << endl;
			cout << "please select following operation£º" << endl;
			cout << "\t\tstop at once! -----1" << endl;
			cout << "\t\tinput again. ------2" << endl;
			cout << "\t\tas default values -3\n" << endl;
			int sele = 0;
			cin >> sele;
			switch(sele)
			{
				case 1: return false;
				case 2: sign = false; break;
				case 3: num = 10; interval = 3; return true;
			}
		}
	}
}

int main()
{
	if(!assign())
		return 1;
	int *a = new int[num];
	for(int i = 0; i < num; i++)
		cout << (a[i] = i+1) << ",";
	cout << endl;
	int i = (interval - 1) % num;
	for(int k = 1; k < num; k++)
	{
		cout << a[i] << ",";
		a[i] = 0;
		for(int j = 1; !(a[i] && (j++ == interval)); i = (i+1) % num);
	}
	cout << "\nNo." << a[i] << " boy has won." << endl;
	delete []a;
}

