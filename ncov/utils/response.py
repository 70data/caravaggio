# coding=utf-8

import datetime
import json
from django.http import HttpResponse


class my_response(object):
    # 统一封装返回值
    def send(resp):
        response = HttpResponse(
            content=json.dumps(resp),
            content_type='application/json;charset = utf-8',
            status='200',
            reason='success',
            charset='utf-8')
        return response

    # 处理正常请求
    def succeed(self, data):
        resp = {}
        resp['status'] = 0
        resp['desc'] = 'succeed'
        resp['data'] = data
        return my_response.send(resp)

    # 处理异常请求
    def failed(self, msg):
        resp = {}
        resp['status'] = 1
        resp['desc'] = msg
        resp['data'] = []
        return my_response.send(resp)

    # 处理非法请求
    @staticmethod
    def void():
        resp = {}
        resp['status'] = 1
        resp['desc'] = 'request is not void'
        resp['data'] = []
        return my_response.send(resp)
