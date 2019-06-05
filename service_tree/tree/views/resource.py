# coding=utf-8

import json
from utils.response import MyResponse
from ..models.resource import Resource

def tree_resource(request):
    # 增加
    # POST /tree/tree_resource/ 增加资源
    if request.method == 'POST':
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = Resource().addResource(requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 非法请求
    else:
        response = MyResponse().void()
    return response

def tree_resource_id(request, resource_id):
    # 查看
    # GET /tree/tree_resource/resource_id 查看资源
    if request.method == 'GET':
        # 处理数据
        data = Resource().getResource(resource_id)
        # 拼接返回值
        response = MyResponse().succeed(data)
    # 修改
    # PUT /tree/tree_resource/resource_id 修改资源
    elif request.method == 'PUT':
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        # 修改节点信息
        dbStatus = Resource().updateResource(resource_id, requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 删除
    # DELETE /tree/tree_resource/resource_id 删除资源
    elif request.method == 'DELETE':
        # 处理数据
        dbStatus = Resource().deleteResource(resource_id)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 非法请求
    else:
        response = MyResponse().void()
    return response

def tree_resource_list(request, asset_id):
    # 查看
    # GET resource/list/asset_id 基于asset_id查看资源
    if request.method == 'GET':
        # 处理数据
        data = Resource().getResourceByAssetid(asset_id)
        # 拼接返回值
        response = MyResponse().succeed(data)
    # 非法请求
    else:
        response = MyResponse().void()
    return response
