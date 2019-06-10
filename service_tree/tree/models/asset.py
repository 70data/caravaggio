# coding=utf-8

from utils.db import db_engine

class Asset(object):

    def getAssetList(self):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT asset_id, asset_source, asset_type, asset_identity, asset_description FROM tree_asset"
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
            tree_asset['source'] = row[1]
            tree_asset['type'] = row[2]
            tree_asset['identity'] = row[3]
            tree_asset['description'] = row[4]
            tree_assets.append(tree_asset)
        # 拼接返回值
        data = {}
        data['tree_assets'] = tree_assets
        return data

    def getAsset(self, asset_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT asset_id, asset_source, asset_type, asset_identity, asset_description FROM tree_asset WHERE asset_id={}".format(asset_id)
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
            tree_asset['source'] = row[1]
            tree_asset['type'] = row[2]
            tree_asset['identity'] = row[3]
            tree_asset['description'] = row[4]
            tree_assets.append(tree_asset)
        # 拼接返回值
        data = {}
        data['tree_assets'] = tree_assets
        return data

    def addAsset(self, requestData):
        asset_source = requestData['source']
        asset_type = requestData['type']
        asset_identity = requestData['identity']
        asset_description = requestData['description']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO tree_asset (asset_source, asset_type, asset_identity, asset_description) VALUES ('{}', '{}', '{}', '{}')".format(asset_source, asset_type, asset_identity, asset_description)
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
        asset_source = requestData['source']
        asset_type = requestData['type']
        asset_identity = requestData['identity']
        asset_description = requestData['description']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "UPDATE tree_asset SET asset_source='{}', asset_type='{}', asset_identity='{}', asset_description='{}' WHERE asset_id='{}'".format(asset_source, asset_type, asset_identity, asset_description, asset_id)
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

class Correlation(object):

    def getIdentityByNode(self, node_name):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        if node_name == '':
            sql = "SELECT node_name, asset_identity FROM tree_correlation, tree_asset WHERE tree_correlation.asset_id=tree_asset.asset_id ORDER BY node_name"
        else:
            sql = "SELECT node_name, asset_identity FROM tree_correlation, tree_asset WHERE node_name like '{}.%' AND tree_correlation.asset_id=tree_asset.asset_id ORDER BY node_name".format(node_name)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        tree_assets = []
        for row in result:
            tree_asset = {}
            tree_asset['node_name'] = row[0]
            tree_asset['identity'] = row[1]
            tree_assets.append(tree_asset)
        # 拼接返回值
        data = {}
        data['correlations'] = tree_assets
        return data

    def getNodeByIdentity(self, asset_identity):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT node_name FROM tree_correlation, tree_asset WHERE tree_correlation.asset_id=tree_asset.asset_id AND tree_asset.asset_identity='{}' ORDER BY node_name".format(asset_identity)
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
        node_names = Correlation().getNodeByIdentity(identity)['node_names']
        for i in node_names:
            if i == node_name:
                return 'failed'
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO tree_correlation (node_name, asset_id) VALUES ('{}', (SELECT asset_id FROM tree_asset WHERE asset_identity='{}'))".format(node_name, identity)
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

    def updateCorrelationByNode(self, node_name, requestData):
        new_node_name = requestData['node_name']
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
        sql = "DELETE FROM tree_correlation WHERE node_name='{}' AND asset_id=(SELECT asset_id FROM tree_asset WHERE asset_identity='{}')".format(node_name, identity)
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
