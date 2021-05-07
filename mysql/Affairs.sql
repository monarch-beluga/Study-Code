-- ============= 事务 ===========
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

-- --- 模拟转账: 事务
set autocommit = 0;			-- 关闭自动提交
start transaction;			-- 开启一个事务
-- 下面两条为一组事务
update account set money=money - 500 where name = 'A';			-- A减500
update account set money=money + 500 where name = 'B';			-- B减500
-- 成功提交，失败回滚
commit;			-- 提交事务  (提交后不能回滚)
rollback;		-- 回滚

set autocommit = 1;			-- 恢复自动提交







