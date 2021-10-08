#include "Arrayio.h"
#define N 500000     /*N为数据量大小，因data1.txt中只有50万个数，所以自行设定N值时需让N<=500000*/

void bubbleSort(int a[],int n)
{
    int i;
    int flag=1;
    while (n>1 && flag==1)
    {  flag=0;
        for (i=1;i<n;i++)
        {      if (a[i]>a[i+1])
                {       a[0]=a[i];
                        a[i]=a[i+1];
                        a[i+1]=a[0];
                        flag=1;
                }
        }
        n--;
    }
}

int  main()
{
   int a[N+1],n;                     /*数据存储在a[1]...a[N]中*/
   printf("数据初始化...\n");
   n=readData(a,N,"data1.txt");      
/*从data1.txt中读入N个整数存入数组a，n为实际读入的数据个数*/
    printf("%d个数据排序中...\n",n);
    bubbleSort(a,n);
    output(a,n);
    saveData(a,n,"out.txt");          /*排序结果存放在out.txt文件中*/
    printf("排序结束，排序结果保存在out.txt文件中。\n");
    return 0;
}
