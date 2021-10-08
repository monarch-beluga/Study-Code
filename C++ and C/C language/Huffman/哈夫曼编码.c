#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct
{
	char ch; //节点字符 
	int w;   //节点权值 
	int lchild,rchild;	//左右孩子的数组下标 
}HafuNode,*HafuTree;

HafuTree ht; //声明一个指向哈夫曼树节点的指针 
typedef struct
{
	char ch;          //叶子节点字符 
	char codestr[20]; //字符编码 
}HafuCode;

HafuCode code[27]; //用于存放对应字符和哈夫曼编码，注意27个字符的设置 

int num;               //记录节点个数 
int codenum=0;         //已经获得的编码个数 
char filename[20]=""; //存储文件名 

void InitHafuArry(); //导入文件,计算权值，生成只含有叶子节点的HafuNode数组 

void InitHafuArry()
{
	int j,i,k;
	char ch;
	HafuNode tmpht;
    FILE* fp = NULL;
	char location[30]=""; //设置目录路径 
	
	ht=(HafuTree)malloc(53*sizeof(HafuNode)); //53=2*n-1= 2*27-1
	if(ht==NULL)
	   return ;
	for(i=0;i<53;i++) /*初始化数据单元，每个单元自成一棵树*/ 
	{
		ht[i].w=0;  //权值初始化为0 
		ht[i].lchild = ht[i].rchild =-1; //左右子树初始为空，设为-1 
	}
	num=0;//记录节点数 	
	printf("File name:");
	scanf("%s",filename); //待编码的文本文件名称 
	strcat(location,filename);	
	fp=fopen(location,"r");//只读方式打开文件 
	if(!fp)
	{
		printf("Open Error");
		return;
	}
	while(!feof(fp)) //读取待编码文件 
	{
		ch=fgetc(fp); //读取字符 
		if((ch==' ')|| (ch<='z' && ch>='a') || (ch<='Z' && ch>='A'))
		{// 只处理有效字符 
			printf("%c",ch);
			if(ch==' ')
			  ch='#'; //处理空格 		
			for(j=0;j<num;j++)
			{
				if(ht[j].ch==ch)
				{
					break;
				}
			}  
			if(j==num)            //找到新字符  
			{
				ht[num].ch = ch; //将新字符存入并将权值加1 
				ht[num].w++;
				num++;
			}
			else
			{
				ht[j].w++; //将已有字符权值加1 
			}
		}
	}
	//以上代码执行完毕，将读取的字符分别设置相应的权值，字符出现次数多的，权值大。 
	fclose(fp);
	printf("\n");
	
	for(i=0;i<num;i++) //对叶子节点按权值进行升序排序 
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
//数组中生成哈夫曼树，返回根节点下标  
{
	int i,k,j,root;
	HafuNode hfnode;
	codenum =0;
	
	//printf("%d", num); //5个节点，这里num=4 
	for(i=0;i<num-1;i++)  //num是全局变量，保存节点的个数 
	{   
	    //需生成num-1个节点 
		k=2*i+1;                  //每次提取前面2个节点，其权值最小 
		hfnode.w= ht[k].w+ht[k-1].w;
		
		hfnode.lchild = k-1; //左子树的序号 
		hfnode.rchild = k;   //右子树的序号
		
		for(j=num+i;j>k;j--) //将新节点插入到有序数组中,j是产生的新节点的下标 
		{
			if(ht[j].w>hfnode.w)
			{
				ht[j+1]=ht[j];//有节点比新节点大，则交换位置 
			}
			else break;
		}
		ht[j]=hfnode;	
		root=j;	
	}		
	return root; //最后生成根节点的下标 ，这里是下标是6 
}

void GetHafuCode(HafuTree ht, int root, char* codestr)
{
    FILE * out;
	int len,i;
	FILE * fp;
	char ch;
	char location[30]=""; //root=6 

	if(ht[root].lchild==-1) //是叶子节点 
	{
		
		code[codenum].ch = ht[root].ch;
		strcpy(code[codenum].codestr,codestr);
		codenum++;
	}
	else  //不是终点则继续递归 
	{
		len = strlen(codestr);//len的初始长度为0 
		codestr[len]='0';//左分支编码0 
		codestr[len+1]=0;//防止被覆盖，尾部加\0 
		GetHafuCode(ht,ht[root].lchild,codestr);//向左递归 
		
		
		len = strlen(codestr);		
		codestr[len-1]='1';//左分支编码1
		GetHafuCode(ht,ht[root].rchild,codestr);
		
		len=strlen(codestr);
		codestr[len-1]=0;//右孩子 递归完成后，删除编码标记末尾 
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
				   fputs(code[i].codestr,out);	//输出编码					  	
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
   	  	 if(ch=='0') //如果为0，从当前节点向左搜索 
   	  	 {
 	  	    if(ht[curr].lchild != -1)
		    {
 		   	  curr=ht[curr].lchild;//若有左子树，向左走 			
 		    } 	
 		    else
 		    {
 		     	curr=root;//没有，返回根节点 
 		    }
   	 	 }
 		 
		 if(ch=='1') //如果为1，从当前节点向右搜索
 		 {
 		    if(ht[curr].rchild!=-1)
 		    {
	 		   curr= ht[curr].rchild;//若有右子树，向右走
	 	   	}
	 	    else
	 	    {
			   curr=root; //没有，返回根节点 
		    }
	     }
		
	  	 if(ht[curr].lchild==-1 && ht[curr].rchild==-1) //叶子节点 
	 	 { 
	 	    printf("%c",ht[curr].ch=='#'?' ':ht[curr].ch);//空格处理 
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
	printf(" 1: 编                           码\n");
    printf(" 2: 解        码（先编码）         \n");
    printf(" 3: 退                           出\n");
    printf("请选择一个序号：\n ");
    
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
	    	
	    	  GetHafuCode(ht,root,codestr); //编码 
	    	  printf("Code:");	    	  
	    	  output= fopen("code.txt","r"); //保存编码到文件 
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
 	  	    	  	printf("%c",ch); //屏幕上输出编码结果 
 	  	    	 } 	  	    	 
  	    	  }
  	    	  fclose(output);
			  break;
  	    	case 2:
			  DecodeHuffmanCode(ht,root); //解码 
			  break;  
		    case 3:
		      exit(0);  //退出 
            default:
              printf("请选择一个序号：\n");
              break;
	    }
	    printf("\n");
	   	printf("====================Menu=======================\n");
   	    printf(" 1: 编                           码\n");
        printf(" 2: 解        码（先编码）         \n");
        printf(" 3: 退                           出\n");
        printf("请选择一个序号：\n ");
		getch();
		scanf("%d",&control);  	
    }		    
    return 0;
}
