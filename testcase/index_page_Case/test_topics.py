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
# 写作日期: 2022/9/15 1:25 AM

import pytest
import requests
from common.requests_common import RequestsCommon

base_url = "http://47.100.175.62:3000/api/v1"

'''
主题首页接口
接收 get 参数

page Number 页数
tab String 主题分类。目前有 ask share job good
limit Number 每一页的主题数量 最大值为50，超过50按50计算
mdrender String 当为 false 时，不渲染。默认为 true，渲染出现的所有 markdown 格式文本。
'''


# def test_topic_index_page():
#     params = {
#         'page': 1,
#         'tab': 'job',  # 主题分类。目前有 ask share job good
#         'limit': 200,  # 表示显示数据数量
#         'mdrender': "false"
#     }
#     # r = requests.get(url=base_url + "/topics", params=params)
#     r = RequestsCommon.requests(self=None, method='GET', url=base_url + "/topics", params=params)
#     # print(r)
#     # print(r.url)
#     # print(r.json())
#     assert r.status_code == 200
#     assert r.json()['success'] == True
#
#     data = r.json()['data']  # 响应数据中的data字段中的所有数据
#
#     assert params['limit'] == len(data)  # 数据显示数量==响应数据字段data的长度
#
#     # 循环遍历响应字段data中的所有数据，判断所有数据中tab这个字段的值==请求参数tab的值
#     for data in data:
#         assert data['tab'] == params['tab']
#
#     # res = json.loads(r.text)
#     # print(json.dumps(res, indent=4, ensure_ascii=False))


@pytest.mark.parametrize('page,tab,limit,mdrender',
                         [(2, 'ask', 2, 'false'),
                          ('', 'ask', 2, 'false'),
                          (1, 'ask', 0, 'true'),
                          (1, '', '', 'false'),
                          ('', '', '', 'true'),
                          ('', '', '', '')])
def test_topic_index_page_parame(page, tab, limit, mdrender):
    """校验字段边界情况"""
    params = {
        'page': page,
        'tab': tab,  # 主题分类。目前有 ask share job good
        'limit': limit,  # 表示显示数据数量
        'mdrender': mdrender
    }
    r = RequestsCommon.requests(self=None, method='GET', url=base_url + '/topics', params=params)
    assert r.status_code == 200
    assert r.json()['success'] == True

    # data_result = r.json()['data']  # 响应字段data
    #
    # assert params['limit'] == len(data_result)  # 请求参数中的limit字段的数量==响应字段中data里面数据的条数
    #
    # for data_result in data_result:
    #     assert data_result['tab'] == params['tab']

# if __name__ == '__main__':
#     pytest.main(['./test_topics.py::test_topic_index_page_parame'], ['-s'], ['-v'])
