/*
-- =========== 测试索引 ============
-- 创建表
create table app_user (
	id bigint(20) unsigned not null auto_increment,
	name varchar(50) default '' comment '用户昵称',
	email varchar(50) not null comment '用户邮箱',
	phone varchar(20) default '' comment '手机号',
	gender tinyint(4) unsigned default 0 comment '性别 (0: 男；1：女)',
	password varchar(100) not null comment '密码',
	age tinyint(4) default 0 comment '年龄',
	create_time datetime default current_timestamp,
	update_time timestamp null default current_timestamp on update current_timestamp,
	primary key(id)
)engine=innodb charset=utf8;
*/
/*
-- 插入100万条数据
-- 写函数之前必须要写，改变结束符，将结束符改为 //
delimiter //
create 
	function mock_data()			-- 定义函数名
	returns int							-- 定义返回值
begin
	declare num int default 1000000;
	declare i int default 0;
	
	while (i < num) do
		-- 插入语句
		insert into app_user (name, email, phone, gender, password, age)
		values
		(
			concat('用户', i), '32165478@qq.com',
			concat(18, floor(rand()*1000000000)), floor(rand()*2),
			uuid(), floor(rand()*100)
		);
		set i = i + 1;
	end while;
	return i;
end //
delimiter ;
-- 函数写完后将结束符重新改为分号;

-- 执行函数
select mock_data();
-- 删除函数
drop function mock_data();
*/
select * from app_user where name = '用户9999';					-- 普通字段查询
select * from app_user where id = 10000;						-- 主键查询
alter table app_user add index id_app_user_name (name);			-- 设置索引
select * from app_user where name = '用户9999';					-- 索引查询




