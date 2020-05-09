# coding=utf-8

import hashlib
import time
import uuid

from utils.db import sql_execute
from .region import Region


class User(object):

    def register(self):
        phone = self['phone']
        md = hashlib.md5()
        md.update(self['password'].encode('utf-8'))
        password = md.hexdigest()
        create_time = time.time()
        modified_time = time.time()
        token = str(uuid.uuid4())
        # 查看用户 如果存在 则不让重复注册
        result = User.info_by_phone(self)
        if len(result) != 0:
            return [], 'existed'
        # 生成SQL
        sql = "INSERT INTO user (phone, password, status, create_time, modified_time, token) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            phone, password, 1, create_time, modified_time, token)
        result, status = sql_execute(sql)
        return token, status

    def update(self):
        phone = self['phone']
        region_ids = self['region_id']
        region_id = ''
        for id in region_ids:
            if region_id == '':
                region_id = id
            else:
                region_id = "{},{}".format(region_id, id)
        # 生成SQL
        sql = "UPDATE user SET region_id='{}' WHERE phone='{}'".format(
            region_id, phone)
        result, status = sql_execute(sql)
        return result, status

    def info_by_phone(self):
        phone = self['phone']
        # 生成SQL
        sql = "SELECT id, phone, password, region_id, token, admin FROM user WHERE phone='{}'".format(
            phone)
        result, status = sql_execute(sql)
        # 处理结果
        user_region_info = []
        data = []
        try:
            for row in result:
                user_id = row[0]
                user_phone = row[1]
                user_password = row[2]
                if row[2] != '':
                    user_region_ids = [int(i) for i in row[3].split(',')]
                    for user_region_id in user_region_ids:
                        region_info = Region.info(user_region_id)
                        user_region_info.extend(region_info)
                user_token = row[4]
                user_admin = row[5]
                user_data = {
                    'id': user_id,
                    'phone': user_phone,
                    'password': user_password,
                    'region_info': user_region_info,
                    'token': user_token,
                    'admin': user_admin
                }
                data.append(user_data)
        except:
            pass
        return data

    def info_by_token(self):
        # 生成SQL
        sql = "SELECT id, phone, password, region_id, token, admin FROM user WHERE token='{}'".format(
            self)
        result, status = sql_execute(sql)
        # 处理结果
        user_region_info = []
        data = []
        try:
            for row in result:
                user_id = row[0]
                user_phone = row[1]
                user_password = row[2]
                if row[3] != '':
                    user_region_ids = [int(i) for i in row[3].split(',')]
                    for user_region_id in user_region_ids:
                        region_info = Region.info(user_region_id)
                        user_region_info.extend(region_info)
                user_token = row[4]
                user_admin = row[5]
                user_data = {
                    'id': user_id,
                    'phone': user_phone,
                    'password': user_password,
                    'region_info': user_region_info,
                    'token': user_token,
                    'admin': user_admin
                }
                data.append(user_data)
        except:
            pass
        return data

    def login(self):
        md = hashlib.md5()
        md.update(self['password'].encode('utf-8'))
        password = md.hexdigest()
        # 查看用户 如果不存在 则不让登陆
        result = User.info_by_phone(self)
        if len(result) == 0:
            return [], ''
        # 判断 密码是否一致
        if password == result[0]['password']:
            return result, 'succeed'
        else:
            return result, 'failed'
