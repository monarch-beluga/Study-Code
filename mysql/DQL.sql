/*
-- �����꼶��
create table grade (
	GradeID int(11) not null auto_increment comment '�꼶���',
	GradeName varchar(50) not null comment '�꼶����',
	primary key (GradeID)
) engine=innodb charset=utf8;

-- ��������
insert into grade (GradeName) values ('��һ'), ('���'), ('����'), ('����'), ('Ԥ�ư�');

-- �����ɼ���
create table result (
	StudentNo int(4) not null comment 'ѧ��',
	SubjectNo int(4) not null comment '�γ̱��',
	ExamDate datetime not null comment '��������',
	StudentResult int(4) not null comment '���Գɼ�',
	key SubjectNo (SubjectNo)
) engine=innodb charset=utf8;

-- ��������
insert into result (StudentNo, SubjectNo, ExamDate, StudentResult) 
values
(1000,1,'2013-11-11 16:00:00',85),
(1000,5,'2013-11-12 16:00:00',70),
(1000,9,'2013-11-11 09:00:00',68),
(1000,13,'2013-11-13 16:00:00',98),
(1000,17,'2013-11-14 16:00:00',58),
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

-- ѧ����
create table student(
	StudentNo int(4) not null comment 'ѧ��',
	LoginPwd varchar(20) default '123456' comment '����',
	StudentName varchar(20) not null comment 'ѧ������',
	Sex enum('M', 'W', 'null') default null comment '�Ա�',
	GradeID int(11) default null comment '�꼶���',
	Phone varchar(50) default null comment '��ϵ�绰',
	Address varchar(255) default null comment '��ַ',
	BornDate DateTime default null comment '����ʱ��',
	Email varchar(50) default null comment '����',
	IdentityCard varchar(18) default null comment '���֤��',
	primary key (StudentNo),
	unique key IdentityCard (IdentityCard),
	key Email (Email)
) engine=innodb charset=utf8;

-- ��������
insert into student (StudentNo, StudentName, Sex, Gradeid, Phone, Address, Email, IdentityCard)
values
(1000, '����', 'M', 2, '13456789536', '��������', 'kies123@qq.com', '123456198001011234'),
(1001, '����', 'M', 1, '13455589896', '�㶫����', 'kies124@qq.com', '123456198001011247'),
(1002, '����', 'W', 2, '13457889536', '�㶫����', 'kies125@qq.com', '123456198001011263'),
(1003, 'С��', 'W', 3, '15456789536', '��������', 'kies126@qq.com', '123456198001022234'),
(1004, 'С��', 'W', 5, '19656789536', '���Ͽ���', 'kies173@qq.com', '123456198001033234'),
(1005, '����', 'M', 4, '18756789536', '��������', 'kies153@qq.com', '123456198001047234'),
(1006, 'С΢', 'W', 5, '13656789536', '�㶫����', 'kues123@qq.com', '123456198001014234'),
(1007, '��ΰ', 'M', 4, '12556789536', '�Ĵ��ɶ�', 'kess123@qq.com', '123456198001078234');


-- �����γ̱�
create table subject (
	SubjectNo int(11) not null auto_increment comment '�γ̱��',
	SubjectName varchar(50) default null comment '�γ�����',
	ClassHour int(4) default null comment 'ѧʱ',
	GradeID int(4) default null comment '�꼶���',
	primary key(SubjectNo)
) engine=innodb charset=utf8;

-- ���ݲ���
insert into subject (SubjectNo,SubjectName,ClassHour,GradeID)
values
(1,'�ߵ���ѧ-1',110,1),
(2,'�ߵ���ѧ-2',110,2),
(3,'�ߵ���ѧ-3',100,3),
(4,'�ߵ���ѧ-4',130,4),
(5,'C����-1',110,1),
(6,'C����-2',110,2),
(7,'C����-3',100,3),
(8,'C����-4',130,4),
(9,'Java�������-1',110,1),
(10,'Java�������-2',110,2),
(11,'Java�������-3',100,3),
(12,'Java�������-4',130,4),
(13,'���ݿ�ṹ-1',110,1),
(14,'���ݿ�ṹ-2',110,2),
(15,'���ݿ�ṹ-3',100,3),
(16,'���ݿ�ṹ-4',130,4),
(17,'C#����',130,1);
*/
/*
-- --------- ָ���򵥲�ѯ -----------
-- ��ѯ���ű�
select * from student;
select * from result;

-- ��ѯһ�ű���ָ�����ֶ�
select StudentNo, StudentName from student;

-- �����һ������,���Ը��ֶ�ȡ������Ҳ���Ը���ȡ����
select StudentNo as ѧ��, StudentName as ѧ������ from student;

-- ���� concat(a, b)
select StudentNo as ѧ��, concat('����', StudentName) as ������ from student;

-- ��ѯһ������Щͬѧ�μ��˿���: destinct ȥ��
select distinct StudentNo from result;

-- ѧԱ���Գɼ�+1��
select StudentNo, StudentResult+1 as ��ֺ� from result;

-- sql ��䲻���ִ�Сд
*/
/*
-- ------- where �����Ӿ� ----------
-- --- �߼������
-- ��ѯѧ���ɼ���[95,100]֮���ѧ��
select studentno, studentresult from result where studentresult<=100 and studentresult>=95;

-- ��ѯ����1000��ѧ��֮���ͬѧ�ĳɼ�
select studentno, studentresult from result where studentno != 1000; -- 1
select studentno, studentresult from result where not studentno = 1000;   -- 2

-- --- ģ����ѯ
-- ��ѯ�ڱ�����ͬѧ��like  %ƥ�����ַ���_ƥ��һ���ַ�
select studentno, studentname, address from student where address like '%����%';

-- ��ѯ����Ϊ���������ġ������ѧԱ: in   
select studentno, studentname from student where studentname in ('����', '����', '����');
*/
/*
-- ---------- �����ѯ join ----------
-- --- ��ѯ�μ��˿��Ե�ͬѧ(ѧ�ţ���������Ŀ��ţ�����)
-- inner join
select s.studentNo, studentname, subjectno, studentresult			-- ��ѯ�ֶ�
from student as s				-- ���ñ���
inner join result as r			-- ���ӷ���
where s.studentno = r.studentno;		-- ȷ������㲢�ж�

-- right join
select s.studentNo, studentname, subjectno, studentresult
from student as s
inner join result as r
on s.studentno = r.studentno;

-- left join
select s.studentNo, studentname, subjectno, studentresult
from student as s
left join result as r
on s.studentno = r.studentno;

-- --- ��ѯ�μ��˿��Ե�ѧ����ѧ�ţ���������Ŀ�������� (��������)
select s.studentno, studentname, subjectname, studentresult
from student as s
inner join result as r
on s.studentno = r.studentno
inner join subject as sub
on sub.subjectno = r.subjectno;
*/

/*
-- --------- ������ -----------
-- --- ��������
create table category (
	categoryid int(10) unsigned not null auto_increment comment '����id',
	pid int(10) not null comment '��id',
	categoryname varchar(50) not null comment '��������',
	primary key (categoryid)
)engine = innodb auto_increment=2 charset=utf8;

insert into category (pid, categoryname)
values
(1, '��Ϣ����'),
(1, '�������'),
(3, '���ݿ�'),
(1, '�������'),
(3, 'web����'),
(5, 'ps����'),
(2, '�칫��Ϣ');
*/
/*
select l.categoryname as '����', r.categoryname as '����'
from category as l
inner join category as r			-- �Լ����Լ�����
on l.categoryid = r.pid;
-- +----------+----------+
-- | ����     | ����     |
-- +----------+----------+
-- | ������� | ���ݿ�   |
-- | ������� | web����  |
-- | ������� | ps����   |
-- | ��Ϣ���� | �칫��Ϣ |
-- +----------+----------+
*/
/*
-- --- ��ϰ������ѧ��ѧ�ţ��������꼶��
select studentno, studentname, gradename
from student as s
inner join grade as g
on g.gradeid = s.gradeid;
*/
/*
-- =========== ��ҳ limit �� ���� order by =============
-- --- �������� asc , ����, desc
select s.studentno, studentname, subjectname, studentresult
from student as s
inner join result as r
on s.studentno = r.studentno
inner join subject as sub
on sub.subjectno = r.subjectno
where subjectname = 'C#����'
order by studentresult desc;			-- ����
*/
/*
-- --- �༶��������ѧ����������ѧ����������
select s.studentno, studentname, subjectname, studentresult
from student as s
inner join result as r
on s.studentno = r.studentno
inner join subject as sub
on sub.subjectno = r.subjectno
order by studentno asc, subjectname asc;		-- ���������ֶ��ö��ŷָ�
*/
/*
-- --- ��ҳ��������ÿ��ѧԱΪһҳ����һҳ5������
-- �鿴����
select s.studentno, studentname, subjectname, studentresult
from student as s
inner join result as r
on s.studentno = r.studentno
inner join subject as sub
on sub.subjectno = r.subjectno
order by studentno asc, subjectname asc;
-- �鿴��һ��
select s.studentno, studentname, subjectname, studentresult
from student as s
inner join result as r
on s.studentno = r.studentno
inner join subject as sub
on sub.subjectno = r.subjectno
order by studentno asc
limit 0,5;						-- ��ʾ��һҳ
-- �鿴�ڶ���
select s.studentno, studentname, subjectname, studentresult
from student as s
inner join result as r
on s.studentno = r.studentno
inner join subject as sub
on sub.subjectno = r.subjectno
order by studentno asc
limit 5,5;						-- ��ʾ�ڶ�ҳ
*/
/*
-- ========= �Ӳ�ѯ ==========
-- --- ��ѯ'C#����'������С��80�ֵ�ѧ����ѧ�ź�����
-- 1.ʹ������
select distinct s.studentno, studentname
from student as s
inner join result as r
on s.studentno = r.studentno
inner join subject as sub
on sub.subjectno = r.subjectno
where subjectname = 'C#����' and studentresult > 80;
-- 2.ʹ���Ӳ�ѯ
select distinct studentno, studentname 
from student 
where studentno in (
	select studentno 
	from result 
	where studentresult > 80 and subjectno = (
		select subjectno 
		from subject
		where subjectname = 'C#����'
	)
);
*/
/*
-- ========== ���ú��� ==========
-- ��ѧ����
select abs(-8);    -- ����ֵ  8
select ceiling(9.4);    -- ����ȡ��  10
select floor(9.4);    -- ����ȡ��   9
select rand();			-- ����һ�� 0 ~ 1֮��������
select sign(10);		-- �ж�һ�����ķ���   0����0  ��������-1 ��������1

-- �ַ�������
select char_length('��̤ʵ�أ����ܱ�������');   -- �����ַ�������
select concat('I ', 'love ', 'you!');			-- ƴ��	
select insert('111111', 2, 0, '222');			-- 122211111
select insert('111111', 2, 4, '222');			-- 12221
-- select insert(�ַ���, ����λ��, Ҫ�滻���ַ���, �ַ���)
select lower('Monarch');			-- תСд
select upper('monarch');			-- ת��д
select instr('monarch', 'c');		-- ���ص�һ��ƥ�������   6
select replace('2211241241', '4', '0');			-- �滻      2211201201
select substr('monarch', 2, 4);		-- ����ָ�����ַ���  (Դ�ַ���, ��ȡλ��, ��ȡ����) onar
select reverse('123456');			-- ��ת�ַ���   654321

-- ʱ������ں���
select current_date();  		-- ��ȡ��ǰ����   YYYY-mm-dd
select curdate();				-- ͬ��
select now();					-- ��ȡ��ǰ������ʱ��   YYYY-MM-DD hh:mm:ss
select localtime();				-- ͬ��
select curtime();				-- ��ȡ��ǰʱ��		hh:mm:ss
*/
/*
-- =========== �ۺϺ��� =============
-- ���ܹ�ͳ�Ʊ��е����ݣ����ѯһ�������ж��ٸ���¼�������
select count(studentname) from student;			-- ָ���ֶΣ������nullֵ
select count(*) from student;				-- �������null�� ���ʼ�������
select count(1) from result;				-- �������null

select sum(studentresult) as �ܺ�,
avg(studentresult) as ƽ����,
max(studentresult) as ��߷�,
min(studentresult) as ��ͷ�
from result;

-- ��ѯ���ÿ�Ŀ��ƽ���֣���߷֣���ͷ�
-- ���ģ����ݲ��õĿγ̷���
select subjectname as �γ�����,
avg(studentresult) as ƽ����,
max(studentresult) as ��߷�,
min(studentresult) as ��ͷ�
from result as r
inner join subject as sub
on r.subjectno = sub.subjectno
group by subjectname  		-- ͨ��ʲô������
having ƽ���� > 80;			-- ����
*/

/*
-- ============ ���� MD5 ���� ============
create table if not exists testmd5 (
	id int(4) not null,
	name varchar(20) not null,
	pwd varchar(50) not null,
	primary key (id)
) engine = innodb charset = utf8;

-- ��������
insert into testmd5 (id, name, pwd)
values
(1, '����', '123456'),
(2, '����', '123456'),
(3, '����', '123456');

-- ����
-- update testmd5 set pwd = md5(pwd) where id = 1;    -- ����
-- update testmd5 set pwd = md5(pwd);					-- ����ȫ��

-- ʵ�ʲ���ʱ�ڲ�������ʱ����
insert into testmd5 
values
(4, 'С��', md5('1234567'));
-- ��ѯʱҲʹ��md5���в�ѯ
select * from testmd5 where pwd = md5('1234567');
*/

