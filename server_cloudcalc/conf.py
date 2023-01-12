'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-12 13:46:56
LastEditTime: 2023-01-12 17:25:51
'''

DETECT_INTERVAL = 4 * 60
INTERVAL_TO_YEAR = DETECT_INTERVAL / (60 * 60 * 24 * 365)

USER = 'root'
PASSWORD = '1234aA'
HOST_IP = '39.108.120.233'
DATABASE = 'DUST'
MYSQL_PORT = 3306
CHARSET = 'utf8mb4'

SMOKE_STANDARD_CN = {
    'concentration_extreme_range_still': [0, 3.5],  # mg/m3
    'concentration_extreme_range_mobile': [0, 2.5],  # mg/m3
    'temperature_extreme_range': [2, 28],  # ℃
    'humidity_extreme_range': [20, 100]  # %
}
spatial_threshold = 100
safety_threshold = [897.3, 30]
