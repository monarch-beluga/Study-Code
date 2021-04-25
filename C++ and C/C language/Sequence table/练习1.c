#include <stdio.h>
#define MaxSize 100 

typedef struct{             
	int data[MaxSize];
	int length;
}SqList;

// 顺序表反转
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

// 2.5顺序表添加
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
	// 顺序表初始化
	for (i = 0; i < 5; ++i)
	{
		List.data[i] = i*2;
		List.length++;
	}
	// 原表输出
	printf("原顺序表\n");
	for (i = 0; i < List.length; ++i)
		printf("%d ", List.data[i]);
	// 顺序表反转
	reverse(&List);
	printf("\n反转后顺序表\n");
	for (i = 0; i < List.length; ++i)
		printf("%d ", List.data[i]);
	reverse(&List);			// 重新反转
	// 顺序表添加
	add(&List, 6);
	printf("\n添加后顺序表\n");
	for (i = 0; i < List.length; ++i)
		printf("%d ", List.data[i]);
	return 0;
}
