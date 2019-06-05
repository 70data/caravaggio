# coding=utf-8

from utils.response import MyResponse

def status(request):
    data = {}
    # 拼接返回值
    response = MyResponse().succeed(data)
    return response
