/*
方法一：
    1.使用log10计算和的位数
    2.然后根据位数整除获取截取的位数正向输出
*/
#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int a, b, sum, bt, t, p;
    cin >> a >> b;
    sum = a + b;
    if(sum < 0)
    {
    	sum = -sum;
    	cout << "-";
    }
    if (sum < 1000)
    	cout << sum;
    else
    {
        bt = log10(sum);
        a = bt / 3;
        for(int i = a; i > 0; i--)
        {
            p = pow(1000, i);
            t = sum / p;
            sum = sum % p;
            if (i == a)
                printf("%d,", t);
            else
                printf("%03d,", t);
        }
    	printf("%03d", sum);
    }
    return 0;
}

/*
方法二：
    每次截取最后一位，然后通过栈（先进后出）输出
*/
#include<iostream>
using namespace std;

int main()
{
    char num[9];
    int n;
    int a, b, sum;
    cin >> a >> b;
    sum = a+b;
    if(sum < 0)
    {
        cout << '-';
        sum = -sum;
    }
    n = -1;
    if(sum == 0)
        cout << 0;
    else
    {
        while(sum > 0)
        {
            num[++n]='0'+(sum%10);
            sum /= 10;
            if((n-(n-n/3)/3+1)%3==0 && sum>0)
                num[++n]=',';
        }
        for(int i = n; i >= 0; i--)
            cout << num[i];
    }
    return 0;
}


