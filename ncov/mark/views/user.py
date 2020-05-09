# coding=utf-8

import json

from utils.response import my_response
from ..models.user import User


def user_register(request):
    # POST /api/mark/user/register
    # 用户注册
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 处理数据
        data, status = User.register(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed([])
            response.set_cookie('token', data)
        elif status == 'existed':
            response = my_response().failed('user is existed.')
        else:
            response = my_response().failed('register failed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def user_update(request):
    # POST /api/mark/user/update
    # 更新用户信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 处理数据
        data, status = User.update(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed([])
        else:
            response = my_response().failed('update user failed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def user_info(request):
    # POST /api/mark/user/info
    # 获取用户信息
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 处理数据
        data = User.info_by_phone(request_data)
        # 拼接返回值
        if len(data) != 0:
            response = my_response().succeed(data)
        else:
            response = my_response().failed('user is not existed.')
    # 非法请求
    else:
        response = my_response().void()
    return response


def user_login(request):
    # POST /api/mark/user/login
    # 用户登陆
    if request.method == 'POST':
        # 解析body数据
        request_data = json.loads(request.body)
        # 处理数据
        data, status = User.login(request_data)
        # 拼接返回值
        if status == 'succeed':
            response = my_response().succeed(data)
            response.set_cookie('token', data[0]['token'])
            if data[0]['admin'] == 1:
                response.set_cookie('admin', True)
        elif status == 'failed':
            response = my_response().failed('login failed.')
        else:
            response = my_response().failed('user is not existed.')
    # 非法请求
    else:
        response = my_response().void()
    return response
