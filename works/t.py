import pandas as pd
import datetime
import sys
import os

from utils.combine import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config

logs = Logs()
base = Base()
date = Date()
config = Config()
combine = Combine()
log_file = 't'
path = r'E:\tmall sku'
final_data = combine.get_all_files(path, log_file)

data = pd.read_excel(r"D:\git\20230215165129.xlsx")
data = data.loc[data['单据类型'].isin(['交易出库','集货调拨入库'])]
data = data['货品编码','外部流水号']
final_data = pd.merge(final_data,data,left_on='子订单编号',right_on='外部流水号',how='left')

print(len(final_data))

logs.info("", "order ...........", log_file)