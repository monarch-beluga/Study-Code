/*
-- 创建年级表
create table grade (
	GradeID int(11) not null auto_increment comment '年级编号',
	GradeName varchar(50) not null comment '年级名称',
	primary key (GradeID)
) engine=innodb charset=utf8;

-- 插入数据
insert into grade (GradeName) values ('大一'), ('大二'), ('大三'), ('大四'), ('预科班');

-- 创建成绩表
create table result (
	StudentNo int(4) not null comment '学号',
	SubjectNo int(4) not null comment '课程编号',
	ExamDate datetime not null comment '考试日期',
	StudentResult int(4) not null comment '考试成绩',
	key SubjectNo (SubjectNo)
) engine=innodb charset=utf8;

-- 插入数据
insert into result (StudentNo, SubjectNo, ExamDate, StudentResult) 
values
(1000,1,'2013-11-11 16:00:00',85),
(1000,5,'2013-11-12 16:00:00',70),
(1000,9,'2013-11-11 09:00:00',68),
(1000,13,'2013-11-13 16:00:00',98),
(1000,57,'2013-11-14 16:00:00',58),
(1001,1,'2013-11-11 16:00:00',83),
(1001,5,'2013-11-12 16:00:00',78),
(1001,9,'2013-11-11 09:00:00',80),
(1001,13,'2013-11-13 16:00:00',95),
(1001,17,'2013-11-14 16:00:00',78),
(1002,2,'2013-11-11 16:00:00',85),
(1002,6,'2013-11-12 16:00:00',78),
(1002,10,'2013-11-11 09:00:00',58),
(1002,14,'2013-11-13 16:00:00',88),
(1002,17,'2013-11-14 16:00:00',88),
(1003,2,'2013-11-11 16:00:00',82),
(1003,6,'2013-11-12 16:00:00',90),
(1003,10,'2013-11-11 09:00:00',98),
(1003,14,'2013-11-13 16:00:00',94),
(1003,17,'2013-11-14 16:00:00',78),
(1004,3,'2013-11-11 16:00:00',86),
(1004,7,'2013-11-12 16:00:00',74),
(1004,11,'2013-11-11 09:00:00',85),
(1004,15,'2013-11-13 16:00:00',95),
(1004,17,'2013-11-14 16:00:00',65),
(1005,3,'2013-11-11 16:00:00',90),
(1005,7,'2013-11-12 16:00:00',80),
(1005,11,'2013-11-11 09:00:00',86),
(1005,15,'2013-11-13 16:00:00',96),
(1005,17,'2013-11-14 16:00:00',78),
(1006,4,'2013-11-11 16:00:00',55),
(1006,8,'2013-11-12 16:00:00',50),
(1006,12,'2013-11-11 09:00:00',58),
(1006,16,'2013-11-13 16:00:00',78),
(1006,17,'2013-11-14 16:00:00',58),
(1007,4,'2013-11-11 16:00:00',99),
(1007,8,'2013-11-12 16:00:00',99),
(1007,12,'2013-11-11 09:00:00',98),
(1007,16,'2013-11-13 16:00:00',98),
(1007,17,'2013-11-14 16:00:00',98);

-- 学生表
create table student(
	StudentNo int(4) not null comment '学号',
	LoginPwd varchar(20) default '123456' comment '密码',
	StudentName varchar(20) not null comment '学生姓名',
	Sex enum('M', 'W', 'null') default null comment '性别',
	GradeID int(11) default null comment '年级编号',
	Phone varchar(50) default null comment '联系电话',
	Address varchar(255) default null comment '地址',
	BornDate DateTime default null comment '出生时间',
	Email varchar(50) default null comment '邮箱',
	IdentityCard varchar(18) default null comment '身份证号',
	primary key (StudentNo),
	unique key IdentityCard (IdentityCard),
	key Email (Email)
) engine=innodb charset=utf8;

-- 插入数据
insert into student (StudentNo, StudentName, Sex, Gradeid, Phone, Address, Email, IdentityCard)
values
(1000, '张三', 'M', 2, '13456789536', '北京朝阳', 'kies123@qq.com', '123456198001011234'),
(1001, '李四', 'M', 1, '13455589896', '广东深圳', 'kies124@qq.com', '123456198001011247'),
(1002, '丽丽', 'W', 2, '13457889536', '广东广州', 'kies125@qq.com', '123456198001011263'),
(1003, '小兰', 'W', 3, '15456789536', '北京朝阳', 'kies126@qq.com', '123456198001022234'),
(1004, '小红', 'W', 5, '19656789536', '河南开封', 'kies173@qq.com', '123456198001033234'),
(1005, '王五', 'M', 4, '18756789536', '陕西西安', 'kies153@qq.com', '123456198001047234'),
(1006, '小微', 'W', 5, '13656789536', '广东深圳', 'kues123@qq.com', '123456198001014234'),
(1007, '阿伟', 'M', 4, '12556789536', '四川成都', 'kess123@qq.com', '123456198001078234');


-- 创建课程表
create table subject (
	SubjectNo int(11) not null auto_increment comment '课程编号',
	SubjectName varchar(50) default null comment '课程名称',
	ClassHour int(4) default null comment '学时',
	GradeID int(4) default null comment '年级编号',
	primary key(SubjectNo)
) engine=innodb charset=utf8;

-- 数据插入
insert into subject (SubjectNo,SubjectName,ClassHour,GradeID)
values
(1,'高等数学-1',110,1),
(2,'高等数学-2',110,2),
(3,'高等数学-3',100,3),
(4,'高等数学-4',130,4),
(5,'C语言-1',110,1),
(6,'C语言-2',110,2),
(7,'C语言-3',100,3),
(8,'C语言-4',130,4),
(9,'Java程序设计-1',110,1),
(10,'Java程序设计-2',110,2),
(11,'Java程序设计-3',100,3),
(12,'Java程序设计-4',130,4),
(13,'数据库结构-1',110,1),
(14,'数据库结构-2',110,2),
(15,'数据库结构-3',100,3),
(16,'数据库结构-4',130,4),
(17,'C#基础',130,1);
*/

------------ 指定简单查询 -----------
-- 查询整张表
select * from student;
select * from result;

-- 查询一张表中指定的字段
select StudentNo, StudentName from student;

-- 给结果一个别名,可以给字段取别名，也可以给表取别名
select StudentNo as 学号, StudentName as 学生姓名 from student;

-- 函数 concat(a, b)
select StudentNo as 学号, concat('姓名', StudentName) as 新名字 from student;

-- 查询一下有哪些同学参加了考试: destinct 去重
select distinct StudentNo from result;

-- 学员考试成绩+1分
select StudentNo, StudentResult+1 as 提分后 from result;

-- sql 语句不区分大小写

------ where 条件子句 ----------
--- 逻辑运算符
-- 查询学生成绩在[95,100]之间的学生
select studentno, studentresult from result where studentresult<=100 and studentresult>=95;

-- 查询除了1000号学生之外的同学的成绩
select studentno, studentresult from result where studentno != 1000; -- 1
select studentno, studentresult from result where not studentno = 1000;   -- 2

--- 模糊查询
-- 查询在北京的同学：like  %匹配多个字符，_匹配一个字符
select studentno, studentname, address from student where address like '%北京%';

-- 查询姓名为张三、李四、王五的学员: in   
select studentno, studentname from student where studentname in ('张三', '李四', '王五');



