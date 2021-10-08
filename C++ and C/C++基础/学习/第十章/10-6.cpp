#include<iostream>
#include<iomanip>
using namespace std;

struct Student
{
	int code;
	char name[20];
	char sex;
	unsigned age;
};

struct Node
{
	Student* s;
	Node* next;
};

void Insert(Node*& head, Node*& t)
{
	if (!head || t->s->code < head->s->code)
	{
		t->next = head;
		head = t;
		return;
	}
	Node* p = head;
	for (; p->next; p = p->next)
		if (t->s->code < p->next->s->code)
			break;
	t->next = p->next;
	p->next = t;
}

void Display(const Node* head)
{
	cout << left;
	for (const Node* p = head; p; p=p->next)
		cout << setw(10) << p->s->code << setw(12) << p->s->name
		<< setw(8) << (p->s->sex == 'M' ? "male" : "female")
		<< setw(6) << p->s->age << endl;
}

int main()
{
	Student a[10] = {
		{8311001, "Smith", 'M', 18},
		{8512901, "kerry", 'F', 19},
		{9022101, "Levy", 'M', 16},
		{8508020, "Doris", 'F', 20},
		{8881232, "Ella", 'F', 18},
		{9123001, "Carrie", 'M', 22},
		{8100825, "Barbara", 'F', 23},
		{9012120, "Carmen", 'M', 20},
		{8712001, "Brice", 'M', 19},
		{8100923, "Auden", 'M', 20}
	};
	Node* first = NULL;
	for (int i = 0; i < 10; i++)
	{
		Node* pN = new Node;
		pN->s = &a[i];
		Insert(first, pN);
	}
	Display(first);
}
