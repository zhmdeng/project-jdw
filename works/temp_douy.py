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
    log_file = "temp_douy"
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    transfer = Transfer()
    generate = Generate()
    try:
        # read path
        path = r"E:\douy"
        # output file name
        final_name = "orders_dy"
        # output path
        path_ = r"E:\orders\combine"

        # end_time = datetime.date(2023,1,28) # notice: pay attention to this time will change the end date to load to database
        # end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
        #
        # begin_time = datetime.date(2022, 12,31)  # notice: pay attention to this time will change the end date to load to database
        # begin_time = begin_time.strftime("%Y-%m-%d %H:%M:%S")
        # # end_time = end_time.strptime("%Y-%m-%d %H:%M:%S")

        # get and set begin and end date

        db_info = config.get_parameters('wms')
        order = f"""
                select * from wms.orders where port = '抖音' 
                """
        order = base.read_data(order, db_info)

        end_time = max(order['created'])
        begin_time = end_time+dt.timedelta(days = -82)
        logs.info("", f"begin time: {begin_time}", log_file)
        logs.info("", f"end time: {end_time}", log_file)

        combine = Combine()
        final_data = combine.get_all_files(path,log_file)
        logs.info("", f"files combine successful ....·.......", log_file)

        final_data.reset_index(inplace=True)

        # data cleaning
        final_data = final_data[['主订单编号', '子订单编号', '支付方式', '选购商品', '商品ID', '商家编码', '商品数量', '商品金额',
                                 '订单提交时间', '支付完成时间', '订单完成时间', '订单状态', '发货时间', '订单应付金额',
                                 '运费', '优惠总金额', '收件人', '收件人手机号', '省', '市', '区', '街道', '详细地址',
                                 '仓库名称','title']]

        final_data.columns = ['tid', 'oid', 'pay_way', 'order_title', 'order_num_iid', 'outer_iid', 'num', 'total_fee',
                              'created', 'pay_time', 'end_time', 'order_status', 'consign_time', 'order_total_fee',
                              'post_fee', 'order_discount_fee', 'receiver_name', 'receiver_mobile', 'receiver_state',
                              'receiver_city', 'receiver_district', 'receiver_town', 'receiver_address',
                              'store_code','title']

        final_data['load_date'] = date.current_time()
        final_data['pay_time'] = final_data['pay_time'].fillna(value='1970-01-01')
        final_data['end_time'] = final_data['end_time'].fillna(value='1970-01-01')
        final_data['consign_time'] = final_data['consign_time'].fillna(value='1970-01-01')
        final_data['total_fee'] = final_data['total_fee'].fillna(value=0.00)
        final_data['order_total_fee'] = final_data['order_total_fee'].fillna(value=0.00)
        final_data['order_discount_fee'] = final_data['order_discount_fee'].fillna(value=0.00)
        final_data['outer_iid'] = final_data['outer_iid'].fillna(value='000000')
        final_data.to_csv(path_ + "/" + "final_name" + ".csv", index=False)

        # final_data['total_fee'] = [lambda x:x.replace(",","") for x in final_data['total_fee']]
        # print(final_data['total_fee'][20741])
        print(len(final_data))
        final_data_ = final_data.iloc[:28740,:]
        _final_data_ = final_data.iloc[28740:, :]
        def replace_(data):
            
            for i in range(len(data)):

                data['total_fee'][i] = str(data['total_fee'][i]).replace(",", "")
                data['order_total_fee'][i] = str(data['order_total_fee'][i]).replace(",", "")
                data['order_discount_fee'][i] = str(data['order_discount_fee'][i]).replace(",", "")

                if (data['order_status'][i] is "已完成") and (data['order_status'][i] is not None):
                    data['order_status'][i] = "交易成功"
                else:
                    continue
            return data

        final_data_.reset_index(inplace=True)
        _final_data_.reset_index(inplace=True)
        final_data_ = replace_(final_data_)
        print(11111111111)
        _final_data_ = replace_(_final_data_)

        final_data = pd.concat([final_data_,_final_data_],axis=0)
        final_data = pd.DataFrame(final_data)
        del final_data['index']
        final_data = final_data.reset_index(drop=True)
        final_data.to_csv(path_ + "/" + final_name + "test" + ".csv", index=False)
        final_data['store'] = ''

        for i in range(len(final_data)):
            if final_data['title'][i] == "Doctor's Best":
                final_data['store'][i] = '多特倍斯'
            elif final_data['title'][i] == "Zipfizz":
                final_data['store'][i] = 'zipfizz能量滋滋官方旗舰店'
            elif final_data['title'][i] == "MAIKON":
                final_data['store'][i] = 'MAIKON舞昆海外旗舰店'
            else:
                continue

        col_name = ['total_fee', 'created', 'pay_time', 'end_time', 'consign_time', 'order_total_fee', 'order_total_fee', 'load_date','store_code']
        new_type = ['float', 'datetime64', 'datetime64', 'datetime64', 'datetime64', 'float', 'float', 'datetime64','str']
        base.retype(final_data, col_name, new_type,log_file)
        final_data.reset_index(drop=True)
        final_data['port'] = '抖音'
        print(2)
        final_data = final_data.loc[final_data['created'] >= begin_time]

        print(len(final_data))
        final_data = final_data.loc[final_data['created'] >= begin_time]
        final_data.drop_duplicates(['tid', 'oid', 'pay_way', 'order_title', 'order_num_iid', 'outer_iid',
                                    'num', 'total_fee', 'created', 'pay_time', 'end_time', 'order_status',
                                    'consign_time', 'order_total_fee', 'post_fee', 'order_discount_fee',
                                    'receiver_name', 'receiver_mobile', 'receiver_state', 'receiver_city',
                                    'receiver_district', 'receiver_town', 'receiver_address', 'store_code',
                                    'title', 'load_date', 'store', 'port'], inplace=True)
        print(len(final_data))

        # save to csv
        time = str(max(final_data['created'])).split(" ")[0]
        final_data.to_csv(path_ + "/" + final_name + f"{time}" + ".csv", index=False)
        logs.info("", "data load to excel successful ...........", log_file)

        # # delete lasted 3 months data
        # delete_data = f"""
        #               delete from wms.orders where port = '抖音' and created >= '{begin_time}'
        #               """
        # base.excute_sql(delete_data,db_info)
        # logs.info("", f"data delete successful,sql statement:\n{delete_data}\ntime range:{begin_time} - {end_time}\n", log_file)
        #
        #
        # # save to database
        # con = base.get_connection(db_info)
        # base.save_sql(final_data, "orders", con, "wms", log_file)
        # logs.info("", "Job run successful ...........\n", log_file)

        move_path = r"E:\orders\history orders\douy"
        path = r"E:\douy\\"
        transfer.move_file(path, move_path, log_file)

        generate.generate_folder(path, log_file)
        path_drb = r"E:\douy\Doctor's Best"
        path_zip = r"E:\douy\Zipfizz"
        generate.generate_folder(path_drb, log_file)
        generate.generate_folder(path_zip, log_file)

        logs.info("", "Job run successful ...........\n", log_file)


    except Exception as e:
        print(e)
        except_type, except_value, except_traceback = sys.exc_info()
        except_file = os.path.split(except_traceback.tb_frame.f_code.co_filename)[1]
        exc_dict = {
            "type": except_type,
            "info": except_value,
            "file name": except_file,
            "line": except_traceback.tb_lineno,
        }
        # print(exc_dict)

        logs.error("", f"Exception is:\n\t{exc_dict}\n", log_file)
        logs.warning("", "Warning ........... some bugs need you to solve!\n", log_file)
        raise e
