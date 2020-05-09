# coding=utf-8

import json

from utils.response import my_response
from ..models.count import Count


def count_insert(request):
    # POST /api/mark/count/insert
    # 添加统计信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 获取 token
        token = request.COOKIES['token']
        request_data['token'] = token
        # 处理数据
        data, status = Count.insert(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed([])
        elif status == 'existed':
            response = my_response().failed('region data in this time is existed.')
        else:
            response = my_response().failed('add count failed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def count_update(request):
    # POST /api/mark/count/update
    # 更新统计信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 获取 token
        token = request.COOKIES['token']
        request_data['token'] = token
        # 处理数据
        data, status = Count.update(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed([])
        elif status == 'permission':
            response = my_response().failed('user has no permission.')
        else:
            response = my_response().failed('update count failed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def count_delete(request):
    # POST /api/mark/count/delete
    # 删除统计信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 获取 token
        token = request.COOKIES['token']
        request_data['token'] = token
        # 处理数据
        data, status = Count.delete(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed([])
        elif status == 'permission':
            response = my_response().failed('user has no permission.')
        else:
            response = my_response().failed('delete count failed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def count_info(request):
    # POST /api/mark/info/getCount
    # 获取统计信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 获取 token
        token = request.COOKIES['token']
        request_data['token'] = token
        # 处理数据
        data, status = Count.info_all(request_data)
        # 拼接返回值
        if status == 'void':
            response = my_response().failed('region void.')
        else:
            response = my_response().succeed(data)
    # 非法请求
    else:
        response = my_response().void()
    return response
