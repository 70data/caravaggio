# coding=utf-8

import json

from utils.response import my_response
from ..models.sample import Sample


def sample_insert(request):
    # POST /api/mark/sample/insert
    # 添加病例信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 获取 token
        token = request.COOKIES['token']
        request_data['token'] = token
        # 处理数据
        data, status = Sample.insert(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed([])
        else:
            response = my_response().failed('add sample failed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def sample_update(request):
    # POST /api/mark/sample/update
    # 更新病例信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 获取 token
        token = request.COOKIES['token']
        request_data['token'] = token
        # 处理数据
        data, status = Sample.update(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed([])
        elif status == 'permission':
            response = my_response().failed('user has no permission.')
        else:
            response = my_response().failed('update sample failed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def sample_delete(request):
    # POST /api/mark/sample/delete
    # 删除病例信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 获取 token
        token = request.COOKIES['token']
        request_data['token'] = token
        # 处理数据
        data, status = Sample.delete(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed([])
        elif status == 'permission':
            response = my_response().failed('user has no permission.')
        else:
            response = my_response().failed('delete sample failed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def sample_info(request):
    # POST /api/mark/info/getPat
    # 获取病例信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 获取 token
        token = request.COOKIES['token']
        request_data['token'] = token
        # 处理数据
        data, status = Sample.info_all(request_data)
        # 拼接返回值
        if status == 'void':
            response = my_response().failed('region void.')
        else:
            response = my_response().succeed(data)
    # 非法请求
    else:
        response = my_response().void()
    return response
