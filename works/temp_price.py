


import datetime
import sys
import os

import pandas as pd

from utils.combine import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config

if __name__ == '__main__':
    log_file = "test"
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    try:

        # price
        # data = pd.read_excel(r"E:\价格\价格2301.xls")
        #
        # data.columns = ['product_id', 'product_name', 'prime_cost']
        #
        # print(data)
        #
        # print(data.columns)
        #
        # # save to database
        db_info = config.get_parameters('wms')
        con = base.get_connection(db_info)

        # save price tabel
        # base.save_sql(data, "price", con, "wms", log_file)
        # logs.info("", "Job run successful ...........\n", log_file)

        # price_info
        final_data = pd.read_excel(r"E:\价格\price\230222.xls")
        print(len(final_data))

        final_data = final_data.drop_duplicates(['product_code', 'outer_code', 'product_name', 'active_price','retail_price',
        'S_price', 'dealership_price', 'distributorship_price','prime_cost'])

        values = ['unknow','000000', '000000', 'unknow',0.00, 0.00,  0.00, 0.00,0.00,  0.00]
        base.fillna_col(final_data, final_data.columns, values, log_file)
        print(len(final_data))

        #save price_info tabel
        # base.save_sql(final_data, "price_info", con, "wms", log_file)
        # logs.info("", "Job run successful ...........\n", log_file)

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
