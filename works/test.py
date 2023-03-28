


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
    log_file = "test"
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
        logs.info("", "begin ...........", log_file)
        # data source
        db_info = config.get_parameters('wms')
        stock = f"select * from wms.stocks where  tid != 0"
        stock = base.read_data(stock,db_info)
        # for i in range(len(stock)):
        #     if stock['outer_code'][i].startswith('zip'):

        stock = stock.loc[stock['outer_code'].startswith('zip')]
        columns = ['tid']
        new_type = ['str']
        # base.retype(stock, columns, new_type,log_file)
        # for i in range(len(stock)):
        #     stock['tid'][i] = stock['tid'][i].strip()

        # stock['tid'] = stock['tid'].astype(str)
        stock.to_excel(r'C:\Users\Administrator\Desktop\test\stock.xlsx',index=False)
        # print(stock['tid'].head(5))
        # print(type(stock['tid'][1]))
        order = f'select * from wms.orders where title = "Zipfizz"'
        order = base.read_data(order, db_info)
        # for i in range(len(order)):
        #     order['tid'][i] = order['tid'][i].strip()
        # base.retype(order, columns, new_type, log_file)
        # order['tid'] = order['tid'].astype('str')
        order.to_excel(r'C:\Users\Administrator\Desktop\test\order.xlsx',index=False)
        combine = pd.merge(stock,order,on='tid',how='inner')
        combine.to_excel(r'C:\Users\Administrator\Desktop\test\d.xlsx', index=False)

        #
        # print(combine.head(5))
        # print(len(combine))
        logs.info("", "end ...........", log_file)

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
