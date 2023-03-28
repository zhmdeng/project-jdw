


create table if not exists order_skus(
	id int(32) not null auto_increment,
	oid varchar(150) not null default "000000" comment "子订单编号",
    order_id varchar(150) not null default "000000" comment "主订单编号",
    sku_name varchar(900) not null default "000000" comment "sku",
    price decimal(9,2) not null default -1.00 comment "sku价格",
    num int not null default 0 comment "sku购买数量",
    outer_code varchar(100) not null default "000000" comment "外部系统编号",
    product_attribut varchar(300) not null default "unknow" comment "商品属性",
    info varchar(300) not null default "unknow" comment "套餐信息",
    postscript varchar(300) not null default "unknow" comment "备注",
    order_status varchar(100) not null default "unknow" comment "订单状态",
    code varchar(100) not null default "000000" comment "商家编码",
    pay_code varchar(100) not null default "000000" comment "支付单号",
    order_total_fee decimal(9,2) not null default -1.00 comment "应付款",
    order_payment decimal(9,2) not null default -1.00 comment "实付金额",
    refund_status varchar(100) not null default "unknow" comment "退款状态",
    refund_money varchar(50) not null default -1.00 comment "退款金额",
    created datetime not null default "0000-00-00 00:00:00" comment "订单创建时间",
    pay_time datetime not null default "0000-00-00 00:00:00" comment "付款时间",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_oid`  (`oid`) using btree
) engine=InnoDB AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = 'sku销售信息';


-- ALTER TABLE wms.order_skus
-- ADD title varchar(300) not null default "unknow" comment "品牌"


-- ALTER TABLE wms.order_skus
-- ADD `port` varchar(300) not null default "unknow" comment "渠道"

-- ALTER TABLE wms.order_skus
-- ADD product_id varchar(300) not null default "unknow" comment "商品id"


-- ALTER TABLE wms.order_skus
-- ADD comments varchar(300) not null default "unknow" comment "商家备注"