
import datetime as dt

from utils.combine import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config
from utils.trans_files import Transfer
from utils.generate import Generate


if __name__ == '__main__':
    log_file = 'temp_tmall'
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    transfer = Transfer()
    generate = Generate()
    try:
            logs.info("", "Job begin:", log_file)
            # read path
            path = r"E:\tmall"
            # output file name
            final_name = "orders"
            # output path
            path_ = r"E:\orders\combine"

            # get and set begin and end date
            db_info = config.get_parameters('wms')

            order = f"""
                    select * from wms.orders where port = '天猫' 
                    """
            order = base.read_data(order, db_info)

            end_time = max(order['created'])
            begin_time = end_time + dt.timedelta(days=-80)
            logs.info("", f"begin time: {begin_time}", log_file)
            logs.info("", f"end time: {end_time}", log_file)
            combine = Combine()
            final_data = combine.get_all_files(path,log_file)
            logs.info("", f"files combine successful ...........", log_file)

            # data cleaning
            final_data = final_data[['订单编号','买家会员昵称','支付单号','买家应付货款','买家应付邮费','买家支付积分','总金额','返点积分',
            '买家实际支付金额','买家实际支付积分','订单状态','收货人姓名','收货地址','运送方式','联系手机','订单创建时间','订单付款时间 ','宝贝标题 ',
            '物流单号 ','宝贝总数量','修改后的sku','发货时间','物流公司','店铺名称']]

            final_data.columns = ['tid','buyer_nick','alipay_no','order_total_fee','post_fee','point_fee','total_fee','buyer_obtain_point_fee',
            'payment','real_point_fee','order_status','receiver_name','receiver_address','shipping_type','receiver_mobile','created','pay_time','order_title',
            'sid','num','sku_id','consign_time','shipping_company_name','store']

            final_data['load_date'] = date.current_time()
            final_data['pay_time'] = final_data['pay_time'].fillna(value='1970-01-01')
            # final_data['end_time'] = final_data['end_time'].fillna(value='1970-01-01')
            final_data['consign_time'] = final_data['consign_time'].fillna(value='1970-01-01')
            final_data = final_data.fillna(value=0)
            # final_data['buyer_nick'] = final_data['pay_time'].fillna(value='unknow')
            # final_data['alipay_no'] = final_data['alipay_no'].fillna(value='000000')

            col_name = ['tid','order_total_fee','post_fee','point_fee','total_fee','payment','real_point_fee','receiver_name','receiver_mobile','created','pay_time','order_title','sid','sku_id','consign_time']
            new_type = ['int64','float','float','float','float','float','float','str','str','datetime64','datetime64','str','str','str','datetime64']
            base.retype(final_data,col_name,new_type,log_file)
            final_data.reset_index(drop=True)
            final_data['pay_way'] = '支付宝'
            final_data['port'] = '天猫'
            final_data = final_data.reset_index(drop=True)

            final_data['receiver_state']=''
            final_data['receiver_city']=''
            final_data['receiver_district']=''
            final_data['receiver_town']=''

            final_data['title']=''
            for i in range(len(final_data)):
                if final_data['receiver_address'][i] is None:
                    continue
                else:
                    final_data['receiver_state'][i] = final_data['receiver_address'][i].split(' ')[0]
                    final_data['receiver_city'][i] = final_data['receiver_address'][i].split(' ')[1]
                    final_data['receiver_district'][i] = final_data['receiver_address'][i].split(' ')[2]
                    final_data['receiver_town'][i] = final_data['receiver_address'][i].split(' ')[3]

                if final_data['store'][i] == 'doctorsbest海外旗舰店':
                    final_data['title'][i] = "Doctor's Best"
                elif final_data['store'][i] == 'ZIPFIZZ海外旗舰店':
                    final_data['title'][i] = "Zipfizz"
                elif final_data['store'][i] == '舞昆海外旗舰店':
                    final_data['title'][i] = "MAIKON"
                else:
                    continue

            print(len(final_data))
            final_data = final_data.loc[final_data['created'] >= begin_time]
            final_data.drop_duplicates(['tid', 'buyer_nick', 'alipay_no', 'order_total_fee', 'post_fee','point_fee', 'total_fee', 'buyer_obtain_point_fee', 'payment',
            'real_point_fee', 'order_status', 'receiver_name', 'receiver_address','shipping_type', 'receiver_mobile', 'created', 'pay_time',
            'order_title', 'sid', 'num', 'sku_id', 'consign_time','shipping_company_name', 'title', 'load_date', 'pay_way', 'port',
            'receiver_state', 'receiver_city', 'receiver_district', 'receiver_town','store'])
            print(len(final_data))

            # save to csv
            time = str(max(final_data['created'])).split(" ")[0]
            final_data.to_csv(path_ + "/" + final_name + f"{time}" + ".csv", index=False)
            logs.info("", "data load to excel successful ...........", log_file)

            # # delete lasted 3 months data
            # delete_data = f"""
            #               delete from wms.orders where port = '天猫' and created >= '{begin_time}'
            #               """
            # base.excute_sql(delete_data, db_info)
            # logs.critical("",f"data delete successful,sql statment:\n{delete_data}\ntime range:{begin_time} - {end_time}\n",log_file)
            #
            # # save to database
            # db_info = config.get_parameters('wms')
            # con = base.get_connection(db_info)
            #
            # base.save_sql(final_data, "orders", con, "wms", log_file)
            # logs.warning("", "data load to database successfully", log_file)

            move_path = r"E:\orders\history orders\doctors best海外旗舰店"
            path = r"E:\tmall\\"
            transfer.move_file(path,move_path, log_file)

            generate.generate_folder(path,log_file)
            path_drb = r"E:\tmall\Doctor's Best"
            path_zip = r"E:\tmall\Zipfizz"
            path_mai = r"E:\tmall\MAIKON"
            generate.generate_folder(path_drb, log_file)
            generate.generate_folder(path_zip, log_file)
            generate.generate_folder(path_mai, log_file)

            logs.info("", "Job run successful ...........\n", log_file)

    except Exception as e:
        print(e)
        logs.error("", f"Exception is:\n\t{e}\n", log_file)
        logs.warning("", "Warning ........... some bugs need you to solve!\n", log_file)
