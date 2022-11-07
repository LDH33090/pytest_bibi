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
# 写作日期: 2022/10/16 12:58 AM
import logging
import os

# 设定日志名称
logger = logging.getLogger('pytest_logs')
# 设定日志等级
logger.setLevel(logging.DEBUG)

# 设定日志输出内容的显示格式
# '[%(asctime)s] [%(filename)s] [line: %(lineno)d] [%(levelname)s] : [%(message)s]'
formatter_str = f'[%(asctime)s] [%(filename)s] [line: %(lineno)d] [%(levelname)s] : [%(message)s]'
formatter = logging.Formatter(formatter_str)

# 1. 设置日志 往控制台输出
sh = logging.StreamHandler()
# 设置日志 往控制台输出的格式化后的内容
sh.setFormatter(formatter)
# 设置日志 在控制台显示的日志等级
sh.setLevel(logging.DEBUG)
# 添加日志到处理器
logger.addHandler(sh)

# 2. 设置日志 往指定目录下到文件输出
# 设定目录位置
logs = os.path.join(os.path.dirname(__file__), '../logs')
# 如果目录不存在就先创建
if not os.path.exists(logs):
    os.mkdir(logs)

# 设定日志内容打印到某个文件
logfile = os.path.join(logs, 'qx.log')

# 设定 日志输出到某个文件的方法
fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
# 设定日志 往文件输出内容，需要进行格式化后
fh.setFormatter(formatter)
# 设定日志 往文件输出日志的等级
fh.setLevel(logging.DEBUG)
# 把日志文件流添加到处理器
logger.addHandler(fh)

if __name__ == '__main__':
    logger.info('this is test_pytest')
