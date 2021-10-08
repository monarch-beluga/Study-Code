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
	printf("请输入学生个数：");
	scanf("%d",&n);
	p = (A *)malloc(sizeof(A)*n);
  //p = (A *)calloc(sizeof(A),n);
	for(int i = 0;i<n;i++)
		scanf("%d%f",&p[i].i,&p[i].f);
	printf("学号		分数\n");
	for(int i = 0;i<n;i++)
		printf("%d		%.2f\n",p[i].i,p[i].f);
	free(p);
	return 0;
}
/*
malloc函数是包含在stdlib库里面的函数，作用是动态分配储存空间，实现一个大小自定义的数组;
使用方法：变量 =（变量类型 *）malloc（size），注意等号两边变量类型一致;size即尺寸
多次调用malloc函数分配的空间不会重合
同样的函数还有calloc，它的使用方法是：变量 = (变量类型 *)calloc（n,size）；
两者的区别在于calloc会初始化存储空间；
最后还有free,它的作用是释放存储空间。*/