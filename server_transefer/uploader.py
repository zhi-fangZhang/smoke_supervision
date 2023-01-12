'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-13 01:01:08
LastEditTime: 2023-01-13 01:34:51
'''
import conf
import time
import pymysql


class Uploader:

    def __init__(self):
        self.conn = pymysql.connect(
        user=conf.USER,
        password=conf.PASSWORD,
        host=conf.HOST_IP,
        database=conf.DATABASE,
        port=conf.MYSQL_PORT,
        charset=conf.CHARSET,
    )

    '''
    上传数据库
    '''

    def upload(self,strs):
        cursor = self.conn.cursor()
        for str in strs.split('[SPLIT]')[:-1]:
            mode, info = self.encrypt_parse(str)
            if mode == 'w':
                sqls = self.upload_worker_pos(info)
            if mode == 's':
                sqls = self.upload_sensor_spvs(info)
            for sql in sqls:
                time.sleep(conf.EXECUTE_PAUSE)
                print(sql)
                cursor.execute(sql)  #3
        self.conn.commit()  #2


    '''
    上传worker_pos表
    '''
    def upload_worker_pos(self,info):
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


    def upload_sensor_spvs(self,info):
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

    def encrypt_parse(self,str):
        arr = str.split('/')
        mode = arr[1][0]
        f_id = arr[1][1]
        info = []
        for i in range(2, len(arr)):
            temp = arr[i].split('&')
            temp.insert(0, f_id)
            info.append(temp)
        return (mode, info)