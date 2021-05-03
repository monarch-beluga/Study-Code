/*
-- 插入
insert into `grade` (`gradename`) values ('小红');
-- insert into <表名> (<字段1>, <字段2>....) values (<值1>, <值2>....)
select * from `grade`;			-- 查看表的全部数据
+---------+-----------+
| gradeid | gradename |
+---------+-----------+
|       1 | 小明      |
|       2 | 小红      |
+---------+-----------+
-- student 表结构
 +----------+--------------------------+------+-----+---------+----------------+
| Field    | Type                     | Null | Key | Default | Extra          |
+----------+--------------------------+------+-----+---------+----------------+
| id       | int                      | NO   | PRI | NULL    | auto_increment |
| name     | varchar(30)              | NO   |     | 匿名    |                |
| pwd      | varchar(20)              | NO   |     | 123456  |                |
| sex      | enum('男','女','未定义') | NO   |     | 未定义  |                |
| birthday | datetime                 | YES  |     | NULL    |                |
| address  | varchar(100)             | YES  |     | NULL    |                |
| email    | varchar(30)              | YES  |     | NULL    |                |
+----------+--------------------------+------+-----+---------+----------------+
-- 插入多条数据
-- insert into student (name, sex) values ('张三', '男') ,('李四', '男'),('小丽', '女');
--  insert into <表名> (<字段>....) values (<值>....),(<值>....).... 
+----+------+--------+-----+----------+---------+-------+
| id | name | pwd    | sex | birthday | address | email |
+----+------+--------+-----+----------+---------+-------+
|  1 | 张三 | 123456 | 男  | NULL     | NULL    | NULL  |
|  2 | 李四 | 123456 | 男  | NULL     | NULL    | NULL  |
|  3 | 小丽 | 123456 | 女  | NULL     | NULL    | NULL  |
+----+------+--------+-----+----------+---------+-------+

-- 修改
-- update student set sex='女' where name='李四';
-- update <表名> set <要更改的属性> = <值> where 查找条件;
-- update student set pwd='aaaaaa';
-- 如果不指定条件，则会将更改执行到每一条数据(如果在工作时不慎操作，请赶紧跑路！！！嘻嘻)
update student set name='白鲸', email='32165@qq.com' where id=1;
+----+------+--------+-----+----------+---------+--------------+
| id | name | pwd    | sex | birthday | address | email        |
+----+------+--------+-----+----------+---------+--------------+
|  1 | 白鲸 | aaaaaa | 男  | NULL     | NULL    | 32165@qq.com |
|  2 | 李四 | aaaaaa | 女  | NULL     | NULL    | NULL         |
|  3 | 小红 | aaaaaa | 女  | NULL     | NULL    | NULL         |
+----+------+--------+-----+----------+---------+--------------+


-- 删除
-- delete命令
delete from student where id=3;
-- 删除指定条件的数据
delete from student;
-- 删除表中所有数据(谨慎使用)
select * from student;

-- truncate命令
select * from grade;
-- 完全清空数据库表
truncate grade;
select * from grade;
*/

