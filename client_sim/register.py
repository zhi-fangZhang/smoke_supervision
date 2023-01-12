'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-12 11:17:42
LastEditTime: 2023-01-12 14:07:56
'''
import pymysql
from worker import Worker
from sensor import Sensor
from client_upload import Client_generator
import conf

facs = conf.REGISTER_DICT


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


def register_i(i):
    conn = init_dataset()
    cursor = conn.cursor()
    cursor.execute('use DUST')
    workers = []
    sensors = []
    for k, dic in enumerate(facs):
        if i != k:
            continue

        cursor.execute(
            f'''INSERT IGNORE INTO factory_info (f_id,name,address,latitude,longitude,length,width,note)
              VALUES (
              {dic['f_id']},
              '{dic['name']}',
              '{dic['address']}',
              {dic['latitude']},
              {dic['longitude']},  
              {dic['length']},  
              {dic['width']},  
              '{dic['note']}'
              );  
              ''')
        for wdic in dic['workers_info']:
            cursor.execute(f'''
            INSERT IGNORE INTO worker_info (f_id,id,name,note)
            VALUES(
                {dic['f_id']},
                {wdic['id']},
                '{wdic['name']}',
                '{wdic['note']}'
            );
            ''')
            workers.append(Worker(wdic['id'], 1, 1, wdic['speed']))
        for sdic in dic['sensors_info']:
            cursor.execute(f'''
            INSERT IGNORE INTO sensor_info (id,f_id,x,y,note)
            VALUES(
                {sdic['id']},
                {dic['f_id']},
                {sdic['x']},
                {sdic['y']},
                '{sdic['note']}'
            );
            ''')
            sensors.append(Sensor(sdic['id'], sdic['x'], sdic['y']))
        conn.commit()
        conn.close()
        return Client_generator(dic['width'], dic['length'], dic['f_id'],
                                sensors, workers)
