#include <stdlib.h>
#include <stdio.h>
typedef struct data
{
	long i;
	float f;
}A;
int main()
{
	int n;
	A *p;
	printf("������ѧ��������");
	scanf("%d",&n);
	p = (A *)malloc(sizeof(A)*n);
  //p = (A *)calloc(sizeof(A),n);
	for(int i = 0;i<n;i++)
		scanf("%d%f",&p[i].i,&p[i].f);
	printf("ѧ��		����\n");
	for(int i = 0;i<n;i++)
		printf("%d		%.2f\n",p[i].i,p[i].f);
	free(p);
	return 0;
}
/*
malloc�����ǰ�����stdlib������ĺ����������Ƕ�̬���䴢��ռ䣬ʵ��һ����С�Զ��������;
ʹ�÷��������� =���������� *��malloc��size����ע��Ⱥ����߱�������һ��;size���ߴ�
��ε���malloc��������Ŀռ䲻���غ�
ͬ���ĺ�������calloc������ʹ�÷����ǣ����� = (�������� *)calloc��n,size����
���ߵ���������calloc���ʼ���洢�ռ䣻
�����free,�����������ͷŴ洢�ռ䡣*/