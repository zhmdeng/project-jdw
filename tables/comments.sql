

create table if not exists comments(
	id int(32) not null auto_increment,
	child_trade_id bigint(20) not null default 000000 comment "交易子订单ID",
	content varchar(900) not null default "unknow" comment "评价内容",
	posi char(10) not null default "unknow" comment "表示标签的极性(正极true,负极false)",
	tag_name varchar(900) not null default "unknow" comment "表示标签的名称",
	append_content varchar(900) not null default "no comments" comment "追加评价内容",
	append_posi char(10) not null default "unknow" comment "(追评)表示标签的极性(正极true,负极false)",
	appen_tag_name varchar(900) not null default "unknow" comment "(追评)表示标签内容",
	append_time datetime not null default "0000-00-00" comment "追评评价时间",
	append_has_negtv char(10) not null default "unknow" comment "追评中是否含有负向标签",
	user_nick varchar(100) not null default "unknow" comment "表示评价者的昵称",
	has_negtv char(10) not null default "unknow" comment "原始评价是否含有负向标签",
	comment_time datetime not null default "0000-00-00" comment "评价时间",
	ouid varchar(300) not null default "unknow" comment "ouid",
	load_date timestamp not null default current_timestamp() comment "下载时间",
	update_date timestamp not null default current_timestamp() comment "更新时间",
	primary key (id) using btree,
	key `idx_child_trade_id`  (`child_trade_id`) using btree
) engine=InnoDB  AUTO_INCREMENT = 55726 default charset=utf8mb4 COMMENT = '评论';