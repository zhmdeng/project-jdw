
import datetime as dt
import sys
import os

import pandas as pd

from utils.combine import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config
from utils.trans_files import Transfer
from utils.generate import Generate


if __name__ == '__main__':
    log_file = 'temp_kshou'
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    transfer = Transfer()
    generate = Generate()
    try:
            # read path
            path = r"E:\kshou"
            # output file name
            final_name = "orders_kshou"
            # output path
            path_ = r"E:\orders\combine"

            # get and set begin and end date
            db_info = config.get_parameters('wms')
            order = f"""
                    select * from wms.orders where port = '快手' -- and title = ""
                    """
            order = base.read_data(order, db_info)

            end_time = max(order['created'])
            begin_time = end_time + dt.timedelta(days=-82)
            logs.info("", f"begin time: {begin_time}", log_file)
            logs.info("", f"end time: {end_time}", log_file)

            # combine files
            combine = Combine()
            final_data = combine.get_all_files(path,log_file)
            logs.info("", f"files combine successful ...........", log_file)

            # data cleaning
            final_data = final_data[['订单号', '订单创建时间', '订单支付时间', '订单状态', '实付款', '快递费', '支付方式', '成交数量',
            '商品名称', '商品ID','SKU编码', '收货人姓名', '收货人电话', '收货地址-省',
            '收货地址-市', '收货地址-区', '收货地址-街道', '收货地址', '快递单号', '快递公司','title']]

            final_data.columns = ['tid','created','pay_time','order_status','order_total_fee','post_fee','pay_way','num',
            'order_title','order_num_iid','sku_properties_name','receiver_name','receiver_mobile','receiver_state',
            'receiver_city','receiver_district','receiver_town','receiver_address','sid','shipping_company_name','title']

            # for i in final_data.columns:
            #     print(f"{i}:{type(final_data[i][0])}")
            final_data['load_date'] = date.current_time()
            final_data['sku_properties_name'] = final_data['sku_properties_name'].fillna(value='unknow')
            final_data['title'] = final_data['title'].fillna(value='unknow')
            final_data['receiver_town'] = final_data['receiver_town'].fillna(value='unknow')
            final_data['pay_time'] = final_data['pay_time'].fillna(value='1970-01-01')
            final_data['sid'] = final_data['sid'].fillna(value='000000')
            final_data['pay_way'] = final_data['pay_way'].fillna(value='unknow')

            final_data = final_data.reset_index(drop=True)
            final_data['store'] = ''

            for col in ['order_total_fee', 'post_fee']:
                final_data[f"{col}"] = final_data[f"{col}"].str.extract(r'(\d+)', expand=True).astype('str')

            # for i in range(len(final_data)):
            #     print(i)
            #     print(final_data['post_fee'][i])
            #
            #     final_data['order_total_fee'][i] = str(final_data['order_total_fee'][i]).replace("¥","")
            #     final_data['post_fee'][i] = str(final_data['post_fee'][i]).replace("¥", "")
            #     print(111111111)
            #     print(final_data['title'][i])
            final_data.to_csv(path_ + "/" + final_name + "-test" + ".csv", index=False)
            logs.info("", "data load to excel successful ...........", log_file)
            print("**************")

            for i in range(len(final_data)):
                if final_data['title'][i] == "Doctor's Best":
                    final_data['store'][i] = '多特倍斯海外官方旗舰店'
                else:
                    continue

            col_name = ['created','pay_time','order_total_fee','post_fee']
            new_type = ['datetime64','datetime64','float','float']
            base.retype(final_data,col_name,new_type,log_file)
            final_data.reset_index(drop=True)
            final_data['port'] = '快手'

            print(len(final_data))
            final_data = final_data.loc[final_data['created'] >= begin_time]
            final_data.drop_duplicates(['tid', 'created', 'pay_time', 'order_status', 'order_total_fee',
             'post_fee', 'pay_way', 'num', 'order_title', 'order_num_iid','sku_properties_name', 'receiver_name', 'receiver_mobile',
             'receiver_state', 'receiver_city', 'receiver_district', 'receiver_town','receiver_address', 'sid', 'shipping_company_name', 'title',
             'load_date', 'store', 'port'])
            print(len(final_data))

            # # save to csv
            # time = str(max(final_data['created'])).split(" ")[0]
            # final_data.to_csv(path_ + "/" + final_name + f"{time}" + ".csv",index=False)
            # logs.info("", "data load to excel successful ...........", log_file)
            #
            # # delete lasted 3 months data
            # delete_data = f"""
            #               delete from wms.orders where port = '快手' and created >= '{begin_time}'
            #               """
            # base.excute_sql(delete_data, db_info)
            # logs.info("",f"data delete successful,sql statment:\n{delete_data}\ntime range:{begin_time} - {end_time}\n",log_file)
            #
            # # save to database
            # db_info = config.get_parameters('wms')
            # con = base.get_connection(db_info)
            #
            # base.save_sql(final_data,"orders",con,"wms",log_file)
            # logs.info("", "Job run successful ...........\n", log_file)

            move_path = r"E:\orders\history orders\kshou\doctor's best"
            path = r"E:\kshou\\"
            transfer.move_file(path, move_path, log_file)

            generate.generate_folder(path, log_file)
            folder = r"E:\kshou\Doctor's Best"

            generate.generate_folder(folder, log_file)


            logs.info("", "Job run successful ...........\n", log_file)

    except Exception as e:
        print(e)
        logs.error("", f"Exception is:\n\t{e}\n", log_file)
        logs.warning("", "Warning ........... some bugs need you to solve!\n", log_file)