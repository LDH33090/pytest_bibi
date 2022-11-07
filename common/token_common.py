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
# 写作日期: 2022/10/2 6:59 PM

import pytest
import requests
import random


# @pytest.fixture(scope='session', autouse=True)
# def getToken():
#     token = "f37c6b2b-fdd7-445d-8a9e-a69e354e7b2d"
#     return token

def getToken():
    token = "f37c6b2b-fdd7-445d-8a9e-a69e354e7b2d"
    return token


# def test_createTopic(getToken):
#     # random_num = random.randint(1, 100)
#     #
#     # base_url = 'http://47.100.175.62:3000/api/v1/topics'
#     # body = {
#     #     "accesstoken": getToken,
#     #     "title": f'chenle{random_num}',
#     #     "tab": "ask",
#     #     "content": "python"
#     # }
#     #
#     # print(random_num)
#     # r = requests.post(url=base_url, data=body)
#     # print(r.json())
#     # return r
#     print("----------------", getToken)

#
# if __name__ == '__main__':
#     test_createTopic(getToken=getToken)
