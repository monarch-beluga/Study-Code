#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct
{
	char ch; //�ڵ��ַ� 
	int w;   //�ڵ�Ȩֵ 
	int lchild,rchild;	//���Һ��ӵ������±� 
}HafuNode,*HafuTree;

HafuTree ht; //����һ��ָ����������ڵ��ָ�� 
typedef struct
{
	char ch;          //Ҷ�ӽڵ��ַ� 
	char codestr[20]; //�ַ����� 
}HafuCode;

HafuCode code[27]; //���ڴ�Ŷ�Ӧ�ַ��͹��������룬ע��27���ַ������� 

int num;               //��¼�ڵ���� 
int codenum=0;         //�Ѿ���õı������ 
char filename[20]=""; //�洢�ļ��� 

void InitHafuArry(); //�����ļ�,����Ȩֵ������ֻ����Ҷ�ӽڵ��HafuNode���� 

void InitHafuArry()
{
	int j,i,k;
	char ch;
	HafuNode tmpht;
    FILE* fp = NULL;
	char location[30]=""; //����Ŀ¼·�� 
	
	ht=(HafuTree)malloc(53*sizeof(HafuNode)); //53=2*n-1= 2*27-1
	if(ht==NULL)
	   return ;
	for(i=0;i<53;i++) /*��ʼ�����ݵ�Ԫ��ÿ����Ԫ�Գ�һ����*/ 
	{
		ht[i].w=0;  //Ȩֵ��ʼ��Ϊ0 
		ht[i].lchild = ht[i].rchild =-1; //����������ʼΪ�գ���Ϊ-1 
	}
	num=0;//��¼�ڵ��� 	
	printf("File name:");
	scanf("%s",filename); //��������ı��ļ����� 
	strcat(location,filename);	
	fp=fopen(location,"r");//ֻ����ʽ���ļ� 
	if(!fp)
	{
		printf("Open Error");
		return;
	}
	while(!feof(fp)) //��ȡ�������ļ� 
	{
		ch=fgetc(fp); //��ȡ�ַ� 
		if((ch==' ')|| (ch<='z' && ch>='a') || (ch<='Z' && ch>='A'))
		{// ֻ������Ч�ַ� 
			printf("%c",ch);
			if(ch==' ')
			  ch='#'; //����ո� 		
			for(j=0;j<num;j++)
			{
				if(ht[j].ch==ch)
				{
					break;
				}
			}  
			if(j==num)            //�ҵ����ַ�  
			{
				ht[num].ch = ch; //�����ַ����벢��Ȩֵ��1 
				ht[num].w++;
				num++;
			}
			else
			{
				ht[j].w++; //�������ַ�Ȩֵ��1 
			}
		}
	}
	//���ϴ���ִ����ϣ�����ȡ���ַ��ֱ�������Ӧ��Ȩֵ���ַ����ִ�����ģ�Ȩֵ�� 
	fclose(fp);
	printf("\n");
	
	for(i=0;i<num;i++) //��Ҷ�ӽڵ㰴Ȩֵ������������ 
	{
		k=i;
		for(j=i+1;j<num;j++)
		{
			if(ht[j].w<ht[k].w)
			   k=j;
		}
		if(k!=i)
		{
			tmpht = ht[i];
			ht[i]=ht[k];
			ht[k]=tmpht;			
		}
	}	
}
int CreateHuffman(HafuTree ht)
//���������ɹ������������ظ��ڵ��±�  
{
	int i,k,j,root;
	HafuNode hfnode;
	codenum =0;
	
	//printf("%d", num); //5���ڵ㣬����num=4 
	for(i=0;i<num-1;i++)  //num��ȫ�ֱ���������ڵ�ĸ��� 
	{   
	    //������num-1���ڵ� 
		k=2*i+1;                  //ÿ����ȡǰ��2���ڵ㣬��Ȩֵ��С 
		hfnode.w= ht[k].w+ht[k-1].w;
		
		hfnode.lchild = k-1; //����������� 
		hfnode.rchild = k;   //�����������
		
		for(j=num+i;j>k;j--) //���½ڵ���뵽����������,j�ǲ������½ڵ���±� 
		{
			if(ht[j].w>hfnode.w)
			{
				ht[j+1]=ht[j];//�нڵ���½ڵ���򽻻�λ�� 
			}
			else break;
		}
		ht[j]=hfnode;	
		root=j;	
	}		
	return root; //������ɸ��ڵ���±� ���������±���6 
}

void GetHafuCode(HafuTree ht, int root, char* codestr)
{
    FILE * out;
	int len,i;
	FILE * fp;
	char ch;
	char location[30]=""; //root=6 

	if(ht[root].lchild==-1) //��Ҷ�ӽڵ� 
	{
		
		code[codenum].ch = ht[root].ch;
		strcpy(code[codenum].codestr,codestr);
		codenum++;
	}
	else  //�����յ�������ݹ� 
	{
		len = strlen(codestr);//len�ĳ�ʼ����Ϊ0 
		codestr[len]='0';//���֧����0 
		codestr[len+1]=0;//��ֹ�����ǣ�β����\0 
		GetHafuCode(ht,ht[root].lchild,codestr);//����ݹ� 
		
		
		len = strlen(codestr);		
		codestr[len-1]='1';//���֧����1
		GetHafuCode(ht,ht[root].rchild,codestr);
		
		len=strlen(codestr);
		codestr[len-1]=0;//�Һ��� �ݹ���ɺ�ɾ��������ĩβ 
	}
	strcat(location,filename);
	fp=fopen(location,"r");
	if(!fp)
	{
		printf("Open Error");
		return;
	}
	out = fopen("code.txt","w+"); 
	if(!out)
	{
		return;
	}
	while(!feof(fp))
	{
		ch=fgetc(fp);
		if((ch==' ')|| (ch<='z' && ch>='a') || (ch<='Z' && ch>='A'))
		{
			if(ch==' ') ch='#';		
			for(i=0;i<codenum;i++)
			{
				if(ch==code[i].ch)
				{
				   fputs(code[i].codestr,out);	//�������					  	
				}
			}  			
		}
				
	}
	fclose(fp);
	fclose(out);
}

void DecodeHuffmanCode(HafuTree ht, int root)
{
   FILE* fp2;
   char ch;
   int curr = root;
   char filename2[20]="";
   char location[30]="";
   printf("File name:");
   scanf("%s", filename);
   strcat(location,filename);
   fp2=fopen(location,"r");
   if(!fp2)
   {
   	   printf("Open Error"); 
   }
   printf("Code:");
   while(!feof(fp2))
   {
   	   ch=fgetc(fp2);
   	   if(ch>='0' && ch<='1')
   	   {
   	   	   printf("%c",ch);
   	   }
   }
   printf("\n")	;
   rewind(fp2); //
   
   while(!feof(fp2))
   {
   	  ch=fgetc(fp2);
   	  if(ch>='0'&&ch<='1')
   	  {
   	  	 if(ch=='0') //���Ϊ0���ӵ�ǰ�ڵ��������� 
   	  	 {
 	  	    if(ht[curr].lchild != -1)
		    {
 		   	  curr=ht[curr].lchild;//������������������ 			
 		    } 	
 		    else
 		    {
 		     	curr=root;//û�У����ظ��ڵ� 
 		    }
   	 	 }
 		 
		 if(ch=='1') //���Ϊ1���ӵ�ǰ�ڵ���������
 		 {
 		    if(ht[curr].rchild!=-1)
 		    {
	 		   curr= ht[curr].rchild;//������������������
	 	   	}
	 	    else
	 	    {
			   curr=root; //û�У����ظ��ڵ� 
		    }
	     }
		
	  	 if(ht[curr].lchild==-1 && ht[curr].rchild==-1) //Ҷ�ӽڵ� 
	 	 { 
	 	    printf("%c",ht[curr].ch=='#'?' ':ht[curr].ch);//�ո��� 
	 	    curr=root;
	 	 }
	 	
     } 	   
   }
   fclose(fp2);
}

int main()
{
	int root;
	char codestr[20]="";
	int control;
	
	printf("====================Menu=======================\n");
	printf(" 1: ��                           ��\n");
    printf(" 2: ��        �루�ȱ��룩         \n");
    printf(" 3: ��                           ��\n");
    printf("��ѡ��һ����ţ�\n ");
    
    scanf("%d", &control);
	while(control!=3)
    {
    	FILE* output;
    	char ch;
    	switch(control)
    	{
	    	case 1:
	    	  InitHafuArry();	    	  
	    	  root=CreateHuffman(ht);
	    	
	    	  GetHafuCode(ht,root,codestr); //���� 
	    	  printf("Code:");	    	  
	    	  output= fopen("code.txt","r"); //������뵽�ļ� 
	    	  if(!output)
	    	  {
  	    	     printf("Open Error");
  			     continue;	
  	    	  }
  	    	  while(!feof(output))
  	    	  {
  	    	  	 ch=fgetc(output);
  	    	  	 if(ch>='0'&& ch<='1')
  	    	  	 {
 	  	    	  	printf("%c",ch); //��Ļ����������� 
 	  	    	 } 	  	    	 
  	    	  }
  	    	  fclose(output);
			  break;
  	    	case 2:
			  DecodeHuffmanCode(ht,root); //���� 
			  break;  
		    case 3:
		      exit(0);  //�˳� 
            default:
              printf("��ѡ��һ����ţ�\n");
              break;
	    }
	    printf("\n");
	   	printf("====================Menu=======================\n");
   	    printf(" 1: ��                           ��\n");
        printf(" 2: ��        �루�ȱ��룩         \n");
        printf(" 3: ��                           ��\n");
        printf("��ѡ��һ����ţ�\n ");
		getch();
		scanf("%d",&control);  	
    }		    
    return 0;
}
