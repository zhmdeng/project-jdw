import pandas as pd

from utils.combine_files import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config


if __name__ == '__main__':
    log_file = 'product_info'
    logs = Logs()
    base = Base()
    date = Date()
    config = Config()
    try:

        final_data = pd.read_excel(r"E:\价格\230222\product_infov1.0.xls")
        print(final_data.columns)

        final_data = final_data[['品牌', '货品ID', '货品编码', '商家编码', '经销出库\n', '分销出库\n', '零售价\nRMB','活动价\nRMB',
       'S大促价\nRMB', '经营成本\n2022.12.31', '货品条形码', '货品名称', '规格',  '类目ID', '类目名称','创建时间', '更新时间']]

        final_data.columns = ['brand','product_id','product_code','outer_code','dealership_price','distributorship_price','retail_price','active_price',
                              'S_price','prime_cost','code','product_name','specs','catagry_id','catagry_name','load_date','update_date']

        values = ['unknow', '000000', '000000', '000000',0.00, 0.00,  0.00, 0.00,
                  0.00,  0.00, 0.00,'000000','unknow', 'unknow','000000','unknow', '0000-00-00 00:00:00','0000-00-00 00:00:00']
        base.fillna_col(final_data, final_data.columns, values, log_file)

        # save to database
        db_info = config.get_parameters('wms')
        con = base.get_connection(db_info)

        # base.save_sql(final_data, "product_info", con, "wms", log_file)
        # logs.info("", "Job run successful ...........\n", log_file)


    except Exception as e:
        print(e)
        logs.info("", f"Exception is:\n\t{e}\n", log_file)
        logs.warning("", "Warning ........... some bugs need you to solve!\n", log_file)