#include<stdio.h>
#include<iostream>
#include<set>
using namespace std;

int main()
{
	set<int> a;
    set<int>::iterator it;
    a.insert(0);
    a.insert(1);
    for(it=a.begin(); it != a.end(); it++)
        *it += 2;
    for(it=a.begin(); it < a.end(); it++)
        cout << *it << endl;
    return 0;
}
 