# coding=utf-8

from utils.db import db_engine

class Asset(object):

    def getAsset(self, asset_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT asset_id, asset_type, asset_identity, node_name FROM tree_asset WHERE asset_id='{}'".format(asset_id)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        tree_assets = []
        for row in result:
            tree_asset = {}
            tree_asset['id'] = row[0]
            tree_asset['type'] = row[1]
            tree_asset['identity'] = row[2]
            tree_asset['node_name'] = row[3]
            tree_assets.append(tree_asset)
        # 拼接返回值
        data = {}
        data['tree_assets'] = tree_assets
        return data

    def addAsset(self, requestData):
        type = requestData['type']
        identity = requestData['identity']
        node_name = requestData['node_name']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO tree_asset (asset_type, asset_identity, node_name) VALUES ('{}', '{}', '{}')".format(type, identity, node_name)
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

    def updateAsset(self, asset_id, requestData):
        type = requestData['type']
        identity = requestData['identity']
        node_name = requestData['node_name']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "UPDATE tree_asset SET asset_type='{}', asset_identity='{}', node_name='{}' WHERE asset_id='{}'".format(type, identity, node_name, asset_id)
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

    def deleteAsset(self, asset_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "DELETE FROM tree_asset WHERE asset_id='{}'".format(asset_id)
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

    def getIdentityByNode(self, node_name):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        if node_name == '':
            sql = "SELECT asset_identity, node_name FROM tree_correlation"
        else:
            sql = "SELECT asset_identity, node_name FROM tree_correlation WHERE node_name like '{}.%'".format(node_name)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        tree_assets = []
        for row in result:
            tree_asset = {}
            tree_asset['identity'] = row[0]
            tree_asset['node_name'] = row[1]
            tree_assets.append(tree_asset)
        # 拼接返回值
        data = {}
        data['tree_assets'] = tree_assets
        return data

    def getNodeByIdentity(self, asset_identity):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT node_name FROM tree_correlation WHERE asset_identity='{}'".format(asset_identity)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        node_names = []
        for row in result:
            node_names.append(row[0])
        # 拼接返回值
        data = {}
        data['node_names'] = node_names
        return data

    def addCorrelation(self, node_name, requestData):
        identity = requestData['identity']
        # 查看是否已关联
        node_names = Asset().getNodeByIdentity(identity)['node_names']
        for i in node_names:
            if i == node_name:
                return 'failed'
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO tree_correlation (node_name, asset_identity) VALUES ('{}', '{}')".format(node_name, identity)
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

    def updateIdentityByNode(self, node_name, requestData):
        new_node_name = requestData['name']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "UPDATE tree_correlation SET node_name='{}' WHERE node_name='{}'".format(new_node_name, node_name)
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

    def deleteCorrelation(self, node_name, requestData):
        identity = requestData['identity']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "DELETE FROM tree_correlation WHERE node_name='{}' AND asset_identity='{}'".format(node_name, identity)
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
