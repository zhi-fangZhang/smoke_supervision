'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-10 23:01:16
LastEditTime: 2023-01-10 23:07:03
'''
from client_upload import Client_generator, Sensor, Worker, simulate

if __name__ == '__main__':
    simulate(Client_generator(
            11, 22, 1,
            [Sensor(1, 0.3, 0.2), Sensor(2, 0.4, 0.1)],
            [Worker(1, 1, 1, 3), Worker(2, 2, 2, 4)]))