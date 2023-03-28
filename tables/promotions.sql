



create table if not exists promotions(
	id int(32) not null auto_increment,
	type varchar(900) not null default "unknow" comment "类型",
	detail varchar(900) not null default "unknow" comment "费用类型",
	money decimal(9,2) not null default 0.00 comment "费用",
	time date not null default "0000-00-00" comment "时间",
	title varchar(900) not null default "unknow" comment "品牌",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_detail`  (`detail`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = '推广费用';   