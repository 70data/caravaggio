# coding=utf-8

from utils.db import db_engine

class UserModel(object):

    def get(self, user_name):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT user_id, user_name, mail FROM auth_user WHERE user_name='{}'".format(user_name)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        auth_user = {}
        for row in result:
            auth_user['user_id'] = row[0]
            auth_user['user_name'] = row[1]
            auth_user['mail'] = row[2]
        # 拼接返回值
        data = auth_user
        return data

    def add(self, user_name, requestData):
        user_mail = requestData['mail']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO auth_user (user_name, mail) VALUES ('{}', '{}')".format(user_name, user_mail)
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

    def update(self, user_name, requestData):
        user_mail = requestData['mail']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "UPDATE auth_user SET user_name='{}', mail='{}' WHERE user_name='{}'".format(user_name, user_mail, user_name)
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

    def delete(self, user_name):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "DELETE FROM auth_user WHERE user_name='{}'".format(user_name)
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

class PermissionModel(object):

    def get(self, permission_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT permission_id, server_name, method, url FROM auth_permission WHERE permission_id={}".format(permission_id)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        auth_permission = {}
        for row in result:
            auth_permission['permission_id'] = row[0]
            auth_permission['server_name'] = row[1]
            auth_permission['method'] = row[2]
            auth_permission['url'] = row[3]
        # 拼接返回值
        data = auth_permission
        return data

    def getPermissionid(self, server_name, method, url):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT permission_id FROM auth_permission WHERE server_name='{}' AND method='{}' AND url='{}'".format(server_name, method, url)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        for row in result:
            permission_id = row[0]
        # 拼接返回值
        data = permission_id
        return data

    def add(self, requestData):
        server_name = requestData['server_name']
        method = requestData['method']
        url = requestData['url']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO auth_permission (server_name, method, url) VALUES ('{}', '{}', '{}')".format(server_name, method, url)
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

    def delete(self, permission_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "DELETE FROM auth_permission WHERE permission_id={}".format(permission_id)
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

class RoleModel(object):

    def get(self, role_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT role_id, role_name, role_description FROM auth_role WHERE role_id={}".format(role_id)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        auth_user = {}
        for row in result:
            auth_user['role_id'] = row[0]
            auth_user['role_name'] = row[1]
            auth_user['role_description'] = row[2]
        # 拼接返回值
        data = auth_user
        return data

    def add(self, requestData):
        role_name = requestData['role_name']
        role_description = requestData['role_description']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO auth_role (role_name, role_description) VALUES ('{}', '{}')".format(role_name, role_description)
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

    def update(self, role_id, requestData):
        role_name = requestData['role_name']
        role_description = requestData['role_description']
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "UPDATE auth_role SET role_name='{}', role_description='{}' WHERE role_id={}".format(role_name, role_description, role_id)
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

    def delete(self, role_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "DELETE FROM auth_role WHERE role_id={}".format(role_id)
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

class RolePermissionModel(object):

    def get(self, role_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT permission_id, server_name, method, url FROM auth_permission WHERE permission_id in (SELECT permission_id FROM auth_role_permission WHERE auth_role_permission.role_id={})".format(role_id)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        auth_permissions = []
        for row in result:
            auth_permission = {}
            auth_permission['permission_id'] = row[0]
            auth_permission['server_name'] = row[1]
            auth_permission['method'] = row[2]
            auth_permission['url'] = row[3]
            auth_permissions.append(auth_permission)
        # 拼接返回值
        data = auth_permissions
        return data

    def getRoleids(self, permission_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT role_id FROM auth_role_permission WHERE auth_role_permission.permission_id={}".format(permission_id)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        role_ids = []
        for row in result:
            role_id = row[0]
            role_ids.append(role_id)
        # 拼接返回值
        data = role_ids
        return data

    def add(self, role_id, permission_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO auth_role_permission (role_id, permission_id) VALUES ({}, {})".format(role_id, permission_id)
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

    def delete(self, role_id, permission_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "DELETE FROM auth_role_permission WHERE role_id={} AND permission_id={}".format(role_id, permission_id)
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

class UserRoleModel(object):

    def get(self, user_name, server_name):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "SELECT role_id, role_name, role_description FROM auth_role WHERE role_id in (SELECT role_id FROM auth_user_role WHERE auth_user_role.user_id=(SELECT user_id FROM auth_user WHERE auth_user.user_name='{}') AND server_name='{}')".format(user_name, server_name)
        print(sql)
        # 执行SQL
        result = db_conn.execute(sql)
        # 释放连接
        db_conn.close()
        # 处理结果
        auth_roles = []
        for row in result:
            auth_role = {}
            auth_role['role_id'] = row[0]
            auth_role['role_name'] = row[1]
            auth_role['role_description'] = row[2]
            auth_roles.append(auth_role)
        # 拼接返回值
        data = auth_roles
        return data

    def add(self, user_name, server_name, role_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "INSERT INTO auth_user_role (user_id, server_name, role_id) VALUES ((SELECT user_id FROM auth_user WHERE auth_user.user_name='{}'), '{}', {})".format(user_name, server_name, role_id)
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

    def delete(self, user_name, server_name, role_id):
        # 获取连接
        db_conn = db_engine.connect()
        # 生成SQL
        sql = "DELETE FROM auth_user_role WHERE user_id=(SELECT user_id FROM auth_user WHERE auth_user.user_name='{}') AND server_name='{}' AND role_id={}".format(user_name, server_name, role_id)
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
