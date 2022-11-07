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
# 写作日期: 2022/9/28 1:25 AM

'''
accesstoken String 用户的 accessToken
title String 标题
tab String 目前有 ask share job dev。开发新客户端的同学，请务必将你们的测试帖发在 dev 专区，以免污染日常的版面，否则会进行封号一周处理。
content String 主体内容
'''
import json

import requests
import random
from common.requests_common import RequestsCommon
from common.token_common import getToken

"""新建主题"""


def createTopic(url, request_body,self):
    random_num = random.randint(1, 100)

    # base_url = 'http://47.100.175.62:3000/api/v1/topics'
    # body = {
    #     "accesstoken": token_all.getToken(),
    #     "title": f'chenle{random_num}',
    #     "tab": "ask",
    #     "content": "python"
    # }
    r = RequestsCommon.requests(self, method='POST', url=url, data=request_body)
    # print(r.text)
    # print(r.json())
    return r


# if __name__ == '__main__':
#     base_url = 'http://47.100.175.62:3000/api/v1/topics'
#     random_num = random.randint(1, 100)
#     body = {
#         "accesstoken": getToken(),
#         "title": f'chenle{random_num}',
#         "tab": "ask",
#         "content": "python"
#     }
#     createTopic(base_url, body,self=None)
