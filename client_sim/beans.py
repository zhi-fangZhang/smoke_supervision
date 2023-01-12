'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 00:26:06
LastEditTime: 2023-01-13 00:43:44
'''
'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 00:26:06
LastEditTime: 2023-01-08 00:38:48
'''


class Factory:
    def __init__(self, x_max, y_max, f_id, sensors, workers):
        self.x_max = x_max
        self.y_max = y_max
        self.x_min = 0
        self.y_min = 0
        self.f_id = f_id
        self.sensors = sensors
        self.workers = workers

class Worker:
    def __init__(self,f_id, id, x_init, y_init, speed):
        self.f_id=f_id
        self.id = id
        self.x = x_init
        self.y = y_init
        self.speed = speed
        return

class Sensor:
    def __init__(self,f_id,id, x, y):
        self.f_id=f_id
        self.id=id
        self.x = x
        self.y = y
