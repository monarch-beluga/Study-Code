#pragma once
#include<string>
#include<iostream>
using namespace std;
class user
{
	public:
		long long account;
		string gender;
		string name;
		string password;
};
class student :private user
{
	private:
		long long id;
		float math;
		float English;
		float language;
		float Comprehensive;
		float sum;
		static double Sum;
		static int num;
	public:
		student(long long i, string n, string g)
		{
			id = i;
			account = i;
			name = n;
			gender = g;
			num++;
		}
		void pr()
		{
			cout << id << endl;
			cout << name << endl;
		}
};
double student::Sum = 0;
int student::num = 0;