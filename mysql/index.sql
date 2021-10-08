/*
-- =========== �������� ============
-- ������
create table app_user (
	id bigint(20) unsigned not null auto_increment,
	name varchar(50) default '' comment '�û��ǳ�',
	email varchar(50) not null comment '�û�����',
	phone varchar(20) default '' comment '�ֻ���',
	gender tinyint(4) unsigned default 0 comment '�Ա� (0: �У�1��Ů)',
	password varchar(100) not null comment '����',
	age tinyint(4) default 0 comment '����',
	create_time datetime default current_timestamp,
	update_time timestamp null default current_timestamp on update current_timestamp,
	primary key(id)
)engine=innodb charset=utf8;
*/
/*
-- ����100��������
-- д����֮ǰ����Ҫд���ı������������������Ϊ //
delimiter //
create 
	function mock_data()			-- ���庯����
	returns int							-- ���巵��ֵ
begin
	declare num int default 1000000;
	declare i int default 0;
	
	while (i < num) do
		-- �������
		insert into app_user (name, email, phone, gender, password, age)
		values
		(
			concat('�û�', i), '32165478@qq.com',
			concat(18, floor(rand()*1000000000)), floor(rand()*2),
			uuid(), floor(rand()*100)
		);
		set i = i + 1;
	end while;
	return i;
end //
delimiter ;
-- ����д��󽫽��������¸�Ϊ�ֺ�;

-- ִ�к���
select mock_data();
-- ɾ������
drop function mock_data();
*/
select * from app_user where name = '�û�9999';					-- ��ͨ�ֶβ�ѯ
select * from app_user where id = 10000;						-- ������ѯ
alter table app_user add index id_app_user_name (name);			-- ��������
select * from app_user where name = '�û�9999';					-- ������ѯ




