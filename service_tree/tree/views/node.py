# coding=utf-8

import json
from utils.response import MyResponse
from ..models.node import Node
from ..models.asset import Asset

def tree_downstream_root(request):
    # 查看
    # GET /tree/node/downstream/ 查看根结点
    if request.method == 'GET':
        # 处理数据
        data = Node().getNodeDownstream('')
        # 拼接返回值
        response = MyResponse().succeed(data)
    # 非法请求
    else:
        response = MyResponse().void()
    return response

def tree_downstream(request, node_name):
    # 查看
    # GET /tree/node/downstream/node_name 查看下游节点
    if request.method == 'GET':
        # 处理数据
        data = Node().getNodeDownstream(node_name)
        # 拼接返回值
        response = MyResponse().succeed(data)
    # 非法请求
    else:
        response = MyResponse().void()
    return response

def tree_node(request, node_name):
    # 查看
    # GET /tree/node/node_name 查看节点
    if request.method == 'GET':
        # 处理数据
        data = Node().getNode(node_name)
        # 拼接返回值
        response = MyResponse().succeed(data)
    # 增加
    # POST /tree/node/node_name 增加节点
    elif request.method == 'POST':
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = Node().addNode(node_name, requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 修改
    # PUT /tree/node/node_name 修改节点
    elif request.method == 'PUT':
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        # 修改节点信息
        updateNodeStatus = Node().updateNode(node_name, requestData)
        # 修改节点下资产的节点信息
        updateIdentityStatus = Asset().updateIdentityByNode(node_name, requestData)
        # 拼接返回值
        if updateNodeStatus == 'succeed' and updateIdentityStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
    # 删除
    # DELETE /tree/node/node_name 删除节点
    elif request.method == 'DELETE':
        # 处理数据
        # 查看是否有子节点
        nodeDownstream = Node().getNodeDownstream(node_name)
        # 查看节点下是否有机器
        asset = Asset().getIdentityByNode(node_name)
        if nodeDownstream['tree_nodes'] == [] and asset['tree_assets'] == []:
            # 删除节点
            dbStatus = Node().deleteNode(node_name)
            # 拼接返回值
            if dbStatus == 'succeed':
                response = MyResponse().succeed({})
            else:
                response = MyResponse().failed('process failed')
        else:
            response = MyResponse().failed('process failed')
    # 非法请求
    else:
        response = MyResponse().void()
    return response
