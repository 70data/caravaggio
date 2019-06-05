# coding=utf-8

import json
from django.http import HttpResponse

class MyResponse(object):

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
        resp['code'] = 0
        resp['message'] = 'succeed'
        resp['data'] = data
        return MyResponse.send(resp)

    # 处理正常请求
    def failed(self, msg):
        resp = {}
        resp['code'] = 1
        resp['message'] = msg
        resp['data'] = {}
        return MyResponse.send(resp)

    # 处理非法请求
    @staticmethod
    def void():
        resp = {}
        resp['code'] = 1
        resp['message'] = 'request is not void'
        resp['data'] = {}
        return MyResponse.send(resp)
