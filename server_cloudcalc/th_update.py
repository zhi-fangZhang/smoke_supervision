'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-10 00:09:22
LastEditTime: 2023-01-12 15:27:39
'''
import update_sensor
import update_miner
import utils
import time
import conf

def update():
    while True:
        conn, cursor = utils.init_dataset()
        update_sensor.check_overrich(cursor)
        update_miner.check_dust(cursor)
        conn.commit()
        conn.close()
        time.sleep(conf.DETECT_INTERVAL)



