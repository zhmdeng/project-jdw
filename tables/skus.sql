


create table if not exists skus(
	id int(32) not null auto_increment,
	skuid bigint(20) not null default 000000 comment "sku的id",
	iid varchar(900) not null default "unknow" comment "sku所属商品id",
	num_iid bigint(20) not null default 000000 comment "sku所属商品数字id",
	properties_name varchar(900) not null default "unknow" comment "sku的销售属性组合字符串",
	quantity int not null default -1 comment "属于这个sku的商品的数量",
	price decimal(9,2) not null default -1.00 comment "属于这个sku的商品的价格",
	outer_id varchar(100) not null default "unknow" comment "商家设置的外部id",
	created datetime not null default "0000-00-00" comment "sku创建的日期",
	modified datetime not null default "0000-00-00" comment "sku最后修改日期",
	status varchar(300) not null default "unknow" comment "sku状态。normal:正常,delete:删除",
	sku_spec_id bigint(20) not null default 000000 comment "表示SKu上的产品规格信息",
	barcode varchar(300) not null default  "unknow" comment "商品级别的条形码",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_skuid`  (`skuid`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = 'sku';   