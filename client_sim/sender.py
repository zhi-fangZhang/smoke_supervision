'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 00:39:49
LastEditTime: 2023-01-13 00:51:22
'''

import threading
import socket
import conf



DISTRIBUTION_IP = conf.DISTRIBUTION_IP
DISTRIBUTION_PORT = conf.DISTRIBUTION_PORT


class Sender:
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((DISTRIBUTION_IP, DISTRIBUTION_PORT))

    def send(self, objs,mode='s'):
        lock = threading.Lock()
        lock.acquire()
        info=self.encrypt(objs,mode)
        self.clientSocket.send(info.encode('utf-8'))
        lock.release()

    def encrypt(self,objs, mode='s'):
        out = '/{}{}'.format(mode, objs[0].f_id)
        if mode == 's':
            for sensor in objs:
                out = out + '/{}&{}&{}&{}'.format(
                    sensor.id, sensor.concentration, sensor.temperature,
                    sensor.humidity)
        elif mode == 'w':
            for worker in objs:
                out = out + '/{}&{}&{}'.format(worker.id, worker.x, worker.y)
        out += '[SPLIT]'
        return out
    



