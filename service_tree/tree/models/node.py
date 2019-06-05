# coding=utf-8

from utils.db import db_engine

class Node(object):

    def getNodeDownstream(self, node_name):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT node_id, node_name, node_upstream_name, node_description FROM tree_node WHERE node_upstream_name='{}' ORDER BY node_name".format(node_name)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        tree_nodes = []
        for row in result:
            tree_node = {}
            tree_node['id'] = row[0]
            tree_node['name'] = row[1]
            tree_node['upstream_name'] = row[2]
            tree_node['node_description'] = row[3]
            tree_nodes.append(tree_node)
        # 拼接返回值
        data = {}
        data['tree_nodes'] = tree_nodes
        return data

    def getNode(self, node_name):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT node_id, node_name, node_upstream_name, node_description FROM tree_node WHERE node_name='{}' ORDER BY node_name".format(node_name)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        tree_nodes = []
        for row in result:
            tree_node = {}
            tree_node['id'] = row[0]
            tree_node['name'] = row[1]
            tree_node['upstream_name'] = row[2]
            tree_node['description'] = row[3]
            tree_nodes.append(tree_node)
        # 拼接返回值
        data = {}
        data['tree_nodes'] = tree_nodes
        return data

    def addNode(self, node_name, requestData):
        upstream_name = '.'.join(node_name.split('.')[:-1])
        description = requestData['description']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO tree_node (node_name, node_upstream_name, node_description) VALUES ('{}', '{}', '{}')".format(node_name, upstream_name, description)
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

    def updateNode(self, node_name, requestData):
        new_node_name = requestData['name']
        new_upstream_name = '.'.join(new_node_name.split('.')[:-1])
        new_description = requestData['description']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "UPDATE tree_node SET node_name='{}', node_upstream_name='{}', node_description='{}' WHERE node_name='{}'".format(new_node_name, new_upstream_name, new_description, node_name)
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

    def deleteNode(self, node_name):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "DELETE FROM tree_node WHERE node_name='{}'".format(node_name)
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
