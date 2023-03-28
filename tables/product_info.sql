


create table if not exists product_info(
	id int(32) not null auto_increment,
	brand varchar(100) not null default "unknow" comment "品牌",
	product_id varchar(100) not null default "000000" comment "货品ID",
	product_code varchar(100) not null default "000000" comment "货品编码",
	outer_code varchar(100) not null default "000000" comment "商家编码",
	
	prime_cost decimal(9,2) not null default 0.00 comment "成本价",
	retail_price decimal(9,2) not null default 0.00 comment "零售价",
	active_price decimal(9,2) not null default 0.00 comment "活动价",
	S_price decimal(9,2) not null default 0.00 comment "S级大促价",
	dealership_price decimal(9,2) not null default 0.00 comment "经销供价",
	distributorship_price decimal(9,2) not null default 0.00 comment "分销供价",
	
	code varchar(100) not null default "000000" comment "货品货品条形码",
	product_name varchar(600) not null default "unknow" comment "货品名称",
	specs varchar(100) not null default "unknow" comment "规格",
	catagry_id varchar(100) not null default "000000" comment "类目ID",
	catagry_name varchar(100) not null default "unknow" comment "类目名称",
	
	load_date timestamp not null default current_timestamp() comment "创建时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_product_id`  (`product_id`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = '产品信息';