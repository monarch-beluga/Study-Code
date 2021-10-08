-- ============= ���� ===========
/*
create database shop character set utf8 collate utf8_general_ci;
use shop;

create table account (
	id int(3) not null auto_increment,
	name varchar(30) not null,
	money decimal(9, 2) not null,
	primary key (id)
)engine = innodb charset=utf8;

insert into account (name, money)
values
('A', 2000.00), ('B', 10000.00)
*/

-- --- ģ��ת��: ����
set autocommit = 0;			-- �ر��Զ��ύ
start transaction;			-- ����һ������
-- ��������Ϊһ������
update account set money=money - 500 where name = 'A';			-- A��500
update account set money=money + 500 where name = 'B';			-- B��500
-- �ɹ��ύ��ʧ�ܻع�
commit;			-- �ύ����  (�ύ���ܻع�)
rollback;		-- �ع�

set autocommit = 1;			-- �ָ��Զ��ύ







