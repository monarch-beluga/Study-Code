#include <stdio.h>
int main()
{
	int i;
	int a[5]={0,1,2,3,4},*p;
	p=a;			//将数组名即数组第一个元素的地址赋值给指针
	printf("%x *p=%.1f\n",p,*p);			//%x以十六进制输出指针内的地址
	for(i=0;i<4;i++)
		printf("%x *p=%.1f\n",++p,*p);		//++p即指针存储的地址按数组元素位置加一
	for(i=0;i<4;i++,p += 2)
		printf("%x *p=%d\n",p,*p);
	return 0; 
}
/*
生成结果为：
4ffe44 *p=0
4ffe48 *p=1
4ffe4c *p=2
4ffe50 *p=3
4ffe54 *p=4
地址的间隔为4，即int型数据存储空间为4字节*/