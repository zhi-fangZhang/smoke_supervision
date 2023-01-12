'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-12 11:17:42
LastEditTime: 2023-01-13 00:56:51
'''
import pymysql
from beans import *
import conf


class Register:
    def __init__(self):
        self.conn = pymysql.connect(
            user=conf.USER,
            password=conf.PASSWORD,
            host=conf.HOST_IP,
            database=conf.DATABASE,
            port=conf.MYSQL_PORT,
            charset=conf.CHARSET,
        )

    def register_i(self,i):
        cursor = self.conn.cursor()
        cursor.execute('use DUST')
        workers = []
        sensors = []
        for k, dic in enumerate(conf.REGISTER_DICT):
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
                workers.append(Worker(dic['f_id'],wdic['id'], 1, 1, wdic['speed']))
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
                sensors.append(Sensor(dic['f_id'],sdic['id'], sdic['x'], sdic['y']))
            self.conn.commit()
            self.conn.close()
            return Factory(dic['width'], dic['length'], dic['f_id'],
                                    sensors, workers)
