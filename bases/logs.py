"""
log file
"""
import logging
import colorlog
import time

from colorlog.formatter import default_formats

from bases.date import Date

class Logs:

    def log_info(self,msg,level,msg_,log_file_name):

        date = Date()
        current_time = date.current_time()
        msg = f"{current_time}\t{msg} {msg_}"

        logger = logging.getLogger(log_file_name)

        logger.setLevel('DEBUG')

        log_colors_config = {
            'DEBUG': 'white',
            'INFO': 'green,bold',
            'WARNING': 'yellow,bold',
            'ERROR': 'cyan,bold',
            'CRITICAL': 'purple',
        }

        file_formatter = logging.Formatter(fmt='%(levelname)s-%(name)s-log:%(message)s')

        console_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s%(levelname)s-%(name)s-log:%(message)s',
            log_colors=log_colors_config)

        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(console_formatter)

        now = time.strftime('%Y-%m-%d')  # time format:2021-10-31
        path = 'F:/logs/' + now + '-' + log_file_name + ".log"  # save to local path

        fh = logging.FileHandler(path, encoding='UTF-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(file_formatter)

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

        if not logger.handlers:
            logger.addHandler(ch)
            logger.addHandler(fh)

        logger.removeHandler(ch)
        logger.removeHandler(fh)

        ch.close()
        fh.close()

    def debug(self, msg, msg_, log_file_name):
        self.log_info(msg, 'DEBUG', msg_, log_file_name)

    def info(self, msg, msg_, log_file_name):
        self.log_info(msg_, 'INFO', msg, log_file_name)

    def warning(self, msg, msg_, log_file_name):
        self.log_info(msg_, 'WARNING', msg, log_file_name)

    def error(self, msg, msg_, log_file_name):
        self.log_info(msg_, 'ERROR', msg, log_file_name)

    def critical(self, msg, msg_, log_file_name):
        self.log_info(msg, 'CRITICAL', msg_, log_file_name)

    def log_func(self,function_name):
        return function_name.__getattribute__('__name__')

    def log_messg(self,function_name):
        date = Date()
        time = date.current_time()
        name = function_name.__getattribute__('__name__')
        print("log:" + " " + f"{time}" + " " + f"{name} run successful!")















# import logging
# import colorlog
#
#
# log_colors_config = {
#     'DEBUG': 'white',  # cyan white
#     'INFO': 'green',
#     'WARNING': 'yellow',
#     'ERROR': 'red',
#     'CRITICAL': 'bold_red',
# }
#
#
# logger = logging.getLogger('logger_name')
#
# # 输出到控制台
# console_handler = logging.StreamHandler()
# # 输出到文件
# file_handler = logging.FileHandler(filename='test.log', mode='a', encoding='utf8')
#
# # 日志级别，logger 和 handler以最高级别为准，不同handler之间可以不一样，不相互影响
# logger.setLevel(logging.DEBUG)
# console_handler.setLevel(logging.DEBUG)
# file_handler.setLevel(logging.INFO)
#
# # 日志输出格式
# file_formatter = logging.Formatter(
#     fmt='[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
#     datefmt='%Y-%m-%d  %H:%M:%S'
# )
# console_formatter = colorlog.ColoredFormatter(
#     fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
#     datefmt='%Y-%m-%d  %H:%M:%S',
#     log_colors=log_colors_config
# )
# console_handler.setFormatter(console_formatter)
# file_handler.setFormatter(file_formatter)
#
# # 重复日志问题：
# # 1、防止多次addHandler；
# # 2、loggername 保证每次添加的时候不一样；
# # 3、显示完log之后调用removeHandler
# if not logger.handlers:
#     logger.addHandler(console_handler)
#     logger.addHandler(file_handler)
#
# console_handler.close()
# file_handler.close()




# if __name__ == '__main__':
#     # logger.debug('debug')
#     # logger.info('info')
#     # logger.warning('warning')
#     # logger.error('error')
#     # logger.critical('qqqqqqqqqq')
#
#
#
#
#     logs = Logs()
#     logs.info("","successful","test")