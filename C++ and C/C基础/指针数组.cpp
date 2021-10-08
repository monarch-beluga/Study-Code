#include <stdio.h>
int main()
{
	int i =0;				
	char a[3][6]={"kjdfd","kljd","lkoi"},*p[3];	
	//*数组名[数组宽度]为指针数组
	char **c;		//**数组名表示指向指针数组的指针
	for(;i<3;i++) p[i]=a[i];
	for(i = 0;i<3;i++) printf("%s\n",p[i]);
	c = p;			//直接把指针数组的数组名赋值给指向指针数组的指针
	for (i=0;i<3;i++) printf("%s\n",*c++);
	return 0; 
}