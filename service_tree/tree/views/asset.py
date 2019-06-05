# coding=utf-8

import json
from utils.response import MyResponse
from ..models.asset import Asset

def tree_asset(request):
    # 增加
    # POST /tree/asset/ 增加资产
    if request.method == 'POST':
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = Asset().addAsset(requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 非法请求
    else:
        response = MyResponse().void()
    return response

def tree_asset_id(request, asset_id):
    # 查看
    # GET /tree/asset/asset_id 基于asset_id查看资产信息
    if request.method == 'GET':
        # 处理数据
        data = Asset().getAsset(asset_id)
        # 拼接返回值
        response = MyResponse().succeed(data)
    # 修改
    # PUT /tree/asset/asset_id 修改资产信息
    elif request.method == 'PUT':
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = Asset().updateAsset(asset_id, requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 删除
    # DELETE /tree/asset/asset_id 删除资产
    elif request.method == 'DELETE':
        # 处理数据
        dbStatus = Asset().deleteAsset(asset_id)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 非法请求
    else:
        response = MyResponse().void()
    return response

def tree_correlation_all(request):
    # 查看
    # GET /tree/asset/tree_correlation/ 查看所有资产
    if request.method == 'GET':
        # 处理数据
        data = Asset().getIdentityByNode('')
        # 拼接返回值
        response = MyResponse().succeed(data)
    # 非法请求
    else:
        response = MyResponse().void()
    return response

def tree_correlation(request, node_name):
    # 查看
    # GET /tree/asset/correlation/node_name 基于node_name查看资产
    if request.method == 'GET':
        # 处理数据
        data = Asset().getIdentityByNode(node_name)
        # 拼接返回值
        response = MyResponse().succeed(data)
    # 增加
    # POST /tree/asset/correlation/ 新建关联
    elif request.method == 'POST':
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = Asset().addCorrelation(node_name, requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 删除
    # DELETE /tree/asset/correlation/node_name 删除关联
    elif request.method == 'DELETE':
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = Asset().deleteCorrelation(node_name, requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 非法请求
    else:
        response = MyResponse().void()
    return response
