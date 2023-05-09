import re

import pandas as pd

import datetime as dt
from datetime import datetime

from utils.combine import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config
from utils.trans_files import Transfer
from utils.generate import Generate

if __name__ == '__main__':
    log_file = "sku"
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    transfer = Transfer()
    generate = Generate()
    try:
        # read path
        combine = Combine()
        # output file name
        final_name = r"\sku"
        # output path
        path_ = r"E:\orders\combine"

        db_info = config.get_parameters('wms')

        order = f"""
                select created from wms.order_skus where created !='0000-00-00'
                """
        order = base.read_data(order, db_info)

        # print(type(order['created'][0]))
        # order['created'] = pd.to_datetime(order['created'],format="%Y-%m-%d %H:%M%S",errors='ignore')
        end_time = max(order['created'])
        # end_time = datetime.strptime(end_time,"%Y-%m-%d")

        begin_time = end_time + dt.timedelta(days=-80)
        logs.info("", f"begin time: {begin_time}", log_file)
        logs.info("", f"end time: {end_time}", log_file)

        # 天猫
        path = r"E:\tmall sku"
        tmall = combine.get_all_files(path, log_file)
        logs.info("", f"files combine successful ...........", log_file)
        logs.info("", f"{tmall.head(5)}", log_file)
        print(tmall['title'])

        tmall.reset_index(inplace=True)
        # tmall["子订单编号"] = tmall["子订单编号"].str.extract(r'(\d+)', expand=True).astype('str')
        # tmall["主订单编号"] = tmall["主订单编号"].str.extract(r'(\d+)', expand=True).astype('str')
        # tmall["支付单号"] = tmall["支付单号"].str.ex tract(r'(\d+)', expand=True).astype('str')
        # data cleaning
        for col in ["子订单编号", "主订单编号", "支付单号"]:
            tmall[f"{col}"] = tmall[f"{col}"].str.extract(r'(\d+)', expand=True).astype('str')
        tmall.to_csv(path_ + "test" + ".csv", index=False)
        logs.info("", "data load to excel successful ...........", log_file)

        # for i in range(len(tmall)):
        #     if type(tmall["子订单编号"][i]) is None:
        #         continue
        #     else:
        #        tmall["子订单编号"][i] = tmall["子订单编号"][i].str.extract(r'(\d+)', expand=True).astype('str')
        # for i in range(len(tmall)):
        #     print(tmall[f"{col}"][i])
        #     tmall[f"{col}"][i] = tmall[f"{col}"][i].str.extract(r'(\d+)', expand=True).astype('str')
        # tmall["子订单编号"] = tmall["子订单编号"].str.extract(r'(\d+)', expand=True).astype('str')
        # tmall["主订单编号"] = tmall["主订单编号"].str.extract(r'(\d+)', expand=True).astype('str')
        # tmall["支付单号"] = tmall["支付单号"].str.extract(r'(\d+)', expand=True).astype('str')
        print(tmall["子订单编号"][1])

        tmall = tmall[['子订单编号', '主订单编号', '标题', '价格', '购买数量', '外部系统编号', '商品属性', '套餐信息', '备注',
                       '订单状态', '商家编码', '支付单号', '买家应付货款', '买家实际支付金额', '退款状态', '退款金额', '订单创建时间', '订单付款时间', 'title']]

        tmall.columns = ['oid', 'order_id', 'sku_name', 'price', 'num', 'outer_code', 'product_attribut', 'info','postscript',
                         'order_status', 'code', 'pay_code', 'order_total_fee', 'order_payment', 'refund_status','refund_money', 'created', 'pay_time', 'title']

        values = ['000000', '000000', '000000', -1.00, 0, '000000', 'unknow', 'unknow', 'unknow',
                  'unknow', '000000', '000000', -1.00, -1.00, 'unknow', -1.00, '0000-00-00 00:00:00',
                  '0000-00-00 00:00:00', 'unknow']
        base.fillna_col(tmall, tmall.columns, values, log_file)

        tmall['port'] = '天猫'
        logs.info("", f"******************* tmall data load successfully! data size:{len(tmall)} *******************",
                  log_file)

        # 抖音
        d_path = r"E:\douy sku"
        douy = combine.get_all_files(d_path, log_file)
        logs.info("", f"douy files combine successful ...........", log_file)

        douy = douy[['主订单编号', '子订单编号', '选购商品', '商品规格', '商品数量', '商家编码',
                     '订单应付金额', '订单提交时间', '订单状态', '商品单价', 'title', '买家留言',
                     '支付完成时间', '售后状态', '商家编码', '商品ID']]

        douy.columns = ['oid', 'order_id', 'sku_name', 'product_attribut', 'num', 'outer_code',
                        'order_total_fee', 'created', 'order_status', 'price', 'title', 'postscript',
                        'pay_time', 'refund_status', 'code', 'product_id']

        douy_ = douy.iloc[:45509, :]
        _douy_ = douy.iloc[45509:, :]

        def replace_(data):

            for i in range(len(data)):
                print(data['refund_status'][i])
                data['product_id'][i] = str(data['product_id'][i]).strip()
                data['order_total_fee'][i] = str(data['order_total_fee'][i]).replace(",", "")
                data['outer_code'][i] = str(data['outer_code'][i]).strip()
                data['code'][i] = str(data['code'][i]).strip()

                if (data['order_status'][i] is "已完成") and (data['order_status'][i] is not None):
                    data['order_status'][i] = "交易成功"
                else:
                    continue

                if data['refund_status'][i] is '-':
                    data['refund_status'][i] = '无退款'
                else:
                    continue
            return data

        douy_.reset_index(inplace=True)
        _douy_.reset_index(inplace=True)
        douy_ = replace_(douy_)
        _douy_ = replace_(_douy_)

        douy = pd.concat([douy_, _douy_], axis=0)
        douy = pd.DataFrame(douy)
        print(douy.columns)
        del douy['index']

        values = ['000000', '000000', '000000', 'unknow', 0, '000000', -1.00, '0000-00-00 00:00:00', 'unknow', -1.00,
                  'unknow', 'unknow', '0000-00-00 00:00:00', 'unknow', '000000', 'unknow']
        base.fillna_col(douy, douy.columns, values, log_file)
        douy['port'] = '抖音'
        final_data = douy
        logs.info("", f"******************* douy data load successfully! data size:{len(douy)} *******************",
                  log_file)

        ## 快手
        k_path = r"E:\kshou sku"
        combine = Combine()
        kshou = combine.get_all_files(k_path, log_file)
        logs.info("", f"kshou files combine successful ...........", log_file)
        print(kshou.columns)

        kshou['outer_code'] = ''
        kshou['code'] = ''
        for i in range(len(kshou)):
            if kshou['商品ID'][i] == 15494940650775:
                kshou['outer_code'][i] = 'DRB-00183'
                kshou['code'][i] = 'DRB-00183'
            elif kshou['商品ID'][i] == 15409677795775:
                kshou['outer_code'][i] = 'DRB-00257'
                kshou['code'][i] = 'DRB-00257'
            elif kshou['商品ID'][i] == 15381735108775:
                kshou['outer_code'][i] = 'DRB-00334'
                kshou['code'][i] = 'DRB-00334'
            elif kshou['商品ID'][i] == 5066958893775:
                kshou['outer_code'][i] = 'DRB-00257'
                kshou['code'][i] = 'DRB-00257'
            elif kshou['商品ID'][i] == 5061736370775:
                kshou['outer_code'][i] = 'DRB-00198'
                kshou['code'][i] = 'DRB-00198'
            elif kshou['商品ID'][i] == 5061728594775:
                kshou['outer_code'][i] = 'DRB-00501'
                kshou['code'][i] = 'DRB-00501'
            elif kshou['商品ID'][i] == 4765856376775:
                kshou['outer_code'][i] = 'DRB-00025'
                kshou['code'][i] = 'DRB-00025'
            elif kshou['商品ID'][i] == 3900475775775:
                kshou['outer_code'][i] = 'DRB-00547C'
                kshou['code'][i] = 'DRB-00547C'
            elif kshou['商品ID'][i] == 15424452589775:
                kshou['outer_code'][i] = 'DRB-00257'
                kshou['code'][i] = 'DRB-00257'
            elif kshou['商品ID'][i] == 15381771086775:
                kshou['outer_code'][i] = 'DRB-00595C'
                kshou['code'][i] = 'P31052118234398178'
            elif kshou['商品ID'][i] == 4255052396775:
                kshou['outer_code'][i] = 'DRB-00580C'
                kshou['code'][i] = 'P31052118213487678'
            elif kshou['商品ID'][i] == 4035845427775:
                kshou['outer_code'][i] = 'DRB-00183'
                kshou['code'][i] = 'DRB-00183'
            elif kshou['商品ID'][i] == 3961275281775:
                kshou['outer_code'][i] = 'DRB-00585C'
                kshou['code'][i] = 'DRB-00585C'
            else:
                continue

        kshou = kshou[['outer_code', 'code', '订单号', '订单号', '订单创建时间', '订单支付时间', '订单状态', '实付款', '成交数量', '买家留言', '退货退款',
                       '商品名称', '商品规格', '商品单价', 'title', '商品ID']]

        kshou.columns = ['outer_code', 'code', 'oid', 'order_id', 'created', 'pay_time', 'order_status',
                         'order_total_fee', 'num', 'postscript', 'refund_status',
                         'sku_name', 'product_attribut', 'price', 'title', 'product_id']

        values = ['000000', '000000', '000000', '000000', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 'unknow', -1.00,
                  0, 'unknow', 'unknow',
                  '000000', 'unknow', -1.0, 'unknow', 'unknow']
        base.fillna_col(kshou, kshou.columns, values, log_file)
        kshou['port'] = '快手'
        for col in ['order_total_fee', 'price']:
            kshou[f"{col}"] = kshou[f"{col}"].str.extract(r'(\d+)', expand=True).astype('str')
        logs.info("", f"******************* kshou data load successfully! data size:{len(kshou)} *******************",
                  log_file)

        ## private
        p_path = r"E:\youz sku"
        private = combine.get_all_files(p_path, log_file)
        logs.info("", f"private files combine successful ...........", log_file)
        print(private.columns)

        # private = private.loc[~private['库存类型'].isin(['非淘ToC'])]

        private = private[['订单号', '订单号', '订单商品状态', '交易成功时间', '商品名称', '商品规格', '规格编码', '商品编码',
                           '商品单价', '商品数量', '商品实际成交金额', '买家备注', '商品退款状态', '商品已退款金额', 'title', '外部支付流水号', '商家订单备注']]

        private.columns = ['oid', 'order_id', 'order_status', 'created', 'sku_name', 'product_attribut', 'outer_code',
                           'code',
                           'price', 'num', 'order_total_fee', 'postscript', 'refund_status', 'refund_money', 'port',
                           'pay_code', 'comments']

        code = config.get_parameters('code')
        private['title'] = ''

        logs.info("", f"{code}", log_file)
        for i in range(len(private)):


            private['outer_code'][i] = str(private['outer_code'][i]).strip()
            private['code'][i] = str(private['code'][i]).strip()

            # logs.info("", f"{private['outer_code'][i].lower()}", log_file)
            # logs.info("", f"{len(private['outer_code'][i])}", log_file)
            # logs.info("", f"{code.get(private['outer_code'][i].lower())}", log_file)

            if "Doctor’s Best" in str(private['sku_name'][i]) or ("Doctor's" in str(private['sku_name'][i])) or (
                    "DRB" in str(private['sku_name'][i])) or ("DRB" in str(private['outer_code'][i])) or (
                    "DRB" in str(private['product_attribut'][i])):
                private['title'][i] = "Doctor's Best"
            elif 'Zipfizz' in str(private['sku_name'][i]) or ("zip" in str(private['outer_code'][i])) or (
                    "zip" in str(private['product_attribut'][i])):
                private['title'][i] = "Zipfizz"
            elif '舞昆' in str(private['sku_name'][i]):
                private['title'][i] = "MAIKON"
            elif '金乐心' in str(private['sku_name'][i]):
                private['title'][i] = "金乐心"
            elif 'Labrada' in str(private['sku_name'][i]) or ("LABRADA" in str(private['sku_name'][i])):
                private['title'][i] = "Labrada"
            else:
                continue

            if code.get(private['code'][i].lower()) == None:

                if code.get(private['outer_code'][i].lower()) == None:
                    logs.info("", f"{private['outer_code'][i]}", log_file)
                    continue
                else:
                    private['outer_code'][i] = code.get(private['outer_code'][i].lower()).replace("'", "")
            else:
                private['outer_code'][i] = code.get(private['code'][i].lower()).replace("'", "")

            if private['refund_money'][i] == 0:
                private['refund_status'][i] = '无退款'
            else:
                continue

        values = ['000000', '000000', 'unknow', '0000-00-00 00:00:00', 'unknow', 'unknow', '000000', '000000',
                  -1.00, 0, -1.00, 'unknow', 'unknow', -1.00, 'unknow', 'unknow', 'unknow', 'unknow']

        base.fillna_col(private, private.columns, values, log_file)
        logs.info("",
                  f"******************* private data load successfully! data size:{len(private)} *******************",
                  log_file)

        # # combine
        tmall = tmall.reset_index(drop=True)
        douy = douy.reset_index(drop=True)
        kshou = kshou.reset_index(drop=True)
        private = private.reset_index(drop=True)

        final_data = pd.concat([tmall, douy, kshou, private], axis=0)
        final_data['load_date'] = date.current_time()
        final_data['update_date'] = date.current_time()
        print(len(final_data))
        print(final_data.columns)
        final_data.drop_duplicates(
            ['oid', 'order_id', 'order_status', 'created', 'sku_name', 'product_attribut', 'outer_code',
             'code', 'price', 'num', 'order_total_fee', 'postscript', 'refund_status', 'refund_money',
             'port', 'pay_code', 'title', 'product_id', 'comments'], inplace=True)
        # col_name = ['created']
        # new_type = ['datetime64']
        # base.retype(final_data, col_name, new_type, log_file)
        final_data['created'] = pd.to_datetime(final_data['created'], errors="coerce")
        print(begin_time)
        final_data = final_data.loc[final_data['created'] >= begin_time]
        print(len(final_data))
        # # save to csv
        time = str(max(final_data['created'])).split(" ")[0]
        final_data.to_csv(path_ + "test.csv", index=False)
        # final_data.to_csv(path_ +  final_name + f"{time}" + ".csv", index=False)
        logs.info("", "data load to excel successful ...........", log_file)
        print(final_data.columns)
        col_name = ['oid', 'order_id', 'sku_name', 'price', 'num', 'outer_code', 'product_attribut', 'info',
                    'postscript', 'order_status',
                    'code', 'pay_code', 'order_total_fee', 'order_payment', 'refund_status', 'refund_money', 'created',
                    'title', 'port',
                    'product_id', 'comments', 'load_date', 'update_date']

        values = ['000000', '000000', '000000', -1.00, 0, '000000', 'unknow', 'unknow', 'unknow', 'unknow',
                  '000000', '000000', -1.00, -1.00, 'unknow', '-1.00', '1970-01-01 01:01:01', '1970-01-01 01:01:01',
                  'unknow', 'unknow',
                  'unknow', 'unknow', '1970-01-01 01:01:01', '1970-01-01 01:01:01']
        base.fillna_col(final_data, final_data.columns, values, log_file)

        new_type = ['str', 'str', 'str', 'float', 'int', 'str', 'str', 'str', 'str', 'str',
                    'str', 'str', 'float', 'float', 'str', 'str', 'datetime64', 'str', 'str',
                    'str', 'str', 'datetime64', 'datetime64']
        base.retype(final_data, col_name, new_type, log_file)

        print(min(final_data['created']))

        # save to csv
        final_data.to_csv(path_ + final_name + f"{time}" + ".csv", index=False)
        logs.info("", "data load to excel successfully", log_file)

        # # delete lasted 3 months data from wms.order_skus table
        # del_data = f"""
        #             select count(*) from wms.order_skus where created >= '{begin_time}'
        #             """
        # del_data = base.read_data(del_data,db_info)
        #
        # delete_data = f"""
        #               delete from wms.order_skus where created >= '{begin_time}'
        #               """
        # base.excute_sql(delete_data,db_info)
        #
        # logs.critical("", f"data delete successful,data length:{del_data},sql statement:\n{delete_data}\ntime range:{begin_time} - {end_time}\n", log_file)
        # print(len(final_data))
        #
        # # save to database
        # db_info = config.get_parameters('wms')
        # con = base.get_connection(db_info)
        #
        # base.save_sql(final_data, "order_skus", con, "wms", log_file)
        # logs.warning("", "data load to database successfully",log_file)
        #
        #
        #
        #
        # # move file folder and generate new folders
        # path_tmall = r"E:\sku\tmall"
        # path_douy = r"E:\sku\douy"
        # path_kshou = r"E:\sku\kshou"
        # path_youz = r"E:\sku\youz"
        #
        # path1 = r"E:\tmall sku"
        # path2 = r"E:\douy sku"
        # path3 = r"E:\kshou sku"
        # path4 = r"E:\youz sku"
        # transfer.move_file(path1, path_tmall, log_file)
        # transfer.move_file(path2, path_douy, log_file)
        # transfer.move_file(path3, path_kshou, log_file)
        # transfer.move_file(path4, path_youz, log_file)
        #
        # generate.generate_folder(path1, log_file)
        # generate.generate_folder(path2, log_file)
        # generate.generate_folder(path3, log_file)
        # generate.generate_folder(path4, log_file)
        # path_drb = r"E:\tmall sku\Doctor's Best"
        # path_zip = r"E:\tmall sku\Zipfizz"
        # path_mai = r"E:\tmall sku\MAIKON"
        # generate.generate_folder(path_drb, log_file)
        # generate.generate_folder(path_zip, log_file)
        # generate.generate_folder(path_mai, log_file)
        # path_drb = r"E:\douy sku\Doctor's Best"
        # path_zip = r"E:\douy sku\Zipfizz"
        # generate.generate_folder(path_drb, log_file)
        # generate.generate_folder(path_zip, log_file)
        # path_drb = r"E:\kshou sku\Doctor's Best"
        # generate.generate_folder(path_drb, log_file)
        # path_drb = r"E:\youz sku\私域"
        # generate.generate_folder(path_drb, log_file)

        logs.info("", "Job run successfully\n", log_file)

    except Exception as e:
        print(e)
        logs.error("", f"Exception is:\n\t{e}\n", log_file)
        logs.warning("", "Warning ........... some bugs need you to solve!\n", log_file)
        # raise ValueError(
        #     f"{e}"
        # )
