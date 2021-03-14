# include<iostream>
using namespace std;

struct Lnode
{
	double data;
	Lnode* next;
};

void ShowList(const Lnode* const head)
{
	for (Lnode* p = (Lnode*)head; p; p = p->next)
		cout << p->data << "\t";
	cout << endl;
}
void DeleteList(Lnode* head)
{
	for (Lnode* p = head; p;)
	{
		Lnode* t = p;
		p = p->next;
		delete t;
	}
}
void Insert(Lnode*& head, Lnode* p)
{
	if (!head)
	{
		head = p;
		p->next = NULL;
		return;
	}
	if (head->data > p->data)
	{
		p->next = head;
		head = p;
		return;
	}
	Lnode* sp;
	for (sp = head; sp->next && (sp->next->data < p->data); sp = sp->next);
	p->next = sp->next;
	sp->next = p;
}
Lnode* Merge(Lnode* h1, Lnode* h2)
{
	Lnode* newHead = h1;
	for (Lnode* p = h2; p;)
	{
		Lnode* t = p;
		p = p->next;
		Insert(newHead, t);
	}
	return newHead;
}
void AddToEnd(Lnode* pnew, Lnode*& head)
{
	if (!head)
		head = pnew;
	else
	{
		Lnode* p;
		for (p = head; p->next; p = p->next);
		p->next = pnew;
	}
	pnew->next = NULL;
}
Lnode* GetNode()
{
	Lnode* item = new Lnode;
	if (item)
	{
		item->next = NULL;
		item->data = 0.0;
	}
	else
		cout << "Nothing allocated\n";
	return item;
}

int main()
{
	Lnode* head1 = NULL;
	Lnode* temp;
	double d;
	cout << "data?";
	cin >> d;
	while (d > 0 && (temp = GetNode()))
	{
		temp->data = d;
		AddToEnd(temp, head1);
		cout << "data?";
		cin >> d;
	}
	ShowList(head1);

	Lnode* head2 = NULL;
	cout << "data?";
	cin >> d;
	while (d > 0 && (temp = GetNode()))
	{
		temp->data = d;
		AddToEnd(temp, head2);
		cout << "data?";
		cin >> d;
	}
	ShowList(head2);

	Lnode* head = Merge(head1, head2);

	ShowList(head);
	DeleteList(head);
}
