# coding=utf-8

from utils.db import db_engine

class Resource(object):

    def getResourceByAssetid(self, asset_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT resource_id, asset_id, resource_type, resource_name, resource_tag, resource_value FROM tree_resource WHERE asset_id='{}' ORDER BY resource_type".format(asset_id)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        node_resources = []
        for row in result:
            node_resource = {}
            node_resource['resource_id'] = row[0]
            node_resource['asset_id'] = row[1]
            node_resource['resource_type'] = row[2]
            node_resource['resource_name'] = row[3]
            node_resource['resource_tag'] = row[4]
            node_resource['resource_value'] = row[5]
            node_resources.append(node_resource)
        # 拼接返回值
        data = {}
        data['node_resources'] = node_resources
        return data

    def getResource(self, resource_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT resource_id, asset_id, resource_type, resource_name, resource_tag, resource_value FROM tree_resource WHERE resource_id='{}' ORDER BY resource_type".format(resource_id)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        node_resources = []
        for row in result:
            node_resource = {}
            node_resource['resource_id'] = row[0]
            node_resource['asset_id'] = row[1]
            node_resource['resource_type'] = row[2]
            node_resource['resource_name'] = row[3]
            node_resource['resource_tag'] = row[4]
            node_resource['resource_value'] = row[5]
            node_resources.append(node_resource)
        # 拼接返回值
        data = {}
        data['node_resources'] = node_resources
        return data

    def addResource(self, requestData):
        asset_id = requestData['asset_id']
        resource_type = requestData['resource_type']
        resource_name = requestData['resource_name']
        resource_tag = requestData['resource_tag']
        resource_value = requestData['resource_value']
        # TODO 需要判断资源是否已存在
        #
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO tree_resource (asset_id, resource_type, resource_name, resource_tag, resource_value) VALUES ('{}', '{}', '{}', '{}', '{}')".format(asset_id, resource_type, resource_name, resource_tag, resource_value)
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
        resource_type = requestData['resource_type']
        resource_name = requestData['resource_name']
        resource_tag = requestData['resource_tag']
        resource_value = requestData['resource_value']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "UPDATE tree_resource SET asset_id='{}', resource_type='{}', resource_name='{}', resource_tag='{}', resource_value='{}' WHERE resource_id='{}'".format(asset_id, resource_type, resource_name, resource_tag, resource_value, resource_id)
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
