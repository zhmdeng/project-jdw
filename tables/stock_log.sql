


create table if not exists stock_log(
	id int(32) not null auto_increment,
	
	code varchar(300) not null default "unknow" comment "单号",
	LP_code varchar(300) not null default "unknow" comment "LP单号",
	outer_code varchar(300) not null default "unknow" comment "商品外部编码",
	product_name varchar(600) not null default "unknow" comment "商品名称",
	store_name varchar(300) not null default "unknow" comment "发货的仓库名称",
	time datetime not null default "0000-00-00 00:00:00" comment "出入库时间",
	type varchar(30) not null default "unknow" comment "单据类型",
	stock_type varchar(50) not null default "unknow" comment "出入库类型",
	num int not null default 0 comment "出入库数量",
	surplus_num int not null default -10000 comment "出入库数量",
	erp_code varchar(600) not null default "unknow" comment "erp编码",
	tid bigint(30) not null default 000000 comment "交易编号",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_code`  (`code`) using btree,
	key `idx_tid`  (`tid`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = 'stock_log';   