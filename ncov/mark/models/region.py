# coding=utf-8

from utils.db import sql_execute


class Region(object):

    def insert(self):
        pid = self['partnerId']
        level = self['level'] + 1
        name = self['name']
        # 生成SQL
        sql = "INSERT INTO region (pid, level, code, name) VALUES ('{}', '{}', 666, '{}')".format(
            pid, level, name)
        result, status = sql_execute(sql)
        return result, status

    def info(self):
        # 生成SQL
        sql = "SELECT id, pid, level, name FROM region WHERE id='{}'".format(
            self)
        result, status = sql_execute(sql)
        # 处理结果
        data = []
        try:
            for row in result:
                region_id = row[0]
                region_pid = row[1]
                region_level = row[2]
                region_name = row[3]
            region_data = {
                'id': region_id,
                'pid': region_pid,
                'level': region_level,
                'name': region_name
            }
            data.append(region_data)
        except:
            pass
        return data

    def get_next(self):
        loc_id = self['locId']
        # 生成SQL
        sql = "SELECT id, level, name FROM region WHERE pid='{}'".format(
            loc_id)
        result, status = sql_execute(sql)
        # 处理结果
        data = []
        try:
            for row in result:
                scope_data = {
                    'id': row[0],
                    'level': row[1],
                    'name': row[2]
                }
                data.append(scope_data)
        except:
            pass
        return data, status

    def get_loc_name(region_id, region_name):
        global loc_name
        # 生成SQL
        sql = "SELECT pid, level, name FROM region WHERE id='{}'".format(
            region_id)
        result, status = sql_execute(sql)
        # 处理结果
        try:
            for row in result:
                pid = row[0]
                level = row[1]
                name = row[2]
        except:
            pass
        if region_name == '':
            loc_name = name
        else:
            loc_name = '{}-{}'.format(name, region_name)
        # 如果不是 1 需要继续查询
        if level != 1:
            Region.get_loc_name(pid, loc_name)
        return loc_name

    def get_ids(id, id_list):
        sids, id_level = Region.get_sids(id)
        # ==空 没有子集
        if len(sids) != 0:
            id_list.extend(sids)
            # ==4 没有子集
            if id_level != 4:
                for sid in sids:
                    Region.get_ids(sid, id_list)
        return id_list

    def get_sids(self):
        id_level = 0
        # 生成SQL
        sql = "SELECT id, level FROM region WHERE pid='{}'".format(
            self)
        result, status = sql_execute(sql)
        # 处理结果
        ids = []
        try:
            for row in result:
                ids.append(row[0])
                id_level = row[1]
        except:
            pass
        return ids, id_level
