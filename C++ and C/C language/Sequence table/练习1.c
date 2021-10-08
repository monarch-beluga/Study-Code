#include <stdio.h>
#define MaxSize 100 

typedef struct{             
	int data[MaxSize];
	int length;
}SqList;

// ˳���ת
void reverse(SqList *L)
{
	int i, temp;
	for (i = 0; i < L->length/2; ++i)
	{
		temp = L->data[i];
		L->data[i] = L->data[L->length-i-1];
		L->data[L->length-i-1] = temp;
	}
}

// 2.5˳������
void add(SqList *L, int p)
{
	int i = L->length;
	for (; p < L->data[i-1]; i--)
		L->data[i] = L->data[i-1];
	L->data[i] = p;
	L->length++;
}

SqList List;

int main()
{
	int i;
	// ˳����ʼ��
	for (i = 0; i < 5; ++i)
	{
		List.data[i] = i*2;
		List.length++;
	}
	// ԭ�����
	printf("ԭ˳���\n");
	for (i = 0; i < List.length; ++i)
		printf("%d ", List.data[i]);
	// ˳���ת
	reverse(&List);
	printf("\n��ת��˳���\n");
	for (i = 0; i < List.length; ++i)
		printf("%d ", List.data[i]);
	reverse(&List);			// ���·�ת
	// ˳������
	add(&List, 6);
	printf("\n��Ӻ�˳���\n");
	for (i = 0; i < List.length; ++i)
		printf("%d ", List.data[i]);
	return 0;
}
