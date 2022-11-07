# -*- coding: utf-8 -*-

# 用例  ID: 
# 用例标题: 
# 预置条件:
# 测试步骤:
#   1.调用接口：sigin,传入账号，密码，请求url，header发起post请求
# 预期结果:
#   1.登录成功，返回当前账户信息l
# 写作日期: 2022/10/14 11:48 PM

import logging
import os

logger = logging.getLogger('qx_web_api')

logger.setLevel(logging.DEBUG)
formatter_str = '[%(asctime)s] [%(filename)s] [line:%(lineno)d] [%(levelname)s] : [%(message)s]'
formatter_end = logging.Formatter(formatter_str)

sh = logging.StreamHandler()
sh.setFormatter(formatter_end)
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)

log_dir = os.path.join(os.path.dirname(__file__), '../logs')
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_path = os.path.join(log_dir, 'testlog.log')

fh = logging.FileHandler(log_path, mode='a', encoding='utf-8')
fh.setFormatter(formatter_end)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

if __name__ == '__main__':
    logger.info('你好啊')
