



create table if not exists price(
	id int(32) not null auto_increment,
	product_id varchar(300) not null default "000000" comment "产品ID",
	K3_code varchar(300) not null default "000000" comment "K3代码",
	product_name varchar(900) not null default "unknow" comment "商品名称",
	active_price decimal(9,2) not null default 0.00 comment "活动价",
	retail_price decimal(9,2) not null default 0.00 comment "零售价",
	S_price decimal(9,2) not null default 0.00 comment "S级大促价",
	S_profit decimal(9,2) not null default 0.00 comment "经营毛利率S价",
	dealership_price decimal(9,2) not null default 0.00 comment "经销供价",
	distributorship_price decimal(9,2) not null default 0.00 comment "分销供价",
	output_price decimal(9,2) not null default 0.00 comment "出库价",
	prime_cost decimal(9,2) not null default 0.00 comment "成本价",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_product_id`  (`product_id`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = '价格体系';   