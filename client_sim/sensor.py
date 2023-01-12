'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 00:25:54
LastEditTime: 2023-01-12 12:10:16
'''
import random
import configparser

import conf
SMOKE_STANDARD = conf.SMOKE_STANDARD

class Sensor:

    stc_standard = SMOKE_STANDARD

    def __init__(self,id, x, y):
        self.id=id
        self.x = x
        self.y = y
        self.env_gen()  # 初始化 self.concentration, self.temperature, self.humidity


    '''
    生成烟尘浓度 温度 湿度
    '''

    def env_gen(self):
        conc, temp, hum = self.stc_standard[
            'concentration_extreme_range'], self.stc_standard[
                'temperature_extreme_range'], self.stc_standard[
                    'humidity_extreme_range']

        self.concentration = random.uniform(conc[0], conc[1])
        self.temperature = random.uniform(temp[0], temp[1])
        self.humidity = random.uniform(hum[0], hum[1])