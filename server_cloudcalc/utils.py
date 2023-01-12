'''
Description:
version: 
Author: Zhang Zhifang
Date: 2023-01-10 01:19:41
LastEditTime: 2023-01-12 13:47:33
'''
'''
增 a
删 d
改 c
查 s
'''
from beans import Smoke, Miner
from itertools import groupby
import pymysql
import conf


def init_dataset():
    conn = pymysql.connect(
        user=conf.USER,
        password=conf.PASSWORD,
        host=conf.HOST_IP,
        database=conf.DATABASE,
        port=conf.MYSQL_PORT,
        charset=conf.CHARSET,
    )
    cursor = conn.cursor()
    cursor.execute('use DUST;')
    return conn, cursor


def operate(cursor, sql, mode='ss'):
    cursor.execute(sql)
    if mode[0] in ['a', 'c', 'd']:
        return True
    elif mode[0] == 's':
        results = cursor.fetchall()
        objects = []
        for res in results:
            if mode[1] == 's':
                objects.append(Smoke(*res))
            if mode[1] == 'm':
                objects.append(Miner(*res))
            elif mode[1] == 'r':  # random search
                objects.append(res)
        return objects


def group_by_key(arr, func):
    return [list(grp) for (match, grp) in groupby(arr, func)]
