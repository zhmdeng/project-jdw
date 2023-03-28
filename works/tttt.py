import pandas as pd
import datetime
import sys
import os

from utils.combine_files import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config

logs = Logs()
base = Base()
date = Date()
config = Config()
combine = Combine()
log_file = 'tttt'
# path = r'E:\orders\history orders\doctors best orders'
# final_data = combine.get_all_files(path, log_file)
# for i in range(len(final_data)):
#     final_data['订单编号'][i] = 'L' + str(final_data['订单编号'][i])
# # for col in ["子订单编号", "主订单编号", "支付单号"]:
# #     final_data[f"{col}"] = final_data[f"{col}"].str.extract(r'(\d+)', expand=True)
# print(final_data.head(5))
# path = r'E:\unit'
# stock = combine.get_all_files(path, log_file)
# for i in range(len(final_data)):
#     stock['外部流水号'][i] = 'L' + str(stock['外部流水号'][i])
# print(stock.head(5))
# data =pd.merge(final_data,stock,left_on='订单编号',right_on='外部流水号',how='inner')
# print(len(data))


# db_info = config.get_parameters('wms')
# logs.info("", "begin ...........", log_file)
# order = f"select * from wms.orders"
# order = base.read_data(order, db_info)
# logs.info("", "order ...........", log_file)
# sku = f"select * from wms.order_skus"
# logs.info("", "begin ...........", log_file)
# sku = base.read_data(sku, db_info)
# order_sku = pd.merge(order,sku,left_on='tid',right_on='order_id',how='right')
# order_sku.to_csv(r'C:\Users\Administrator\Desktop\test\dd.csv', index=False)
# print(len(order_sku))
# logs.info("", "order ...........", log_file)

# a = [1,2,3,4]
# for i in a:
#     print(i)
#     if i == 3:
#         i=2
# print(a)


d_path = r"E:\douy sku"
douy = pd.read_csv(r"E:\douy sku\Doctor's Best\1678339072_3c89c52343427c0433464ab44af5938dBuiaMkIP.csv",dtype={'商品ID':'str','货品ID':'str'})
logs.info("", f"douy files combine successful ...........", log_file)

douy = douy[['商品ID', '货品ID', '商家编码']]
douy = douy.drop_duplicates(['商品ID', '货品ID', '商家编码'])
print(douy)
douy = douy.reset_index(drop=True)
douy['商品ID'] = douy['商品ID'].astype(str)
douy['货品ID'] = douy['货品ID'].astype(str)
for i in range(len(douy)):
    douy['商家编码'][i] = str(douy['商家编码'][i]).strip()
    douy['商品ID'][i] = str(douy['商品ID'][i])
    douy['货品ID'][i] = str(douy['货品ID'][i])
code = f"""
        select * from wms.price_info
"""
db_info = config.get_parameters('wms')
code = base.read_data(code, db_info)
code = code[['product_code','fixed_code']]

print(douy)


douy = pd.merge(douy,code,left_on='商家编码',right_on='product_code',how='left')
douy.to_csv(r'C:\Users\Administrator\Desktop\douy0316.csv')

data_ = pd.read_excel(r"C:\Users\Administrator\Desktop\全量商品列表2023-03-01_2023-03-09_数据更新日期2023-03-09(1).xlsx",sheet_name='商品',dtype={'new_商品ID':'str','货品ID':'str'})
data = pd.read_excel(r"C:\Users\Administrator\Desktop\抖店2023-03-01~03-13源数据 - 副本.xlsx",sheet_name='源数据节选',dtype={'商品编号':'str'})
data = pd.merge(data_,data,left_on='new_商品ID',right_on='商品编号',how='right')
print(data.columns)
data = data[['new_商品ID', '货品ID', '商家编码','fixed_code','商品标题', '商品编号','成交金额\n（剔除退款）', '成交件数\n（剔除退款）']]
data.to_excel(r'C:\Users\Administrator\Desktop\data.xls')





