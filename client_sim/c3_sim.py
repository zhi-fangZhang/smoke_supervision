'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-10 23:01:16
LastEditTime: 2023-01-13 00:59:26
'''
from simulator import Simulator
from register import Register
from sender import Sender


if __name__ == '__main__':
    Simulator(Register().register_i(2),Sender()).simulate()