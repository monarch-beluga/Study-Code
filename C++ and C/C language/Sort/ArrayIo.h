#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 500000

/*从文件中读入数据存入数组a*/
int readData(int a[], int n,char *f )  /*函数返回成功读入的数据个数*/
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

/*存盘函数*/
void saveData(int a[],int n, char *f )
{
    FILE *fp;
    int i;
    fp=fopen(f,"w");
    if (fp==NULL)   printf("文件建立失败！");
    else
    {
        for (i=0;i<n;i++)
            {   if (i%10==0) fprintf(fp,"%c",'\n');
                fprintf(fp,"%8d",a[i]);
            }
        fclose(fp);
    }
}


/*输出长度为n的整型数组*/
void output(int a[],int n)
{  int i;
   printf("\n数组的内容是：\n");
   for (i=0;i<n;i++)
     { if (i%10==0) printf("\n");
	   printf("%7d",a[i]);
     }
  printf("\n");
}

