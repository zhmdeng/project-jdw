import os
from bases.logs import Logs


class Generate:

    def generate_folder(self, path, log_file):
        """
        :param path: place where want to generate a new folder
        :param log_file: log filename
        :return: generate a new folder or raise an error information
        """

        folder = os.path.exists(path)
        logs = Logs()
        if not folder:
            os.makedirs(path)
            logs.info("", f"There added a new folder:{path}!", log_file)
        else:
            logs.warning("", "There exists this folder! Please use other folder name,and try again", log_file)

# if __name__ == '__main__':
#     logs = Logs()
#     path = r"E:\youz\私域2"
#     log_file = 'generate'
#     created = Generate()
#     created.generate_folder(path,log_file)
#     logs.info("", "There added a new folder here too!", log_file)
