"""
combine excel or .csv format files from folders
"""


from bases.logs import Logs
import pandas as pd
import os
import chardet

class Combine:

    def get_encoding(self,file):
        with open(file,'rb') as f:

            return chardet.detect(f.read(5))['encoding']

    def get_files_data(self,path,log_file):

        final_data = pd.DataFrame()
        # global final_data
        logs = Logs()
        files = os.listdir(path)

        num = 0
        for file in files:
            if os.path.isfile(path + "/" +file):
                filename,extension=os.path.splitext(file)
                # 判断文件类别
                if extension == ".txt" :
                    logs.info("",f"waiting for reading contents of {filename} ...........",f"{log_file}")
                    data = pd.read_table(path+'/' +file)
                    final_data = final_data.append(data,ignore_index=True)
                    logs.info("",f"\n{data.head(1)}",log_file)
                elif extension=='.xlsx':
                    logs.info("",f"waiting for reading contents of {filename} ...........",f"{log_file}")
                    data = pd.read_excel(path+'/' +file)
                    final_data = final_data.append(data,ignore_index=True)
                    logs.info("",f"\n{data.head(1)}",log_file)
                elif extension=='.xls':
                    logs.info("",f"waiting for reading contents of {filename} ...........",f"{log_file}")
                    data = pd.read_excel(path+'/' +file,index_col=None)
                    final_data = final_data.append(data,ignore_index=True)
                    logs.info("",f"\n{data.head(1)}",log_file)
                elif extension=='.csv':
                    logs.info("",f"waiting for reading contents of {filename} ...........",f"{log_file}")
                    current_file = path + '/' + file
                    print('current file encoding:',self.get_encoding(current_file))
                    # data = pd.read_csv(path + '/' + file, index_col=None, encoding='GB18030')

                    # data = pd.read_csv(path + '/' + file, index_col=None,encoding=self.get_encoding(current_file))

                    # if self.get_encoding(current_file) == 'GB18030':
                    #     data = pd.read_csv(path + '/' + file, index_col=None,encoding='GB18030')
                    if self.get_encoding(current_file) == 'ISO-8859-1':
                        data = pd.read_csv(path + '/' + file, index_col=None, encoding='GB18030')
                    else:
                        data = pd.read_csv(path + '/' + file, index_col=None, encoding='utf-8')
                    final_data = final_data.append(data,ignore_index=True)
                    logs.info("",f"\n{data.head(1)}",log_file)
            # 判断是不是文件夹
            elif os.path.isdir(path+'/'+file):
                self.get_files_data(path + '/' + file,f"{log_file}")
            num = num +1
            logs.info("", f"total files number: {num} ...........", f"{log_file}")

        return final_data

    def get_all_files(self,path,log_file):

        logs = Logs()
        folders = os.listdir(path)
        print(path)
        path_folder = str(path).split("\\")[1]
        print(folders)
        final_data = pd.DataFrame()

        for folder in folders:
            if os.path.isdir(path + '/' + folder) is True:
                logs.info("", f"current folder is:\t{path_folder}\\{folder}", f"{log_file}")
                data = self.get_files_data(path +'\\'+ folder,f"{log_file}")
            else:
                data = self.get_files_data(path,f"{log_file}")
            data['title'] = str(folder)
            final_data = final_data.append(data)

        logs.info("", f"run successful ...........", f"{log_file}")
        return final_data






