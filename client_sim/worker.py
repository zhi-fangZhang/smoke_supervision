'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2022-12-29 14:06:50
LastEditTime: 2023-01-12 10:38:21
'''
import numpy as np
import cv2
import random


class Worker:
    def __init__(self, id, x_init, y_init, speed):
        self.id = id
        self.x = x_init
        self.y = y_init
        self.speed = speed
        return

    '''
    根据speed,x,y生成一组新的x,y
    '''

    def traj_gen(self, factory):
        key = random.randint(0, 5)
        if key == 0:
            self.x += self.speed
        elif key == 1:
            self.y += self.speed
        elif key == 2:
            self.x -= self.speed
        elif key == 3:
            self.y -= self.speed
        else:
            pass

        if self.x > factory.x_max: self.x = factory.x_max-1
        if self.y > factory.y_max: self.y = factory.y_max-1
        if self.x < factory.x_min: self.x = factory.x_min+1
        if self.y < factory.y_min: self.y = factory.y_min+1

    '''
    生成工人轨迹图
    '''

    def print_map(self, factory):
        map = [[0] * (factory.x_max - factory.x_min + 1)
               for _ in range((factory.y_max - factory.y_min + 1))]
        map[self.x][self.y] = 255
        img = np.array(map, dtype=np.uint8)
        return img
