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
# 写作日期: 2022/10/3 2:32 PM


'''
接收 post 参数

accesstoken String 用户的 accessToken
title String 标题
tab String 目前有 ask share job dev。开发新客户端的同学，请务必将你们的测试帖发在 dev 专区，以免污染日常的版面，否则会进行封号一周处理。
content String 主体内容
'''
import pytest

from common.create_topic_common import createTopic
from common.token_common import getToken
import random


# def test_createTopic():
#     url = 'http://47.100.175.62:3000/api/v1/topics'
#     params = {
#         'accesstoken': getToken(),
#         'title': '精选',
#         'tab': 'ask',
#         'content': 'python'
#     }
#     r = createTopic(url, params)
#     print(r.json())
#     # assert r.status_code == 200
#     # assert r.json()['success'] == True

def test_createTopic_true():
    url = 'http://47.100.175.62:3000/api/v1/topics'
    random_num = random.randint(1, 101)
    token = getToken()
    params = {
        'accesstoken': token,
        'title': f'chenle{random_num}',
        'tab': 'ask',
        'content': 'python'
    }
    # print(f'随机数===={random_num}')
    r = createTopic(url, params, self=None)
    # print(r.json())
    assert r.status_code == 200
    assert r.json()['success'] == True
    assert r.json()['topic_id'] != None
    assert 'topic_id' in r.json()
    assert 'topic_id' in r.text


def test_createTopic_false():
    url = 'http://47.100.175.62:3000/api/v1/topics'
    random_num = random.randint(1, 101)
    token = getToken()
    params = {
        'accesstoken': token,
        'title': f'chenle{random_num}',
        'tab': 'ask',
        'content': 'python'
    }
    # print(f'随机数===={random_num}')
    r = createTopic(url, params, self=None)
    # print(r.json())
    assert r.status_code != 200
    assert r.json()['success'] == False
    assert 'topic_id' not in r.json()
    assert r.json()['error_msg'] == '错误的accessToken'
    assert 'topic_id' not in r.text


@pytest.mark.parametrize()
def test_test_createTopic_requestdata():
    pass

# if __name__ == '__main__':
#     test_createTopic_true(getToken())
#     # test_createTopic_false(getToken=getToken)
