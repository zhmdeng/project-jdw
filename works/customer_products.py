


from utils.combine import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config
from utils.trans_files import Transfer


if __name__ == '__main__':
    log_file = 'market_info'
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    try:
            # read path
            path = r"E:\marketing"
            # output file name
            final_name = "\market_info"
            # output path
            path_ = r"E:\orders\combine"

            # combine files
            combine = Combine()
            final_data = combine.get_all_files(path,log_file)
            logs.info("", f"files combine successful ...........", log_file)
            print(final_data.columns)
            # data cleaning
            final_data = final_data[['日期', '排名', '商品名称', '商品ID', '商品访客数', '支付买家数', '支付金额','购买偏好TGI']]

            final_data.columns = ['created','ranks','product_name','product_id','visitor_num','pay_num','pay_money','TGI']

            final_data = final_data.reset_index(drop=True)
            for i in range(len(final_data)):
                final_data['visitor_num'][i] = str(final_data['visitor_num'][i]).replace(",", "")
                final_data['pay_money'][i] = str(final_data['pay_money'][i]).replace(",","")
                final_data['pay_ratio'][i] = str(final_data['pay_ratio'][i]).replace("%", "")

            values = ['0000-00-00',0,'unknow','000000',-1,-1,-1.00,-1]
            base.fillna_col(final_data, final_data.columns, values, log_file)

            new_type = ['datetime64','int','str','str','str','float','float','float']
            base.retype(final_data, final_data.columns, new_type, log_file)

            final_data['load_date'] = date.current_time()
            final_data['update_date'] = date.current_time()
            print(len(final_data))
            final_data.drop_duplicates(['sector', 'upper_sector', 'plat', 'created', 'gross_merchandise_volume',
                                        'upper_money', 'pay_ratio', 'load_date', 'update_date'],inplace=True)
            print(len(final_data))
            # save to csv
            time = str(max(final_data['created'])).split(" ")[0]
            final_data.to_csv(path_ + final_name + f"{time}" + ".csv",index=False)
            logs.info("", "data load to excel successful ...........", log_file)

            # # save to database
            # db_info = config.get_parameters('wms')
            # con = base.get_connection(db_info)
            #
            # base.save_sql(final_data,"market_info",con  ,"wms",log_file)
            # logs.info("", "Job run successful ...........\n", log_file)
            #
            # move_path = r"E:\市场"
            # path = r"E:\marketing\\"
            # transfer = Transfer()
            # transfer.move_file(path,move_path, log_file)

    except Exception as e:
        print(e)
        logs.info("", f"Exception is:\n\t{e}\n", log_file)
        logs.warning("", "Warning ........... some bugs need you to solve!\n", log_file)