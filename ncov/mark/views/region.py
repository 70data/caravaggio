# coding=utf-8

import json

from utils.response import my_response
from ..models.region import Region


def region_insert(request):
    # POST /api/mark/region/insert
    # 添加子地区
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 处理数据
        data, status = Region.insert(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed([])
        else:
            response = my_response().failed('add region failed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def region_next(request):
    # POST /api/mark/info/getNextLoc
    # 获取下级地区
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 处理数据
        data, status = Region.get_next(request_data)
        # 拼接返回值
        response = my_response().succeed(data)
    # 非法请求
    else:
        response = my_response().void()
    return response
