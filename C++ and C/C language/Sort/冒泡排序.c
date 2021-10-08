#include "Arrayio.h"
#define N 500000     /*NΪ��������С����data1.txt��ֻ��50����������������趨Nֵʱ����N<=500000*/

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
   int a[N+1],n;                     /*���ݴ洢��a[1]...a[N]��*/
   printf("���ݳ�ʼ��...\n");
   n=readData(a,N,"data1.txt");      
/*��data1.txt�ж���N��������������a��nΪʵ�ʶ�������ݸ���*/
    printf("%d������������...\n",n);
    bubbleSort(a,n);
    output(a,n);
    saveData(a,n,"out.txt");          /*�����������out.txt�ļ���*/
    printf("���������������������out.txt�ļ��С�\n");
    return 0;
}
