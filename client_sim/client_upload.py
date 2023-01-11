'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 00:39:49
LastEditTime: 2023-01-10 22:35:36
'''
from factory import Factory
from worker import Worker
from sensor import Sensor
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import socket


class Client_generator(Factory):
    def __init__(self, x_max, y_max, f_id, sensors, workers):
        super(Client_generator, self).__init__(x_max, y_max, f_id, sensors,
                                               workers)
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect(('127.0.0.1', 8080))

    def send(self, info):
        lock=threading.Lock()
        lock.acquire()
        self.clientSocket.send(info.encode('utf-8'))
        lock.release()

def simulate(client):
    sensor_interval = 5
    worker_interval = 10
    # sensor_interval = 5 * 60
    # worker_interval = 10
    start = int(time.time())
    while True:
        now = int(time.time())
        if not (now - start) % sensor_interval:
            sensor_parse = client.update_sensors()
            client.send(sensor_parse)
        if not (now - start) % worker_interval:
            worker_parse = client.update_workers()
            client.send(worker_parse)
        time.sleep(1)


if __name__ == '__main__':

    pool = ThreadPoolExecutor(max_workers=100)
    sim1 = pool.submit(
        simulate,
        Client_generator(
            11, 22, 1,
            [Sensor(1, 0.3, 0.2), Sensor(2, 0.4, 0.1)],
            [Worker(1, 1, 1, 3), Worker(2, 2, 2, 4)]))
    sim2 = pool.submit(
        simulate,
        Client_generator(
            11, 22, 2,
            [Sensor(3, 0.3, 0.2), Sensor(4, 0.4, 0.1)],
            [Worker(3, 1, 1, 3), Worker(4, 2, 2, 4)]))
    # sim3 = pool.submit(simulate, Client_generator(11,22,3,[Sensor(3,0.3,0.2),Sensor(4,0.4,0.1)],[Worker(3,1,1,3),Worker(4,2,2,4)]))
    # sim4 = pool.submit(simulate, Client_generator(11,22,4,[Sensor(3,0.3,0.2),Sensor(4,0.4,0.1)],[Worker(3,1,1,3),Worker(4,2,2,4)]))
    # sim5 = pool.submit(simulate, Client_generator(11,22,5,[Sensor(3,0.3,0.2),Sensor(4,0.4,0.1)],[Worker(3,1,1,3),Worker(4,2,2,4)]))

    # pool.shutdown()
