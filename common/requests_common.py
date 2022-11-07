# -*- coding: utf-8 -*-

# 用例  ID: 
# 用例标题: 
# 预置条件:
# 测试步骤:
#   1.调用封装好的日志模块 2.实现接口请求日志输出效果
# 预期结果:
#   1.日志格式化内容显示正确
# 脚本作者: 林德浩
# 写作日期: 2022/10/16 11:51 AM

import requests
from common.log_common02 import LogCommon

"""
自定义发送请求
       请求方法为字符串格式，params、data、json数据可以为空
       method：请求方法
       url：请求URL
       params：get请求的参数
       data：body中的数据
       json：body中json格式的数据
       kwargs：其它字典参数，允许传入不定长的参数
 """


class RequestsCommon:
    def requests(self, method: str, url, params=None, data=None, json=None, **kwargs):
        method_list = ['GET', 'POST', 'DELETE', 'PUT', 'options', 'PATCH', 'HEAD', ]
        method = method.upper()
        # get(url, params=None, **kwargs):
        if method == 'GET':
            res = requests.get(url=url, params=params, **kwargs)
            if json:
                LogCommon.logMessage(f'请求方法:{method},请求url:{url},请求参数:{json},响应结果:{res.text}')
            elif params:
                LogCommon.logMessage(f'请求方法:{method},请求url:{url},请求参数:{params},响应结果:{res.text}')
            elif not json and not params:
                LogCommon.logMessage(
                    f'请求方法:{method},请求url:{url},请求参数:{res.url.split("?")[-1]},响应结果:{res.text}')
            return res
        # post(url, data=None, json=None, **kwargs):
        if method == 'POST':
            if data:
                res = requests.post(url=url, data=data, **kwargs)
                LogCommon.logMessage(f'请求方法:{method},请求url:{url},请求参数:{data},响应结果:{res.text}')
            elif json:
                res = requests.post(url=url, data=json, **kwargs)
                LogCommon.logMessage(f'请求方法:{method},请求url:{url},请求参数:{json},响应结果:{res.text}')
            return res
        # delete(url, **kwargs):
        if method == 'DELETE':
            res = requests.delete(url=url)
            LogCommon.logMessage(f'请求方法:{method},请求url:{url},请求参数:{res.request},响应结果:{res.text}')
            return res

        # put(url, data=None, **kwargs)
        if method == 'PUT':
            res = requests.put(url=url, data=data, **kwargs)
            LogCommon.logMessage(f'请求方法:{method},请求url:{url},请求参数:{data},响应结果:{res.text}')
            return res

        else:
            try:
                LogCommon.logMessage(f'请求方法未定义，请检查代码')
            except:
                LogCommon.logMessage(Exception)
            finally:
                LogCommon.logMessage(f'请求方法不包含在此请求方法{method_list}列表元素之内')
