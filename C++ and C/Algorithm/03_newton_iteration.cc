#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

// 牛顿迭代实现开平方  ----->   f(x) = x^2 - n
int NewtonSqurt(int num);
// 牛顿迭代拓展：实现求得方程 f(x) = x^3 - n 的解
double NewtonSolvingEquations(double num);

int main()
{
	int num;
	int square;
	cout << "Please enter the number to be squared:" << endl;
	cin >> num;
	square = NewtonSqurt(num);
	cout << "num integer part of square root: " << square << endl;

	// -----------------------------------------------------------
	cout << "Please enter the number:" << endl;
	double fnum, solution;
	cin >> fnum;
	solution = NewtonSolvingEquations(fnum);			// 100
	cout << "Solution of the equation: " << solution << endl;
	return 0;
}

int NewtonSqurt(int num)
{
	if (num < 1)
		return 0;
	else if (num < 4)
		return 1;
	else
	{
		double i, res = 2;
		while((int)res != (int)i)
		{
			i = res;
			res = (i * i + num) / (2 * i);
			// cout << fixed << setprecision(16) << res << endl;
		}
		return (int)res;
	}
}
/*
牛顿迭代法的原理：
先假设一个X0，并求X0与f(x)得切线L0
然后得到L0与x轴得交点X1
然后求X1与f(x)得切线L1，得到L1与x轴得交点X2……
每一次得到得Xn都会更加逼近与方程f(x)=0的解
直到Xn 与 Xn+1 的值相等，或达到一个特定的精度时，迭代结束
上述为牛顿迭代的几何原理，而转化为数学则为：
使用线性近似公式，也就是泰勒公式的一阶展开，得：
f(x) = f(x0) + f'(x0)*(x - x0)
设上述公式所得的解为x1，则可得
x1 = x0 - f(x0)/f'(x0)
同理，新得到的x1比x0更接近x
由此可得： Xn+1 = Xn - f(Xn)/f'(Xn)
将 f(x) = x^2 - n带入其中，得：
Xn+1 = Xn - (Xn^2 - n)/(2 * Xn) = (Xn^2 + n)/(2 * Xn) 
*/

double NewtonSolvingEquations(double num)
{
	double i;
	double res = 2.0;
	while(abs(res-i) >= 1e-15 || res != i)
	{
		i = res;
		res = i - (i*i*i + i*i - num) / (3*i*i + 2*i*i);
		// cout << fixed << setprecision(16) << res << endl;
	}
	return res;
}

