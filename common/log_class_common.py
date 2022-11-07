# -*- coding: utf-8 -*-

# 用例  ID: 
# 用例标题: 
# 预置条件:
# 测试步骤:
#   1.调用接口：sigin,传入账号，密码，请求url，header发起post请求
# 预期结果:
#   1.登录成功，返回当前账户信息
#   2.检查响应码为：200，各字段正确
# 脚本作者: 林德浩
# 写作日期: 2022/10/17 11:20 PM
import os
import logging

'''
      %(levelno)s: 打印日志级别的数值
      %(levelname)s: 打印日志级别名称
      %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
      %(filename)s: 打印当前执行程序名
      %(funcName)s: 打印日志的当前函数
      %(lineno)d: 打印日志的当前行号
      %(asctime)s: 打印日志的时间
      %(thread)d: 打印线程ID
      %(threadName)s: 打印线程名称
      %(process)d: 打印进程ID
      %(message)s: 打印日志信息
      '''


class Log:

    def __init__(self):
        # 定义日志存储路径
        self.log_dir = os.path.join(os.path.dirname(__file__), '../logs')
        self.log_fath = os.path.join(self.log_dir, 'bill.log')

        self.format_str = f'[%(asctime)s] [%(process)d] [%(pathname)s] [%(levelname)s]: [%(message)s]'
        self.format_end = logging.Formatter(self.format_str)
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)

        self.set_file_logger()
        self.set_console_logger()

    def set_console_logger(self):
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(self.format_end)
        self._logger.addHandler(consoleHandler)

    def set_file_logger(self):
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)
        fileHandler = logging.FileHandler(self.log_fath, mode='a', encoding='utf-8')
        fileHandler.setFormatter(self.format_end)
        self._logger.addHandler(fileHandler)

    def get_logger(self):
        return self._logger


# if __name__ == '__main__':
#     log = Log().get_logger()
#     log.info('nihao')
