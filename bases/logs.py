"""
log file
"""
import logging
import time
from bases.date import Date

class Logs:

    def log_info(self,msg,level,msg_,log_file_name):

        date = Date()
        current_time = date.current_time()
        msg = f"{current_time}\t{msg} {msg_}"

        logger = logging.getLogger(log_file_name)

        logger.setLevel('DEBUG')

        formatter = logging.Formatter('%(levelname)s-%(name)s-log:%(message)s')

        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)

        now = time.strftime('%Y-%m-%d')  # time format,eg:2021-10-31
        path = 'F:/logs/' + now + '-' + log_file_name + ".log"  # save to local path

        fh = logging.FileHandler(path, encoding='UTF-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

        if level == 'DEBUG':
            logger.debug(msg)
        elif level == 'INFO':
            logger.info(msg)
        elif level == 'WARNING':
            logger.warning(msg)
        elif level == 'ERROR':
            logger.error(msg)
        elif level == 'CRITICAL':
            logger.critical(msg)

        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self, msg, msg_, log_file_name):
        self.log_info(msg, 'DEBUG', msg_, log_file_name)

    def info(self, msg, msg_, log_file_name):
        self.log_info(msg, 'INFO', msg_, log_file_name)

    def warning(self, msg, msg_, log_file_name):
        self.log_info(msg, 'WARNING', msg_, log_file_name)

    def error(self, msg, msg_, log_file_name):
        self.log_info(msg, 'ERROR', msg_, log_file_name)

    def critical(self, msg, msg_, log_file_name):
        self.log_info(msg, 'CRITICAL', msg_, log_file_name)

    def log_func(self,function_name):
        return function_name.__getattribute__('__name__')

    def log_messg(self,function_name):
        date = Date()
        time = date.current_time()
        name = function_name.__getattribute__('__name__')
        print("log:" + " " + f"{time}" + " " + f"{name} run successful!")

# if __name__ == '__main__':
#     logs = Logs()
#     logs.info("","successful","test")