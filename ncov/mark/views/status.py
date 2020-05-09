# coding=utf-8

from utils.response import my_response


def status(request):
    data = {}
    # 拼接返回值
    response = my_response().succeed(data)
    return response
