'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 00:25:54
LastEditTime: 2023-01-12 10:36:23
'''
import random
import configparser

cp = configparser.ConfigParser()
cp.read('my.ini')
SMOKE_STANDARD = cp.get('sensor', 'SMOKE_STANDARD')

class Sensor:

    stc_standard = SMOKE_STANDARD

    def __init__(self,id, x_ratio, y_ratio):
        self.id=id
        self.x_ratio = x_ratio
        self.y_ratio = y_ratio
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