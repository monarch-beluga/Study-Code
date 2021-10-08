#include<iostream>
using namespace std;

class Matrix
{
public:
	Matrix();
	friend Matrix operator+(Matrix&, Matrix&);
	friend ostream& operator<<(ostream&, Matrix&);
	friend istream& operator>>(istream&, Matrix&);

private:
	int mat[2][3];

};

Matrix::Matrix()
{
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 3; j++)
			mat[i][j] = 0;
}

Matrix operator+(Matrix &a, Matrix &b)
{
	Matrix c;
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 3; j++)
			c.mat[i][j] = a.mat[i][j] + b.mat[i][j];
	return c;
}

istream& operator>>(istream &in, Matrix &m)
{
	cout << "input value of matrix: " << endl;
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 3; j++)
			in >> m.mat[i][j];
	return in;
}

ostream &operator<< (ostream &out, Matrix &m)
{

	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 3; j++)
			out << m.mat[i][j] << "\t";
		out << endl;
	}
	return out;
}

int main()
{
	Matrix a, b, c;
	cin >> a;
	cin >> b;
	cout << endl << "Matrix a: " << endl << a << endl;
	cout << endl << "Matrix b: " << endl << b << endl;

	c = a + b;
	cout << endl << "Matrix c: " << endl << c << endl;

	return 0;
}