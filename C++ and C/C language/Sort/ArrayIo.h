#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 500000

/*���ļ��ж������ݴ�������a*/
int readData(int a[], int n,char *f )  /*�������سɹ���������ݸ���*/
{
    FILE *fp;
    int i;
    fp=fopen(f,"r");
    if (fp==NULL)   return 0;
    else
    {
        for (i=0;i<n && !feof(fp);i++)
            fscanf(fp,"%d",&a[i]);
        fclose(fp);
        return i;
    }
}

/*���̺���*/
void saveData(int a[],int n, char *f )
{
    FILE *fp;
    int i;
    fp=fopen(f,"w");
    if (fp==NULL)   printf("�ļ�����ʧ�ܣ�");
    else
    {
        for (i=0;i<n;i++)
            {   if (i%10==0) fprintf(fp,"%c",'\n');
                fprintf(fp,"%8d",a[i]);
            }
        fclose(fp);
    }
}


/*�������Ϊn����������*/
void output(int a[],int n)
{  int i;
   printf("\n����������ǣ�\n");
   for (i=0;i<n;i++)
     { if (i%10==0) printf("\n");
	   printf("%7d",a[i]);
     }
  printf("\n");
}

