# coding=utf-8

from utils.db import db_engine

class Resource(object):

    def getResource(self, resource_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT resource_id, asset_id, resource_name, resource_tag, resource_value FROM tree_resource WHERE resource_id='{}' ORDER BY resource_name".format(resource_id)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        tree_resources = []
        for row in result:
            tree_resource = {}
            tree_resource['resource_id'] = row[0]
            tree_resource['asset_id'] = row[1]
            tree_resource['name'] = row[2]
            tree_resource['tag'] = row[3]
            tree_resource['value'] = row[4]
            tree_resources.append(tree_resource)
        # 拼接返回值
        data = {}
        data['tree_nodes'] = tree_resources
        return data

    def addResource(self, requestData):
        asset_id = requestData['asset_id']
        name = requestData['name']
        tag = requestData['tag']
        value = requestData['value']
        # 需要判断资源是否已存在
        # need to do
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO tree_resource (asset_id, resource_name, resource_tag, resource_value) VALUES ('{}', '{}', '{}', '{}')".format(asset_id, name, tag, value)
        print(sql)
        # 执行SQL
        try:
            db_conn.execute(sql)
            result = 'succeed'
        except:
            result = 'failed'
        # 释放连接
        db_conn.close()
        return result

    def updateResource(self, resource_id, requestData):
        asset_id = requestData['asset_id']
        name = requestData['name']
        tag = requestData['tag']
        value = requestData['value']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "UPDATE tree_resource SET asset_id='{}', resource_name='{}', resource_tag='{}', resource_value='{}' WHERE resource_id='{}'".format(asset_id, name, tag, value, resource_id)
        print(sql)
        # 执行SQL
        try:
            db_conn.execute(sql)
            result = 'succeed'
        except:
            result = 'failed'
        # 释放连接
        db_conn.close()
        return result

    def deleteResource(self, resource_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "DELETE FROM tree_resource WHERE resource_id='{}'".format(resource_id)
        print(sql)
        # 执行SQL
        try:
            db_conn.execute(sql)
            result = 'succeed'
        except:
            result = 'failed'
        # 释放连接
        db_conn.close()
        return result

    def getResourceByAssetid(self, asset_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT resource_id, asset_id, resource_name, resource_tag, resource_value FROM tree_resource WHERE asset_id='{}' ORDER BY resource_name".format(asset_id)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        tree_resources = []
        for row in result:
            tree_resource = {}
            tree_resource['resource_id'] = row[0]
            tree_resource['asset_id'] = row[1]
            tree_resource['name'] = row[2]
            tree_resource['tag'] = row[3]
            tree_resource['value'] = row[4]
            tree_resources.append(tree_resource)
        # 拼接返回值
        data = {}
        data['tree_nodes'] = tree_resources
        return data
