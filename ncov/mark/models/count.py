# coding=utf-8

import time

from utils.db import sql_execute
from .region import Region
from .user import User


class Count(object):

    def insert(self):
        region_id = self['countRegionId']
        date = self['countDate']
        confirm = self['countConfirm']
        recover = self['countRecover']
        dead = self['countDead']
        source_url = self['countSourceUrl']
        source_text = self['countSourceText']
        token = self['token']
        user_id = User.info_by_token(token)[0]['id']
        create_time = time.time()
        modified_time = time.time()
        search_count_info = {
            'locId': region_id,
            'date': date
        }
        search_data, status = Count.info(search_count_info)
        if len(search_data) != 0:
            count_status = search_data[0]['countStatus']
            # 已存在
            if count_status == 1:
                return [], 'existed'
            # 已删除
            else:
                # 生成SQL
                sql = "UPDATE count SET status=1 WHERE count_region_id='{}' AND count_date='{}'".format(
                    region_id, date)
                result, status = sql_execute(sql)
                return result, status
        # 生成SQL
        sql = "INSERT INTO count (count_region_id, count_date, count_confirm, count_recover, count_dead, count_source_url, count_source_text, count_user_id, count_create_time, count_modified_time) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            region_id, date, confirm, recover, dead, source_url, source_text, user_id, create_time, modified_time)
        result, status = sql_execute(sql)
        return result, status

    def update(self):
        count_id = self['id']
        region_id = self['countRegionId']
        date = self['countDate']
        confirm = self['countConfirm']
        recover = self['countRecover']
        dead = self['countDead']
        source_url = self['countSourceUrl']
        source_text = self['countSourceText']
        modified_time = time.time()
        token = self['token']
        user_info = User.info_by_token(token)[0]
        is_admin = user_info['admin']
        user_id = user_info['id']
        count_user_id = Count.info_by_id(count_id)[0]['count_user_id']
        if is_admin == 1 or user_id == count_user_id:
            # 生成SQL
            sql = "UPDATE count SET count_region_id='{}', count_date='{}', count_confirm='{}', count_recover='{}', count_dead='{}', count_source_url='{}', count_source_text='{}', count_modified_time='{}' WHERE id='{}'".format(
                region_id, date, confirm, recover, dead, source_url, source_text, modified_time, count_id)
            result, status = sql_execute(sql)
            return result, status
        else:
            return [], 'permission'

    def delete(self):
        count_id = self['countId']
        region_id = Count.info_by_id(count_id)[0]['region_id']
        token = self['token']
        user_info = User.info_by_token(token)[0]
        is_admin = user_info['admin']
        user_id = user_info['id']
        count_user_info = Count.info_by_id(count_id)[0]
        count_user_id = count_user_info['count_user_id']
        count_date = count_user_info['count_date']
        if is_admin == 1 or user_id == count_user_id:
            ids = Region.get_ids(region_id, [region_id])
            # 删除 count
            sql = "UPDATE count SET status=0 WHERE id='{}'".format(
                count_id)
            result, status = sql_execute(sql)
            # 删除 子count & 子sample
            for loc_id in ids:
                sql = "UPDATE count SET status=0 WHERE count_date='{}' AND count_region_id='{}'".format(
                    count_date, loc_id)
                sql_execute(sql)
                sql = "UPDATE sample SET status=0 WHERE sample_confirm_time='{}' AND sample_region_id='{}'".format(
                    count_date, loc_id)
                sql_execute(sql)
            return result, status
        else:
            return [], 'permission'

    def info_by_id(self):
        # 生成SQL
        sql = "SELECT count_region_id, count_date, count_confirm, count_recover, count_dead, count_source_url, count_source_text, count_user_id FROM count WHERE id='{}' AND status=1".format(
            self)
        result, status = sql_execute(sql)
        # 处理结果
        data = []
        try:
            for row in result:
                count_info = {
                    'region_id': row[0],
                    'count_date': row[1],
                    'count_confirm': row[2],
                    'count_recover': row[3],
                    'count_dead': row[4],
                    'count_source_url': row[5],
                    'count_source_text': row[6],
                    'count_user_id': row[7]
                }
                data.append(count_info)
        except:
            pass
        return data

    def info(self):
        id_list = self['locId']
        count_date = self['date']
        # 生成SQL
        sql = "SELECT id, count_confirm, count_recover, count_dead, count_source_url, count_source_text, count_region_id, status FROM count WHERE count_region_id in ({}) AND count_date='{}' AND status=1".format(
            id_list, count_date)
        result, status = sql_execute(sql)
        # 处理结果
        data = []
        try:
            for row in result:
                user_data = {
                    'id': row[0],
                    'countConfirm': row[1],
                    'countRecover': row[2],
                    'countDead': row[3],
                    'countSourceUrl': row[4],
                    'countSourceText': row[5],
                    'countRegionId': row[6],
                    'countStatus': row[7]
                }
                loc_name = Region.get_loc_name(row[6], '')
                user_data['locName'] = loc_name
                data.append(user_data)
        except:
            pass
        return data, status

    def info_all(self):
        count_region_id = self['locId']
        count_date = self['date']
        level = Region.info(count_region_id)[0]['level']
        if level != 2:
            return [], 'void'
        token = self['token']
        region_info = User.info_by_token(token)[0]['region_info']
        region_ids = []
        for one_region in region_info:
            region_ids.append(one_region['id'])
        if count_region_id not in region_ids:
            return [], 'void'
        ids = Region.get_ids(count_region_id, [count_region_id])
        id_list = ','.join([str(x) for x in ids])
        # 处理结果
        id_data = {
            'locId': id_list,
            'date': count_date
        }
        data, status = Count.info(id_data)
        return data, status
