#include<iostream>
using namespace std;
#include<vector>
#define Max 110
int main()
{
    int n, m, id, cs, c, count, s, e, t;
    cin >> n >> m;
    int sq[Max];
    vector<int> tree[Max];
    for (int i = 0; i < m; ++i)
    {
    	cin >> id >> cs;
    	for (int j = 0; j < cs; ++j)
    	{
    		cin >> c;
    		tree[id].push_back(c);
    	}
    }
    s = e = 0;
    sq[e++] = 1;
    while(s != e)
    {
    	if (s)
    		cout << " ";
    	count = 0;
    	t = e;
    	while(s != t)
    	{
    		int q = sq[s++];
    		cs = tree[q].size();
    		if (cs == 0)
    			count++;
    		else
    			for (int j = 0; j < cs; ++j)
    				sq[e++] = tree[q][j];
    	}
    	cout << count;
    }
    return 0;
}