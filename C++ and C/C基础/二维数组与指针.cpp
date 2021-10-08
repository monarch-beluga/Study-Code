#include <stdio.h>
int main()
{
	int a[2][3],i,*p;
	p=&a[0][0];				//注意指针地址赋值与一位数组的不同
	for(i=0;i<6;i++)
			scanf("%d",p++);
	p=&a[0][0];
	for(i=0;i<6;i++,p++)
			printf("%x *p=%d\n",p,*p);
	return 0; 
}