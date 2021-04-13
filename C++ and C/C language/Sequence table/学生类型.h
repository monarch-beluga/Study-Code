#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MaxSize 100 
#define TRUE 1
#define FALSE 0
typedef struct{        //定义学生成绩表中数据元素的类型 
	char num[13];      //学号 
	char name[8];      //姓名 
	char classname[15];//专业班级 
	int score;         //成绩 
}ElemType; //学生信息类型 
typedef struct{             
	ElemType elem[MaxSize]; //存储学生信息的数组 
	int length;             //学生数 
}SqList; //顺序表类型的定义 
