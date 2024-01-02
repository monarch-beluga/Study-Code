#include<iostream>
#include <algorithm>
using namespace std;

typedef struct ListNote{
    int val;
    ListNote* next;
}*Node;

void PrintList(Node head)
{
    Node p = head;
    while(p != NULL)
    {
        cout << p->val << " ";
        p = p->next;
    }
    cout << "\n";
}

void swapNote(Node& head)
{
    Node p1, p2, p3;
    p1 = head;
    int i = 0;
    while(p1 != NULL)
    {
        p2 = p1->next;
        p1->next = p2->next;
        p2->next = p1;
        if (i == 0)
            head = p2;
        else
            p3->next = p2;
        p3 = p1;
        p1 = p1->next;
        ++i;
    }
}


int main()
{ 
    #if ONLINE_JUDGE
    #else
    freopen("input.txt", "r", stdin);
    #endif
    Node head, p1, p2;
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        p1 = new ListNote();
        cin >> p1->val;
        if (i == 0)
            head = p1;
        else
            p2->next = p1;
        p2 = p1;
    }

    PrintList(head);
    swapNote(head);
    PrintList(head);

    return 0;
}




