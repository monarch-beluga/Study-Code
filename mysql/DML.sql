/*
-- ����
insert into `grade` (`gradename`) values ('С��');
-- insert into <����> (<�ֶ�1>, <�ֶ�2>....) values (<ֵ1>, <ֵ2>....)
select * from `grade`;			-- �鿴���ȫ������
+---------+-----------+
| gradeid | gradename |
+---------+-----------+
|       1 | С��      |
|       2 | С��      |
+---------+-----------+
-- student ��ṹ
 +----------+--------------------------+------+-----+---------+----------------+
| Field    | Type                     | Null | Key | Default | Extra          |
+----------+--------------------------+------+-----+---------+----------------+
| id       | int                      | NO   | PRI | NULL    | auto_increment |
| name     | varchar(30)              | NO   |     | ����    |                |
| pwd      | varchar(20)              | NO   |     | 123456  |                |
| sex      | enum('��','Ů','δ����') | NO   |     | δ����  |                |
| birthday | datetime                 | YES  |     | NULL    |                |
| address  | varchar(100)             | YES  |     | NULL    |                |
| email    | varchar(30)              | YES  |     | NULL    |                |
+----------+--------------------------+------+-----+---------+----------------+
-- �����������
-- insert into student (name, sex) values ('����', '��') ,('����', '��'),('С��', 'Ů');
--  insert into <����> (<�ֶ�>....) values (<ֵ>....),(<ֵ>....).... 
+----+------+--------+-----+----------+---------+-------+
| id | name | pwd    | sex | birthday | address | email |
+----+------+--------+-----+----------+---------+-------+
|  1 | ���� | 123456 | ��  | NULL     | NULL    | NULL  |
|  2 | ���� | 123456 | ��  | NULL     | NULL    | NULL  |
|  3 | С�� | 123456 | Ů  | NULL     | NULL    | NULL  |
+----+------+--------+-----+----------+---------+-------+

-- �޸�
-- update student set sex='Ů' where name='����';
-- update <����> set <Ҫ���ĵ�����> = <ֵ> where ��������;
-- update student set pwd='aaaaaa';
-- �����ָ����������Ὣ����ִ�е�ÿһ������(����ڹ���ʱ������������Ͻ���·����������)
update student set name='�׾�', email='32165@qq.com' where id=1;
+----+------+--------+-----+----------+---------+--------------+
| id | name | pwd    | sex | birthday | address | email        |
+----+------+--------+-----+----------+---------+--------------+
|  1 | �׾� | aaaaaa | ��  | NULL     | NULL    | 32165@qq.com |
|  2 | ���� | aaaaaa | Ů  | NULL     | NULL    | NULL         |
|  3 | С�� | aaaaaa | Ů  | NULL     | NULL    | NULL         |
+----+------+--------+-----+----------+---------+--------------+


-- ɾ��
-- delete����
delete from student where id=3;
-- ɾ��ָ������������
delete from student;
-- ɾ��������������(����ʹ��)
select * from student;

-- truncate����
select * from grade;
-- ��ȫ������ݿ��
truncate grade;
select * from grade;
*/

