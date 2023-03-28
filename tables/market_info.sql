



create table if not exists market_info(
	id int(32) not null auto_increment,
	sector varchar(300) not null default 'unknow' comment '行业',
	upper_sector varchar(300) not null default 'unknow' comment '父行业',
	plat varchar(30) not null default 'unknow' comment '平台',
	created date not null default "0000-00-00" comment "日期",
	gross_merchandise_volume decimal(10,2) not null default -1.00 comment '交易额',
	upper_money decimal(10,2) not null default -1.00 comment '父行业交易额',
	pay_ratio decimal(10,2) not null default -1.00 comment '支付占父行业比例',
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_sector`  (`sector`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = '市场';   

-- ALTER TABLE wms.price_info
-- ADD sector varchar(300) not null default "unknow" comment "行业"