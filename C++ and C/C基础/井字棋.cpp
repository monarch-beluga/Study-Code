#include<stdio.h>
static char a[9];			//����������
void f()		
{
	for(int i=0;i<9;i++)
		a[i]=' ';
}
void Ccb()			//��ӡ����
{
	printf("%c%c%c\n",a[0],a[1],a[2]);
	puts("-+-+-");
	printf("%c%c%c\n",a[3],a[4],a[5]);
	puts("-+-+-");
	printf("%c%c%c\n",a[6],a[7],a[8]);
}
int win(int i)		//�ж�ʤ��
{
	int x=0;
	char ch;
	if(i%2==1) ch='#';
	else ch='$';
	if(a[0]==ch&&a[1]==ch&&a[2]==ch)x=1;
	if(a[3]==ch&&a[4]==ch&&a[5]==ch)x=1;
	if(a[8]==ch&&a[7]==ch&&a[6]==ch)x=1;
	if(a[0]==ch&&a[3]==ch&&a[6]==ch)x=1;
	if(a[1]==ch&&a[4]==ch&&a[7]==ch)x=1;
	if(a[2]==ch&&a[5]==ch&&a[8]==ch)x=1;
	if(a[0]==ch&&a[4]==ch&&a[8]==ch)x=1;
	if(a[6]==ch&&a[4]==ch&&a[2]==ch)x=1;
	return x;
}
int main()
{
	int n=0,m;
	puts("����������Ϊ��ִ$,������Ϊ��ִ#������б��Ϊͬһ��ʤ��");
	f();
	Ccb();
	do
	{
		do
		{
			printf("������1~9���ӵ�λ�ã�");
			scanf("%d",&m);
		}while(a[m-1]!=' ');
		if(n%2==0)a[m-1]='$';
		else a[m-1]='#';
		Ccb();
		win(n);
		n++;
	}while(n<9&&win(n-1)==0);
	if(win(n-1)==0)puts("ƽ�֣�");
	else if(n%2==1)puts("��ʤ��");
	else puts("��ʤ��");
}