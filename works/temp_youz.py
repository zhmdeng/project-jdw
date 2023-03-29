
import datetime as dt
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
    log_file = "temp_youz"
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    try:
        # read path
        path = r"E:\youz"
        # output file name
        final_name = "youz"
        # output path
        path_ = r"E:\orders\combine"

        # get and set begin and end date
        db_info = config.get_parameters('wms')
        order = f"""
                select * from wms.orders where port = '私域' -- and title = ""
                """
        order = base.read_data(order, db_info)

        end_time = max(order['created'])
        begin_time = end_time + dt.timedelta(days=-90)
        logs.info("", f"begin time: {begin_time}", log_file)
        logs.info("", f"end time: {end_time}", log_file)

        combine = Combine()
        final_data = combine.get_all_files(path, log_file)
        logs.info("", f"files combine successful ....·.......", log_file)
        print(final_data.columns)
        # data cleaning
        final_data = final_data[['订单号', '归属店铺', '订单类型', '订单状态', '订单创建时间', '买家付款时间', '商品种类数',
                            '付款方式', '支付流水号', '商品金额合计', '运费', '店铺优惠合计',
                            '应收订单金额', '订单实付金额', '全部商品名称','收货人/提货人', '收货人手机号/提货人手机号',
                            '收货人省份', '收货人城市','收货人地区', '详细收货地址/提货地址','买家姓名','订单退款状态']]

        final_data.columns = ['tid', 'store', 'type', 'order_status', 'created', 'pay_time', 'num',
                              'pay_way', 'alipay_no', 'order_total_fee', 'post_fee', 'order_discount_fee',
                              'payment', 'received_payment', 'order_title', 'receiver_name', 'receiver_mobile',
                              'receiver_state','receiver_city','receiver_district','receiver_address','buyer_nick','refund_status']

        # final_data['num'] = final_data['num'].abs()
        # final_data['private'] = ''
        # for i in range(len(final_data)):
        #     if final_data['group'][i] == '非淘ToC':
        #         final_data['private'][i] = 'no'
        #     else:
        #         final_data['private'][i] = 'yes'

        final_data['title'] = ''

        for i in range(len(final_data)):

            final_data['tid'][i] = str(final_data['tid'][i]).strip()
            final_data['alipay_no'][i] = str(final_data['alipay_no'][i]).strip()

            if "Doctor’s Best" in str(final_data['order_title'][i]) or ("Doctor's" in str(final_data['order_title'][i])) or ("DRB" in str(final_data['order_title'][i])):
                final_data['title'][i] = "Doctor's Best"
            elif 'Zipfizz' in str(final_data['order_title'][i]) or ("zip" in str(final_data['order_title'][i])):
                final_data['title'][i] = "Zipfizz"
            elif '舞昆' in str(final_data['order_title'][i]):
                final_data['title'][i] = "MAIKON"
            elif '金乐心' in str(final_data['order_title'][i]):
                final_data['title'][i] = "金乐心"
            elif 'Labrada' in str(final_data['order_title'][i]) or ("LABRADA" in str(final_data['order_title'][i])):
                final_data['title'][i] = "Labrada"
            else:
                continue

        values = ['000000', 'unknow', 'unknow', 'unknow', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0,
                  'unknow', '000000', -1.00, -1.00, -1.00,
                  -1.00, -1.00, 'unknow', 'unknow', '000000',
                  'unknow', 'unknow', 'unknow', 'unknow', 'unknow', 'unknow', 'unknow']
        base.fillna_col(final_data, final_data.columns, values, log_file)
        final_data['port'] = '私域'
        final_data['created'] = pd.to_datetime(final_data['created'], errors="coerce")
        # save to csv
        time = str(max(final_data['created'])).split(" ")[0]
        final_data.to_csv(path_ + "/" + final_name + f"{time}" + ".csv", index=False,encoding='utf-8')
        logs.info("", "final_data load to excel successful ...........", log_file)

        print(len(final_data))
        final_data = final_data.loc[final_data['created'] >= begin_time]
        final_data.drop_duplicates(['tid', 'store', 'type', 'order_status', 'created', 'pay_time', 'num',
                              'pay_way', 'alipay_no', 'order_total_fee', 'post_fee', 'order_discount_fee',
                              'payment', 'received_payment', 'order_title', 'receiver_name', 'receiver_mobile',
                              'receiver_state','receiver_city','receiver_district','receiver_address','buyer_nick','refund_status','title'])
        print(len(final_data))

        # # delete lasted 3 months data
        # delete_data = f"""
        #               delete from wms.orders where port = '私域' and created >= '{begin_time}'
        #               """
        # base.excute_sql(delete_data, db_info)
        # logs.info("",f"data delete successful,sql statment:\n{delete_data}\ntime range:{begin_time} - {end_time}\n",log_file)
        #
        # # save to database
        # db_info = config.get_parameters('wms')
        # con = base.get_connection(db_info)
        #
        # base.save_sql(final_data, "orders", con, "wms", log_file)
        # logs.info("", "load data to orders run successful ...........\n", log_file)




































        #
        # # load to wms.orders table
        # new_data = pd.read_excel(r"E:\有赞.xlsx")
        # final_data = final_data.loc[~(final_data['group'].isin(['非淘ToC']))]
        # final_data = final_data.loc[(final_data['output_type'].isin(['消费者退货入库','销售出库单']))]
        #
        # new_data = pd.merge(final_data,new_data,left_on=['code','outer_code','LBX_code'],right_on=['商品ID','货品编码','仓储单号'],how='inner')
        # print(len(new_data))
        #
        # new_data = new_data[['store_name','outer_code','group','product_name','num','time',
        #                      '仓出库时间','订单金额','运费','买家收货地址','货品金额',
        #                      '订单状态','快递公司','物流单号','店铺名称','分销店铺名称','外部单号']]
        # new_data.columns = ['store_code','outer_iid','port','order_title','num','created',
        #                     'consign_time','order_total_fee','post_fee','receiver_address','price',
        #                     'order_status','shipping_company_name','sid','store','distributor','tid']
        # print(new_data)
        # new_data.reset_index(inplace=True)
        # new_data.to_excel(r"E:\new_data.xlsx")
        #
        # new_data['receiver_address'] = new_data['receiver_address'].fillna(value='unknow')
        # new_data['receiver_state'] = ''
        # new_data['receiver_city'] = ''
        # new_data['receiver_district'] = ''
        # new_data['receiver_town'] = ''
        #
        # new_data['title'] = ''
        # for i in range(len(new_data)):
        #
        #     new_data['receiver_address'][i] = str(new_data['receiver_address'][i])
        #
        #     if new_data['outer_iid'][i].startswith('DRB'):
        #         new_data['title'][i] = "Doctor's Best"
        #     elif new_data['outer_iid'][i].startswith('zip'):
        #         new_data['title'][i] = "Zipfizz"
        #     elif new_data['outer_iid'][i].startswith('WK'):
        #         new_data['title'][i] = "MAIKON"
        #     else:
        #         new_data['title'][i] = "unknow"
        #
        #     if new_data['port'][i] == '有赞（贴溯源码）':
        #         new_data['port'][i] = '私域'
        #     # elif new_data['port'][i] == '洋葱':
        #     #     new_data['port'][i] = '经/分销'
        #     else:
        #         continue
        #
        #     if new_data['receiver_address'][i] == 'unknow':
        #         continue
        #     elif len(new_data['receiver_address'][i]) == 1:
        #         print(new_data['receiver_address'][i])
        #         new_data['receiver_state'][i] = str(new_data['receiver_address'][i]).split(' ')[0]
        #     elif len(new_data['receiver_address'][i]) == 2:
        #         new_data['receiver_state'][i] = str(new_data['receiver_address'][i]).split(' ')[0]
        #         new_data['receiver_city'][i] = str(new_data['receiver_address'][i]).split(' ')[1]
        #     elif len(new_data['receiver_address'][i]) == 3:
        #         new_data['receiver_state'][i] = str(new_data['receiver_address'][i]).split(' ')[0]
        #         new_data['receiver_city'][i] = str(new_data['receiver_address'][i]).split(' ')[1]
        #         new_data['receiver_district'][i] = str(new_data['receiver_address'][i]).split(' ')[2]
        #     else:
        #         new_data['receiver_state'][i] = str(new_data['receiver_address'][i]).split(' ')[0]
        #         new_data['receiver_city'][i] = str(new_data['receiver_address'][i]).split(' ')[1]
        #         new_data['receiver_district'][i] = str(new_data['receiver_address'][i]).split(' ')[2]
        #         new_data['receiver_town'][i] = str(new_data['receiver_address'][i]).split(' ')[3]
        #
        # print(new_data.columns)
        # new_data = new_data.reset_index(drop=True)
        # del new_data['index']
        # new_data.columns = ['store_code', 'outer_iid', 'port', 'order_title', 'num','created', 'consign_time',
        #                     'order_total_fee', 'post_fee','receiver_address', 'price', 'order_status','shipping_company_name',
        #                      'sid', 'store', 'distributor', 'tid','receiver_state', 'receiver_city','receiver_district',
        #                     'receiver_town', 'title']
        #
        # values = ['unknow', '000000', 'unknow', 'unknow', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00',
        #           -1.00, -1.00,'unknow', -1.00, 'unknow', 'unknow',
        #           '000000','unknow','unknow','0','unknow','unknow','unknow',
        #           'unknow','unknow']
        # base.fillna_col(new_data, new_data.columns, values, log_file)
        #
        # # new_data.to_excel(r"E:\new_data1.xlsx")
        # # base.save_sql(new_data, "orders", con, "wms", log_file)
        # # logs.info("", "load data to wms.orders run successful ...........\n", log_file)

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

        logs.info("", f"Exception is:\n\t{exc_dict}\n", log_file)
        logs.warning("", "Warning ........... some bugs need you to solve!\n", log_file)
        raise e
