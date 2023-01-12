'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 00:26:06
LastEditTime: 2023-01-12 14:31:09
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

    '''
    暂时解析成字符串

    例子：
    [s fid]/id&conc&temp&hum/1&12&13&14/2&13&15&89/3&89&45&12/[s]
    [w fid]/id&x&y/1&12&13/2&13&15/3&89&45/[w]
    '''

    def encrypt(self, mode='s'):
        out = '/{}{}'.format(mode, self.f_id)
        if mode == 's':
            for sensor in self.sensors:
                out = out + '/{}&{}&{}&{}'.format(
                    sensor.id, sensor.concentration, sensor.temperature,
                    sensor.humidity)
        elif mode == 'w':
            for worker in self.workers:
                out = out + '/{}&{}&{}'.format(worker.id, worker.x, worker.y)
        out += '[SPLIT]'
        return out

    def update_workers(self):
        for worker in self.workers:
            worker.traj_gen(self)
            return self.encrypt('w')

    def update_sensors(self):
        for sensor in self.sensors:
            sensor.env_gen()
            return self.encrypt('s')
