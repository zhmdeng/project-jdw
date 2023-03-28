



create table if not exists price_info(
	id int(32) not null auto_increment,
	brand varchar(100) not null default "unknow" comment "品牌",
	product_code varchar(300) not null default "000000" comment "产品ID",
	outer_code varchar(300) not null default "000000" comment "产品ID",
	product_name varchar(900) not null default "unknow" comment "商品名称",
	active_price decimal(9,2) not null default 0.00 comment "活动价",
	retail_price decimal(9,2) not null default 0.00 comment "零售价",
	S_price decimal(9,2) not null default 0.00 comment "S级大促价",
	dealership_price decimal(9,2) not null default 0.00 comment "经销供价($)",
	distributorship_price decimal(9,2) not null default 0.00 comment "分销供价($)",
	prime_cost decimal(9,2) not null default 0.00 comment "成本价",
	load_date timestamp not null default current_timestamp() comment "录入时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_product_code`  (`product_id`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = '价格信息'; 

ALTER TABLE wms.price_info ADD COLUMN fixed_code VARCHAR(100) DEFAULT '000000' COMMENT '整理outer_code' AFTER outer_code; 



-- ALTER TABLE wms.price_info
-- ADD bar_code varchar(300) not null default "000000" comment "商品条码" 