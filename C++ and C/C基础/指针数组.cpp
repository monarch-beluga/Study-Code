#include <stdio.h>
int main()
{
	int i =0;				
	char a[3][6]={"kjdfd","kljd","lkoi"},*p[3];	
	//*������[������]Ϊָ������
	char **c;		//**��������ʾָ��ָ�������ָ��
	for(;i<3;i++) p[i]=a[i];
	for(i = 0;i<3;i++) printf("%s\n",p[i]);
	c = p;			//ֱ�Ӱ�ָ���������������ֵ��ָ��ָ�������ָ��
	for (i=0;i<3;i++) printf("%s\n",*c++);
	return 0; 
}