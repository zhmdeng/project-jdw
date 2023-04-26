



create table if not exists customer_products(
	id int(32) not null auto_increment,
	created date not null default "0000-00-00" comment "日期",
	ranks int(10) not null default 0 comment "排名",
	product_name varchar(300) not null default "unknow" comment "商品名称",
	product_id varchar(100) not null default "000000" comment "商品ID",
	visitor_num int(32) not null default -1 comment "商品访客数",
	pay_num int(32) not null default -1 comment "支付买家数",
	pay_money decimal(11,2) not null default -1.00 comment "支付金额",
	TGI int(32) not null default -1 comment "购买偏好TGI",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_product_id`  (`product_id`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = '商品分布';   

