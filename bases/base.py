import pandas as pd
from sqlalchemy import create_engine
from bases.logs import Logs

class Base:

    def get_connection(self,db_info):
        # db_info paramter detail info:
        # db_info = {
        #     'username':'root',
        #     'password':'123456',
        #     'port':3306,
        #     'server':'localhost',
        #     'database':'wms'
        # }
        engine = create_engine(
            "mysql+pymysql://{}:{}@{}:{}/{}".format(db_info['username'], db_info['password'], db_info['server'],
                                                          db_info['port'], db_info['database']))
        connection = engine.connect()
        return connection

    def read_data(self,query,db_info):
        con = self.get_connection(db_info)
        data = pd.read_sql("{}".format(query),con)
        return data

    def excute_sql(self,query,db_info):
        engine = create_engine(
            "mysql+pymysql://{}:{}@{}:{}/{}".format(db_info['username'], db_info['password'], db_info['server'],
                                                    db_info['port'], db_info['database']))
        with engine.begin() as conn:
            conn.execute(query)


    def save_sql(self,data,table,con,schema,log_file,chunksize=1000,if_exists="append"):
        log = Logs()
        data.to_sql(name=table,con=con,schema=schema,chunksize=chunksize,if_exists=if_exists,index=False)
        log.info("","data load to database successful!",log_file)

    def retype(self,data,col_name,new_type,log_file):
        logs = Logs()
        for i in range(len(col_name)):
            origion_type = type(data[f'{col_name[i]}'][0])
            data[f'{col_name[i]}'] = data[f'{col_name[i]}'].astype(f'{new_type[i]}')
            logs.info("", f"{col_name[i]}:{origion_type}--->{new_type[i]}", log_file)
        # data[f'{col_name}'] = data[f'{col_name}'].astype(f'{new_type}')

    def fillna_col(self,data,col_name:list,value:list,log_file):
        logs = Logs()
        for i in range(len(col_name)):
            data[f'{col_name[i]}'] = data[f'{col_name[i]}'].fillna(value=f'{value[i]}')
            logs.info("", f"{col_name[i]} --->{value[i]}", log_file)


# if __name__ == '__main__':
#     base = Base()
#     db_info = {
#         'username':'root',
#         'password':'123456',
#         'port':3306,
#         'server':'localhost',
#         'database':'wms'
#     }
#     base.get_connection(db_info)