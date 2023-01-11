'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-09 00:07:04
LastEditTime: 2023-01-10 00:53:47
'''
import pymysql
import threading
import time
'''
解码报文
s: f_id,id,conc,temp,hum
w: f_id,id,x,y
'''


def encrypt_parse(str):
    arr = str.split('/')
    mode = arr[1][0]
    f_id = arr[1][1]
    info = []
    for i in range(2, len(arr)):
        temp = arr[i].split('&')
        temp.insert(0, f_id)
        info.append(temp)
    return (mode, info)


'''
初始化数据库
'''


def init_dataset():
    conn = pymysql.connect(
        user='root',
        password='1234aA',
        host='39.108.120.233',
        database='DUST',
        port=3306,
        charset='utf8mb4',
    )
    return conn


'''
上传数据库
'''


def upload(str, conn):
    # lock = threading.Lock()
    # lock.acquire()
    cursor = conn.cursor()
    mode, info = encrypt_parse(str)
    if mode == 'w':
        sqls = upload_worker_pos(info)
    if mode == 's':
        sqls = upload_sensor_spvs(info)
    for sql in sqls:
        print(sql)
        time.sleep(1)
        cursor.execute(sql)  #3
    conn.commit()  #2
    # lock.release()


'''
上传worker_pos表
'''


def upload_worker_pos(info):
    sqls = []
    # w: f_id,id,x,y
    for item in info:
        sql = 'INSERT INTO worker_pos(f_id,id,x,y) VALUES '
        f_id = item[0]
        id = item[1]
        x = item[2]
        y = item[3]
        sql += '({},{},{},{});'.format(f_id, id, x, y)
        sqls.append(sql)
        return sqls


'''
上传sensor_spvs表
s: f_id,id,conc,temp,hum
'''


def upload_sensor_spvs(info):
    sqls = []
    # s: f_id,id,conc,temp,hum
    for item in info:
        sql = 'INSERT INTO sensor_spvs(f_id,id,concentration,temperature,humidity) VALUES '
        f_id = item[0]
        id = item[1]
        conc = item[2]
        temp = item[3]
        hum = item[4]
        sql += '({},{},{},{},{});'.format(f_id, id, conc, temp, hum)
        sqls.append(sql)
        return sqls


def run(new_client_socket):
    conn = init_dataset()
    conn.cursor().execute('USE DUST;')
    conn.commit()
    while True:
        recv_date = new_client_socket.recv(1024)
        if recv_date:
            lock = threading.Lock()
            lock.acquire()
            str = recv_date.decode("utf-8")
            upload(str, conn)
            lock.release()
        else:
            break
    new_client_socket.close()
    conn.close()
