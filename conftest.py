# # -*- coding: utf-8 -*-
#
# # 用例  ID:
# # 用例标题:
# # 预置条件:
# # 测试步骤:
# #   1.调用接口：sigin,传入账号，密码，请求url，header发起post请求
# # 预期结果:
# #   1.登录成功，返回当前账户信息
# #   2.检查响应码为：200，各字段正确
# # 脚本作者: 林德浩
# # 写作日期: 2022/9/14 5:33 PM
# import json
#
# import pytest
# import requests
# import json
#
# """http://47.100.175.62:3000/api/v1/topics"""
#
#
# def test_topics():
#     url = 'http://47.100.175.62:3000/api/v1/topics'
#     params = {
#         'page': 1,
#         'tab': '',
#         'limit': 50,
#         'mdrender': False
#     }
#     r = requests.get(url=url, params=params)
#     print(r)
#     print(r.url)
#     print(r.json())
#     assert r.status_code == 200
#     assert r.json()['success'] == True
#
#     # res = json.loads(r.text)
#     # print(json.dumps(res, indent=4, ensure_ascii=False))
#
#
# test_topics()
#
#
# def test_addTopic():
#     url = 'http://47.100.175.62:3000/api/v1/topics'
#     params = {
#         'accesstoken': '9806e7cb-beb0-45ed-aab6-2a84ec903ec5',
#         'title ': 'pytest',
#         'tab': 'ask',  # 目前有 ask share job dev
#         'content': 'pytest学习'
#     }
#
#     req = requests.post(url=url, data=params)
#     print(req.json())
#
#
# # test_addTopic()
