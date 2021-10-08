#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void get_next(string b, int next[])   // next算法
{
    int i = 0;
    int j = -1;
    next[0] = -1;
    while(i < (int)b.length())
    {
        if (j == -1 || b[i] == b[j])
        {
            j++;
            i++;
            next[i] = j;
        }
        else
            j = next[j];
    }
}
void get_nextval(string b, int nextval[])           // next修正值算法
{
    int i = 0;
    int j = -1;
    nextval[0] = -1;
    while(i < (int)b.length())
    {
        if (j == -1 || b[i] == b[j])
        {
            j++;
            i++;
            if (b[i] == b[j])
                nextval[i] = nextval[j];
            else
                nextval[i] = j;
        }
        else
            j = nextval[j];
    }
}
int Index(string a, string b, int poe)          // KMP算法
{
    int i = poe;
    int j = 0;
    int nextval[b.length()];
    int n = 0;
    get_nextval(b, nextval);
    while((i < (int)a.length()) && (j < (int)b.length()))
    {
        n++;
        if (j == -1 || a[i] == b[j]) 
        {
            i++;
            j++;
        }
        else
            j = next[j];
    }
    cout << n << endl;
    if (j >= (int)b.length())
        return (i - b.length());
    return -1;
}

int main()
{
    string a = "baaabaaaab";
    string b = "aaaab";
    cout << Index(a, b, 0) << endl;
}