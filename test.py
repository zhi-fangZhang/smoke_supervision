'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-09 00:22:36
LastEditTime: 2023-01-09 22:55:27
'''

from server.upload.server_run import encrypt_parse
from server.upload.server_run import upload_sensor_spvs

if __name__ == '__main__':
    str='/s1/1&12&13&14/2&13&15&89/3&89&45&12'
    mode,info=encrypt_parse(str)
    sql=upload_sensor_spvs(info)

