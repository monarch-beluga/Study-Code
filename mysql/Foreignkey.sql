-- 外键表
/*
create table `grade`(
	`gradeid` int(10) not null auto_increment comment '年级id',
	`gradename` varchar(50) not null comment '年级名称',
	primary key (`gradeid`))
engine=innodb charset=utf8;
*/
-- 创建表的时候添加外键
/*
create table if not exists `student` (
	`id` int(4) not null auto_increment comment '学号',
	`name` varchar(30) not null default '匿名' comment '姓名',
	`pwd` varchar(20) not null default '123456' comment '密码',
	`sex` enum('男','女','未定义') default '未定义' not null comment '性别',
	`gradeid` int(10) not null comment '学生的年级',
	`birthday` datetime default NULL comment '出生日期',
	`address` varchar(100) default null comment '家庭住址',
	`email` varchar(30) default null comment '邮箱',
	primary key (`id`),
	key `FK_gradeid` (`gradeid`),
	constraint `FK_gradeid` foreign key (`gradeid`) references `grade` (`gradeid`)
)auto_increment=1
engine=innodb charset=utf8;
*/

-- 在已有的表添加外键

create table if not exists `student` (
	`id` int(4) not null auto_increment comment '学号',
	`name` varchar(30) not null default '匿名' comment '姓名',
	`pwd` varchar(20) not null default '123456' comment '密码',
	`sex` enum('男','女','未定义') default '未定义' not null comment '性别',
	-- `gradeid` int(10) not null comment '学生的年级',
	`birthday` datetime default NULL comment '出生日期',
	`address` varchar(100) default null comment '家庭住址',
	`email` varchar(30) default null comment '邮箱',
	primary key (`id`)
)engine=innodb charset=utf8;
/*
alter table `student`
add constraint `FK_gradeid` foreign key(`gradeid`) references `grade` (`gradeid`);
*/
