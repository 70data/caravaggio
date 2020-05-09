# coding=utf-8

import sqlalchemy

# 全局连接池
db_engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:Password4Mysql!@39.99.156.174:3306/ncov')


def sql_execute(sql):
    print("SQL:", sql)
    # 获取连接
    db_conn = db_engine.connect()
    # 执行SQL
    try:
        result = db_conn.execute(sql)
        status = 'succeed'
    except:
        result = []
        status = 'failed'
    # 释放连接
    db_conn.close()
    return result, status
