#include <stdio.h>
#include<time.h>
#include<stdlib.h>
#define N 16
static int a[N][N],b[N][N];
void Ass()
{
	int i,j;
	for(i=0;i<N;i++)
		for(j=0;j<N;j++)
			b[i][j]=-1;
}
void Ccb(int b[][N])
{
	int i,j;
	printf("  ");
	for(i=1;i<=N;i++)
		printf("%2d",i);
	printf("\n");
	for(i=0;i<N;i++)
	{
		printf("%-2d",i+1);
		for(j=0;j<N;j++)
			printf("%2d",b[i][j]);
		printf("\n");
	}
}
int Lde(int x,int y)		//����ף���a����Ϊ��������
{
	int i,j,n;
	int sst[8][2]={-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};		//���ʵ����Աߵİ˸�������������
	if(a[x][y]==9) return 0;		//������return 9 һ���ֹ��������λ����ͬ�ĵ���
	a[x][y]=9;				//������9��ʾ
	for(n=0;n<8;n++)
	{
		i=x+sst[n][0];		//�����Ա߰˸�����
		j=y+sst[n][1];
		if(i<N&&j<N&&i>=0&&j>=0&&a[i][j]<9)a[i][j]++;		//��ֹԽ��
	}
	return 9;
}
void display(int x,int y)		//����������a����Ϸ����ֵ��b
{
	int i,j,n;
	int sst[8][2]={-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};
	if(a[x][y]==0&&b[x][y]==-1)
	{
		b[x][y]=a[x][y];
		for(n=0;n<8;n++)
		{
			i=x+sst[n][0];
			j=y+sst[n][1];
			if(i<N&&j<N&&i>=0&&j>=0) display(i,j);		//�ݹ�˼��
		}
	}
	else b[x][y]=a[x][y];
}
int mark()			//������ʽ
{
	int type,x,y;
	printf("����������ͣ�0 ������� 1 ��ǵ��� 2 ȡ�����ױ�ǣ�");
	scanf("%d",&type);
	printf("�����С��кţ�1~%d����",N);
	scanf("%d%d",&x,&y);
	if(type==0)
	{
		if(a[x-1][y-1]==9) return 0;
		else display(x-1,y-1);
	}
	else if(type==1) b[x-1][y-1]=9;
	else  b[x-1][y-1]=-1;
	return 1;
}
int end()			//��Ϸ������ʽ
{
	int x,y;
	for(x=0;x<N;x++)
		for(y=0;y<N;y++)
			if(b[x][y]==-1) return 1;			//����ʾ����b����-1��ʱ����
	return 0;
}
int main()
{
	int Number,i,j,n,x,y,err=0;
	srand((unsigned)time( NULL ) );			//��ʼ�������
	Number = rand()%(N)+(N-3);			//���������
	for(n=0;n<Number;n++)				//���ף�������������a
	{
		x = rand()%(N-1);
		y = rand()%(N-1);
		if(Lde(x,y)==0) n--;				//��ֹ������ͬһλ��
	}
	Ass();
	Ccb(b);
	do						//��Ϸ����Ҫ����
	{
		if(!mark())
		{
			puts("��ȵ�����1");
			continue;
		}
		system("cls");
		Ccb(b);
	}while(end());
	for(i=0;i<N;i++)			//�ж�ʤ��
		for(j=0;j<N;j++) 
			if(a[i][j]!=b[i][j]) err++;
	if(err==0)puts("��ʤ���ˣ�");
	else puts("ʧ�ܣ������ˣ�");
	return 0;
}