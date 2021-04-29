#include <iostream>
using namespace std;

// 定义节点类型
class Note
{
	public:
		Note(int i, Note* p)
		{
			data = i;
			next = p;
		}
		int get_data();
		Note* get_next();
		void set_data(int i);
		void set_next(Note* p);
	private:
		int data;
		Note* next;
};

// 输出链表函数
void PrintList(Note* head);
Note* Reverse(Note* head);

int main()
{
	Note* head = NULL;
	for(int i = 0; i < 6; i++)
		head = new Note(i, head);
	cout << "Original linked list:" << endl;
	PrintList(head);

	Note* new_head = Reverse(head);
	cout << "After the linked list is reversed:" << endl;
	PrintList(new_head);
}

void PrintList(Note* head)
{
	Note* p = head;
	while(p != NULL)
	{
		cout << p->get_data() << "->";
		p = p->get_next();
	}
	cout << "NULL" << endl;
}

Note* Reverse(Note* head)
{
	Note* prev = NULL;			// 存储上一个节点
	Note* curr = head;			// 表示当前节点
	Note* next;					// 存储下一个节点
	while(curr != NULL)
	{
		next = curr->get_next();
		curr->set_next(prev);
		prev = curr;
		curr = next;
	}
	return prev;
}



int Note::get_data()
{
	return data;
}
Note* Note::get_next()
{
	return next;
}
void Note::set_data(int i)
{
	data = i;
}
void Note::set_next(Note* p)
{
	next = p;
}
