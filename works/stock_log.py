
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
    log_file = "stock_log"
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    try:
        # read path
        path = r"E:\unit"
        # output file name
        final_name = "stock_log"
        # output path
        path_ = r"E:\orders\combine"

        # end_time = datetime.date(2023 ,1 ,1)
        # end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
        # # end_time = end_time.strptime("%Y-%m-%d %H:%M:%S")


        combine = Combine()
        final_data = combine.get_all_files(path ,log_file)
        logs.info("", f"files combine successful ....·.......", log_file)
        print(final_data.columns)

        # # data cleaning
        final_data = final_data[['单号', 'LP单号', '货品编码', '货品名称', '仓库名称', '出入库时间', '单据类型', '库存类型',
                                '出入数量','结存数量', 'ERP订单号', '外部流水号']]
        #
        final_data.columns = ['code', 'LP_code', 'outer_code', 'product_name', 'store_name', 'time', 'type', 'stock_type',
                              'num', 'surplus_num', 'erp_code', 'tid']

        values = ['unknow','unknow','unknow','unknow','unknow','0000-00-00 00:00:00','unknow','unknow',
                  0,-10000,'unknow',000000]
        base.fillna_col(final_data,final_data.columns,values,log_file)

        # save to csv
        time = str(max(final_data['time'])).split(" ")[0]
        final_data.to_csv(path_ + "/" + final_name + f"{time}" + ".csv", index=False)
        logs.info("", "data load to excel successful ...........", log_file)

        # save to database
        db_info = config.get_parameters('wms')
        con = base.get_connection(db_info)

        # base.save_sql(final_data, "stocks", con, "wms", log_file)
        logs.info("", "******Job run successful ...........\n", log_file)


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
