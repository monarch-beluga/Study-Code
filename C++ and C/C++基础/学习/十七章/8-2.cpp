#include<iostream>
using namespace std;
#include<queue>
#include<string>

void test_empty()
{
	priority_queue<int> mypq;
	int sum = 0;

	for (int i = 1; i <= 100; i++)
		mypq.push(i);

	while (!mypq.empty())
	{
		sum += mypq.top();
		mypq.pop();
	}
	cout << "总和是：" << sum << endl;
}

void test_pop()
{
	priority_queue<int> mypq;
	mypq.push(30);
	mypq.push(100);
	mypq.push(25);
	mypq.push(40);
	cout << "元素出队列……" << endl;

	while (!mypq.empty())
	{
		cout << "" << mypq.top();
		mypq.pop();
	}
	cout << endl;
}

void test_top()
{
	priority_queue<string> mypq;
	mypq.push("how");
	mypq.push("are");
	mypq.push("you");

	cout << "队头元素：--" << mypq.top() << endl;
}

int main()
{
	test_empty();
	cout << "\n----------------------------------------\n";
	test_pop();
	cout << "\n----------------------------------------\n";
	test_top();
	cout << "\n----------------------------------------\n";

	priority_queue<double> q;
	q.push(66.6);
	q.push(22.2);
	q.push(44.4);

	cout << q.top() << "\t";

	q.pop();
	q.push(11.1);
	q.push(55.5);
	q.push(33.3);
	q.pop();
	while (!q.empty())
	{
		cout << q.top() << "\t";
		q.pop();
	}
	cout << endl;

	return 0;
}