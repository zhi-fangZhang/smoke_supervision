'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-11 01:07:46
LastEditTime: 2023-01-11 22:47:42
'''

import pymysql
from threading import Thread
import threading
import time


def init_dataset():
    conn = pymysql.connect(
        user='root',
        password='1234aA',
        host='39.108.120.233',
        database='DUST',
        port=3306,
        charset='utf8mb4',
    )
    cursor = conn.cursor()
    cursor.execute('use DUST;')
    return conn, cursor

def fetch(cursor, sql):
    cursor.execute(sql)
    arr=cursor.fetchall()
    return arr


class Retriever:
    def __init__(self) -> None:
        pass

    def fetch_every_time(self,sqls,signals,widgets):
        def th():
            if len(sqls)!=len(signals) or len(sqls)!=len(widgets):
                raise Exception()
            while True:
                self.fetch_now(sqls,signals,widgets)               
                time.sleep(1)
        th = Thread(target=th,args=())
        th.setDaemon(True)
        th.start()


    
    def fetch_once(self,sqls,signals,widgets):
        def th():
            self.fetch_now(sqls,signals,widgets)

        th = Thread(target=th,args=())
        th.setDaemon(True)
        th.start()
    
    def fetch_now(self,sqls,signals,widgets):
        lock = threading.Lock()
        lock.acquire()
        conn,cursor=init_dataset()
        for i in range(len(sqls)):
            signals[i].emit(widgets[i],fetch(cursor,sqls[i])) 
        conn.close()
        lock.release()



