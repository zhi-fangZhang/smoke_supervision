'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 00:39:49
LastEditTime: 2023-01-12 14:11:02
'''
from factory import Factory
from worker import Worker
from sensor import Sensor
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import socket
import conf

SENSOR_INTERVAL = conf.SENSOR_INTERVAL
WORKER_INTERVAL = conf.WORKER_INTERVAL
SIMULATE_PAUSE = conf.SIMULATE_PAUSE
DISTRIBUTION_IP = conf.DISTRIBUTION_IP
DISTRIBUTION_PORT = conf.DISTRIBUTION_PORT


class Client_generator(Factory):
    def __init__(self, x_max, y_max, f_id, sensors, workers):
        super(Client_generator, self).__init__(x_max, y_max, f_id, sensors,
                                               workers)
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((DISTRIBUTION_IP, DISTRIBUTION_PORT))

    def send(self, info):
        lock = threading.Lock()
        lock.acquire()
        self.clientSocket.send(info.encode('utf-8'))
        lock.release()


def simulate(client):
    sensor_interval = SENSOR_INTERVAL
    worker_interval = WORKER_INTERVAL
    start = int(time.time())
    while True:
        now = int(time.time())
        if not (now - start) % sensor_interval:
            sensor_parse = client.update_sensors()
            client.send(sensor_parse)
        if not (now - start) % worker_interval:
            worker_parse = client.update_workers()
            client.send(worker_parse)
        time.sleep(SIMULATE_PAUSE)
