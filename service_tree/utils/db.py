# coding=utf-8

import sqlalchemy

# 全局连接池
db_engine = sqlalchemy.create_engine('mysql+mysqlconnector://user:passwd)@ip:port/dbname')
