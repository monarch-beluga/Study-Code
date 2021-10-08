-- �����
/*
create table `grade`(
	`gradeid` int(10) not null auto_increment comment '�꼶id',
	`gradename` varchar(50) not null comment '�꼶����',
	primary key (`gradeid`))
engine=innodb charset=utf8;
*/
-- �������ʱ��������
/*
create table if not exists `student` (
	`id` int(4) not null auto_increment comment 'ѧ��',
	`name` varchar(30) not null default '����' comment '����',
	`pwd` varchar(20) not null default '123456' comment '����',
	`sex` enum('��','Ů','δ����') default 'δ����' not null comment '�Ա�',
	`gradeid` int(10) not null comment 'ѧ�����꼶',
	`birthday` datetime default NULL comment '��������',
	`address` varchar(100) default null comment '��ͥסַ',
	`email` varchar(30) default null comment '����',
	primary key (`id`),
	key `FK_gradeid` (`gradeid`),
	constraint `FK_gradeid` foreign key (`gradeid`) references `grade` (`gradeid`)
)auto_increment=1
engine=innodb charset=utf8;
*/

-- �����еı�������

create table if not exists `student` (
	`id` int(4) not null auto_increment comment 'ѧ��',
	`name` varchar(30) not null default '����' comment '����',
	`pwd` varchar(20) not null default '123456' comment '����',
	`sex` enum('��','Ů','δ����') default 'δ����' not null comment '�Ա�',
	-- `gradeid` int(10) not null comment 'ѧ�����꼶',
	`birthday` datetime default NULL comment '��������',
	`address` varchar(100) default null comment '��ͥסַ',
	`email` varchar(30) default null comment '����',
	primary key (`id`)
)engine=innodb charset=utf8;
/*
alter table `student`
add constraint `FK_gradeid` foreign key(`gradeid`) references `grade` (`gradeid`);
*/
