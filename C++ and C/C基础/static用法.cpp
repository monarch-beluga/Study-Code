#include<stdio.h>
void in()					//û�з���ֵʱ��void
{
	static int x;		//ֻ�����ֵʱ��ֵ�����û����ȷ��ֵ����ֵΪ0
	x++;
	printf("%d\n",x);
}
int main()
{
	void in();
	in();
	in();
	in();
}