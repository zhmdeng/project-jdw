


-- taobao.logistics.orders.detail.get
create table if not exists shippings(
	id int(32) not null auto_increment,
	tid bigint(30) not null default 000000 comment "交易编号",
	order_code varchar(100) not null default "unknow" comment "物流订单编号",
	seller_nick varchar(900) not null default "unknow" comment "卖家昵称",
	buyer_nick varchar(300) not null default "unknow" comment "买家昵称",
	delivery_start datetime not null default "0000-00-00 00:00:00" comment "预约取货开始时间",
	delivery_end datetime not null default "0000-00-00 00:00:00" comment "预约取货结束时间",
	out_sid varchar(100) not null default "unknow" comment "运单号,具体一个物流公司的运单号码",
	item_title varchar(900) not null default "unknow" comment "货物名称",
	receiver_name varchar(100) not null default "unknow" comment "收货人的姓名",
	receiver_mobile bigint(20) not null default 000000 comment "收货人的手机号码",
	receiver_phone bigint(20) not null default 000000 comment "收货人的电话号码",
	zip int(11) not null default 000001 comment "邮政编码",
	address varchar(900) not null default "unknow" comment "详细地址",
	city varchar(100) not null default "unknow" comment "所在城市",
	state varchar(100) not null default "unknow" comment "所在省份",
	country varchar(100) not null default "unknow" comment "国家名称",
	district varchar(100) not null default "unknow" comment "区/县",
	created datetime not null default "0000-00-00 00:00:00" comment "运单创建时间",
	modified datetime not null default "0000-00-00 00:00:00" comment "运单修改时间",
	status varchar(100) not null default "unknow" comment "物流订单状态",
	type char(10) not null default "unknow" comment "物流方式:可选free卖家包邮,post平邮,express快递,ems",
	freight_payer char(10) not null default "unknow" comment "谁承担运费:可选buyer买家,seller卖家",
	company_name varchar(300) not null default "unknow" comment "物流公司名称",
	seller_confirm char(10)not null default "unknow" comment "卖家是否确认发货:yes是,no否",
	is_quick_cod_order char(10) not null default "unknow" comment "标示是否快捷COD订单",
	is_split int(11) not null default 0 comment "表明是否拆单，默认0",
	sub_tids varchar(900) not null default "unknow" comment "拆单子订单列表，对应的数据是:该物流订单下的全部子订单",
	ouid varchar(300) not null default "unknow" comment "ouid",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_order_code` (`order_code`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = '订单物流详情';   