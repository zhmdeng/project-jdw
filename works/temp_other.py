
import datetime
import sys
import os

import pandas as pd

from utils.combine_files import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config

if __name__ == '__main__':
    log_file = "temp_other"
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    try:
        logs.info("", f"Job begin ...........", log_file)
        db_info = config.get_parameters('wms')
        # tmall = f"""
        #             select distinct  title,`port`,store,buyer_nick,a.order_id as tid,a.sku_name,a.`outer` as outer_code,a.code,a.product_attribut,a.order_total_fee,a.refund_money,a.created,a.num,-- a.tag,
        #             b.product_name,b.active_price,b.retail_price,b.S_price,b.prime_cost,b.distributorship_price from
        #             (select *
        #                         -- ,case when created <= '2022-12-31' then '2022-9-30' else '2022-12-31' end as tag
        #                         ,case when refund_money = '无退款申请' then 0.00 else refund_money end as refund
        #             from
        #             -- 获取port/title
        #             (select d.*,c.title,c.`port`,c.store,c.buyer_nick
        #             from (select title,`port`,tid,store,buyer_nick from wms.orders ) c
        #             inner join (select distinct os.*,
        #                                SUBSTRING_INDEX( SUBSTRING_INDEX( os.outer_code, '+', h.help_topic_id + 1 ), ';',- 1 ) AS `outer`
        #
        #             from wms.order_skus os
        #             join mysql.help_topic h on h.help_topic_id < ( ( length(os.outer_code) - length( REPLACE (os.outer_code, '+', '' ) ) + 1 ) )
        #             where order_status = '没有申请退款') d
        #             on c.tid = d.order_id) e)  a
        #             left join
        #             (select product_id as outer_code,product_name,active_price,retail_price,S_price,prime_cost,distributorship_price,load_date from wms.price  where load_date = '2022-12-31 00:00:00') b
        #             on  a.outer_code = b.outer_code -- a.tag = b.load_date and
        #             where a.outer_code is not null and b.outer_code is not null
        # """
        # tmall = base.read_data(tmall, db_info)
        # logs.info("", f"tmall load successful ...........", log_file)
        # print(tmall.columns)
        nontmall = f"""
                    select * from (
                    SELECT
                           distinct tid as order_id,title,created,port,order_status,num,order_total_fee,
                                    SUBSTRING_INDEX( SUBSTRING_INDEX( a.order_title, ';', h.help_topic_id + 1 ), ';',- 1 ) AS sku_name ,
                                    SUBSTRING_INDEX( SUBSTRING_INDEX( a.num_iid, ';', h.help_topic_id + 1 ), ';',- 1 ) AS outer_code
                    from wms.orders a
                    join mysql.help_topic h on h.help_topic_id < ( ( length( a.order_title) - length( REPLACE ( a.order_title, ';', '' ) ) + 1 ) )
                    where order_status = '交易成功') a 
                    where  `port` != '天猫'
        """
        nontmall = base.read_data(nontmall, db_info)
        logs.info("", f"nontmall load successful ...........", log_file)
       #  print(nontmall.columns)
       #  tmall = tmall[['title', 'port', 'store', 'buyer_nick', 'tid', 'product_name', 'outer_code',
       # 'code', 'product_attribut', 'order_total_fee', 'refund_money',
       # 'created', 'num', 'product_name', 'active_price', 'retail_price',
       # 'S_price', 'prime_cost', 'distributorship_price']]
       #
       #  tmall = tmall.reset_index()
       #  nontmall = nontmall.reset_index()
       #  final_data = pd.concat([tmall,nontmall],axis=1)
       #  logs.info("", f"data concat successful ...........", log_file)
       #  print(final_data)
       #  del final_data['index']

        # save to database
        db_info = config.get_parameters('wms')
        con = base.get_connection(db_info)

        # base.save_sql(nontmall, "order_skus", con, "wms", log_file)
        # logs.info("", "Job run successful ...........\n", log_file)


    except Exception as e:
        print(e)
        logs.info("", f"Exception is:\n\t{e}\n", log_file)
        logs.warning("", "Warning ........... some bugs need you to solve!\n", log_file)