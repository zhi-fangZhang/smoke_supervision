'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-10 00:09:22
LastEditTime: 2023-01-10 14:36:37
'''
import update_sensor
import update_miner
import utils
import time


def update():
    conn, cursor = utils.init_dataset()
    update_sensor.check_overrich(cursor)
    update_miner.check_dust(cursor)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    while True:
        update()
        time.sleep(utils.DETECT_INTERVAL)