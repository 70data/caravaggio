# coding=utf-8

import datetime
import json
import time

from utils.db import sql_execute
from .region import Region
from .user import User


class Sample(object):

    def insert(self):
        token = self['token']
        user_id = User.info_by_token(token)[0]['id']
        create_time = time.time()
        modified_time = time.time()
        region_id = self['sampleRegionId']
        sample_type = self['sampleType']
        sample_confirm_time = self['sampleConfirmTime']
        sample_sex = self['sampleSex']
        sample_age = self['sampleAge']
        source_url = self['sampleSourceUrl']
        source_text = self['sampleSourceText']
        custom_tag = json.dumps(self['sampleCustomTag'], ensure_ascii=False)
        # 生成SQL
        sql = "INSERT INTO sample (sample_user_id, sample_create_time, sample_modified_time, sample_region_id, sample_type, sample_confirm_time, sample_sex, sample_age, sample_source_url, sample_source_text, sample_custom_tag) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            user_id, create_time, modified_time, region_id, sample_type, sample_confirm_time, sample_sex, sample_age, source_url, source_text, custom_tag)
        result, status = sql_execute(sql)
        return result, status

    def update(self):
        sample_id = self['id']
        modified_time = time.time()
        region_id = self['sampleRegionId']
        sample_type = self['sampleType']
        sample_confirm_time = self['sampleConfirmTime']
        sample_sex = self['sampleSex']
        sample_age = self['sampleAge']
        source_url = self['sampleSourceUrl']
        source_text = self['sampleSourceText']
        custom_tag = json.dumps(self['sampleCustomTag'], ensure_ascii=False)
        token = self['token']
        user_info = User.info_by_token(token)[0]
        is_admin = user_info['admin']
        user_id = user_info['id']
        count_user_id = Sample.info_by_id(sample_id)[0]['sample_user_id']
        if is_admin == 1 or user_id == count_user_id:
            # 生成SQL
            sql = "UPDATE sample SET sample_modified_time='{}', sample_region_id='{}', sample_confirm_time='{}', sample_type='{}', sample_sex='{}', sample_age='{}', sample_source_url='{}', sample_source_text='{}', sample_custom_tag='{}' WHERE id='{}'".format(
                modified_time, region_id, sample_confirm_time, sample_type, sample_sex, sample_age,  source_url, source_text, custom_tag, sample_id)
            result, status = sql_execute(sql)
            return result, status
        else:
            return [], 'permission'

    def delete(self):
        sample_id = self['patId']
        token = self['token']
        user_info = User.info_by_token(token)[0]
        is_admin = user_info['admin']
        user_id = user_info['id']
        count_user_id = Sample.info_by_id(sample_id)[0]['sample_user_id']
        if is_admin == 1 or user_id == count_user_id:
            # 生成SQL
            sql = "UPDATE sample SET status=0 WHERE id='{}'".format(
                sample_id)
            result, status = sql_execute(sql)
            return result, status
        else:
            return [], 'permission'

    def info_by_id(self):
        # 生成SQL
        sql = "SELECT sample_user_id, sample_region_id, sample_confirm_time, sample_type, sample_sex, sample_age, sample_source_text, sample_source_url, sample_custom_tag FROM sample WHERE id='{}' AND status=1".format(
            self)
        result, status = sql_execute(sql)
        # 处理结果
        data = []
        try:
            for row in result:
                sample_info = {
                    'sample_user_id': row[0],
                    'sample_region_id': row[1],
                    'sample_confirm_time': row[2],
                    'sample_type': row[3],
                    'sample_sex': row[4],
                    'sample_age': row[5],
                    'sample_source_text': row[6],
                    'sample_source_url': row[7],
                    'sample_custom_tag': row[8]
                }
                data.append(sample_info)
        except:
            pass
        return data

    def info(self):
        id_list = self['locId']
        sample_confirm_time = self['date']
        # 生成SQL
        sql = "SELECT id, sample_region_id, sample_confirm_time, sample_type, sample_sex, sample_age, sample_source_text, sample_source_url, sample_custom_tag FROM sample WHERE sample_region_id in ({}) AND sample_confirm_time='{}' AND status=1".format(
            id_list, sample_confirm_time)
        result, status = sql_execute(sql)
        # 处理结果
        data = []
        try:
            for row in result:
                tags = []
                if row[8] != '':
                    try:
                        tags = json.loads(row[8], encoding='utf-8')
                    except:
                        pass
                user_data = {
                    'id': row[0],
                    'sampleRegionId': row[1],
                    'sampleConfirmTime': row[2].strftime("%Y-%m-%d"),
                    'sampleType': row[3],
                    'sampleSex': row[4],
                    'sampleAge': row[5],
                    'sampleSourceText': row[6],
                    'sampleSourceUrl': row[7],
                    'sampleCustomTag': tags
                }
                loc_name = Region.get_loc_name(row[1], '')
                user_data['locName'] = loc_name
                data.append(user_data)
        except:
            pass
        return data, status

    def info_all(self):
        sample_region_id = self['locId']
        sample_confirm_time = self['date']
        level = Region.info(sample_region_id)[0]['level']
        if level != 2:
            return [], 'void'
        token = self['token']
        region_info = User.info_by_token(token)[0]['region_info']
        region_ids = []
        for one_region in region_info:
            region_ids.append(one_region['id'])
        if sample_region_id not in region_ids:
            return [], 'void'
        ids = Region.get_ids(sample_region_id, [sample_region_id])
        id_list = ','.join([str(x) for x in ids])
        # 处理结果
        id_data = {
            'locId': id_list,
            'date': sample_confirm_time
        }
        data, status = Sample.info(id_data)
        return data, status
