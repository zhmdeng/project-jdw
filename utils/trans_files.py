

import shutil
import os
from bases.logs import Logs
from bases.date import Date


class Transfer:

    def move_file(self,files,path,log_file):
        """
        :param log_file: a file path where logs information will be saved
        :param files: file or folder
        :param path: output path where file or folder will be saved
        :return: none
        """
        logs = Logs()
        date = Date()
        date_ = date.today_(0)
        current_time = date.current_time()
        current_time = str(current_time).split(" ")[1].replace(":", "~")
        folder_name = str(date_)

        filelist = os.listdir(path)

        if folder_name in filelist:
            path_way = path + "\\" + folder_name + f"-{current_time}"
            os.makedirs(path_way)
            shutil.move(files, path_way)
        else:
            path_way = path + "\\" + folder_name + f"-{current_time}"
            os.makedirs(path_way)
            shutil.move(files, path_way)

        logs.warning("", f"file move to folder:{path_way} successful!",log_file)

# if __name__ == '__main__':
#     transfer = Transfer()
#     file = r'E:\marketing\2023-04-07'
#     path = r"E:\marketing"
#     transfer.move_file(file,path)