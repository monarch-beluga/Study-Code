#include <stdio.h>
int main()
{
	int i;
	int a[5]={0,1,2,3,4},*p;
	p=a;			//���������������һ��Ԫ�صĵ�ַ��ֵ��ָ��
	printf("%x *p=%.1f\n",p,*p);			//%x��ʮ���������ָ���ڵĵ�ַ
	for(i=0;i<4;i++)
		printf("%x *p=%.1f\n",++p,*p);		//++p��ָ��洢�ĵ�ַ������Ԫ��λ�ü�һ
	for(i=0;i<4;i++,p += 2)
		printf("%x *p=%d\n",p,*p);
	return 0; 
}
/*
���ɽ��Ϊ��
4ffe44 *p=0
4ffe48 *p=1
4ffe4c *p=2
4ffe50 *p=3
4ffe54 *p=4
��ַ�ļ��Ϊ4����int�����ݴ洢�ռ�Ϊ4�ֽ�*/