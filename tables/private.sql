


create table if not exists private_log(
	id int(32) not null auto_increment,
	
	store_name varchar(300) not null default "unknow" comment "发货的仓库编码",	
	outer_code varchar(300) not null default "unknow" comment "商品外部编码",
	type varchar(30) not null default "unknow" comment "库存类型类型",
	`group` varchar(100) not null default "unknow" comment "库存分组",
	bu varchar(50) not null default "unknow" comment "公司名称",
	product_name varchar(600) not null default "unknow" comment "商品名称",
	code varchar(300) not null default "unknow" comment "商品条形码",
	product_id varchar(300) not null default "000000" comment "商品id",
	output_type varchar(50) not null default "unknow" comment "单据类型",
	POC_code varchar(300) not null default "unknow" comment "POC单号",
	LBX_code varchar(300) not null default "unknow" comment "LBX单号",
	num int not null default 0 comment "出入库数量",
	`private` varchar(30) not null default "unknow" comment "is private",
	time datetime not null default "0000-00-00 00:00:00" comment "出入库时间",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_outer_code`  (`outer_code`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = 'private_log';   