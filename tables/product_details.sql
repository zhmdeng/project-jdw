


create table if not exists product_details(
	id int(32) not null auto_increment,
	product_name varchar(600) not null default 000000 comment "产品名称",
	outer_code varchar(100) not null default 000000 comment "外部产品ID",
	tsc varchar(30) not null default "unknow" comment "淘宝标准产品编码",
	cid bigint(20) not null default 000000 comment "商品类目ID",
	cat_name varchar(300) not null default "unknow" comment "商品类目名称",
	props varchar(900) not null default "unknow" comment "产品的关键属性列表",
	name varchar(900) not null default "unknow" comment "产品名称",
	binds varchar(900) not null default "unknow" comment "产品非关键属性列表",
	sale_props varchar(900) not null default "unknow" comment "产品的销售属性列表",
	price decimal(9,2) not null default -1.00 comment "产品的市场价",
	`desc` varchar(900) not null default "unknow" comment "产品的描述",
	pic_url varchar(900) not null default "unknow" comment "产品的主图片地址",
	created datetime not null default "0000-00-00" comment "创建时间",
	modified datetime not null default "0000-00-00" comment "修改时间",
	status int not null default 66 comment "当前状态(0商家确认,1屏蔽,2未确认,3小二确认,-1删除)",
	vertical_market int not null default 66 comment "垂直市场",
	property_alias varchar(900) not null default "unknow" comment "销售属性值的别名",
	customer_props varchar(900) not null default "unknow" comment "用户自定义属性",
	sell_pt varchar(900) not null default "unknow" comment "产品卖点描述",
	imgs_id int not null default 000000 comment "产品图片ID",
	url varchar(900) not null default "unknow" comment "图片地址",
	position int not null default 000000 comment "图片序号",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_product_id`  (`product_id`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = '产品详情';