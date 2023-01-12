'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-12 10:26:44
LastEditTime: 2023-01-13 00:54:21
'''

# 所有距离单位均为m,速度m/WORKER_INTERVAL(s)

REGISTER_DICT = [{
    'f_id':
    1,
    'name':
    'Yulin Mine',
    'address':
    '横山县石马坬',
    'latitude':
    38.28,
    'longitude':
    109.73,
    'length':
    300,
    'width':
    600,
    'note':
    '#',
    'workers_info': [{
        'id': 1,
        'name': '韶芃',
        'note': '#',
        'speed': 20
    }, {
        'id': 2,
        'name': '于涵蕾',
        'note': '#',
        'speed': 10
    }],
    'sensors_info': [{
        'id': 1,
        'x': 10,
        'y': 20,
        'note': ''
    }, {
        'id': 2,
        'x': 200,
        'y': 100,
        'note': ''
    }, {
        'id': 3,
        'x': 80,
        'y': 500,
        'note': ''
    }]
}, {
    'f_id':
    2,
    'name':
    'Pingshuo Mine',
    'address':
    '山西朔州市区',
    'latitude':
    39.33,
    'longitude':
    112.43,
    'length':
    400,
    'width':
    700,
    'note':
    '#',
    'workers_info': [{
        'id': 1,
        'name': '越妙之',
        'note': '#',
        'speed': 20
    }, {
        'id': 2,
        'name': '漆璞瑜',
        'note': '#',
        'speed': 5
    }, {
        'id': 3,
        'name': '矫妙梦',
        'note': '#',
        'speed': 10
    }, {
        'id': 4,
        'name': '仲浩壤',
        'note': '#',
        'speed': 7
    }],
    'sensors_info': [{
        'id': 1,
        'x': 100,
        'y': 200,
        'note': ''
    }, {
        'id': 2,
        'x': 300,
        'y': 600,
        'note': ''
    }, {
        'id': 3,
        'x': 200,
        'y': 300,
        'note': ''
    }, {
        'id': 4,
        'x': 150,
        'y': 400,
        'note': ''
    }]
}, {
    'f_id':
    3,
    'name':
    'Liyuan Dam Mine',
    'address':
    '横山县石马坬',
    'latitude':
    29.0,
    'longitude':
    106.6,
    'length':
    500,
    'width':
    700,
    'note':
    '#',
    'workers_info': [{
        'id': 1,
        'name': '田浩辰',
        'note': '#',
        'speed': 5
    }, {
        'id': 2,
        'name': '张志方',
        'note': '#',
        'speed': 5
    }, {
        'id': 3,
        'name': '吴杰',
        'note': '#',
        'speed': 10
    }, {
        'id': 4,
        'name': '锺离奇',
        'note': '#',
        'speed': 7
    }],
    'sensors_info': [{
        'id': 1,
        'x': 100,
        'y': 200,
        'note': ''
    }, {
        'id': 2,
        'x': 300,
        'y': 600,
        'note': ''
    }, {
        'id': 3,
        'x': 10,
        'y': 100,
        'note': ''
    }, {
        'id': 4,
        'x': 400,
        'y': 10,
        'note': ''
    }]
}, {
    'f_id':
    4,
    'name':
    'Huolin River Mine',
    'address':
    '内蒙通辽市',
    'latitude':
    43.62,
    'longitude':
    122.27,
    'length':
    600,
    'width':
    900,
    'note':
    '#',
    'workers_info': [{
        'id': 1,
        'name': '牢浩慨',
        'note': '#',
        'speed': 20
    }, {
        'id': 2,
        'name': '偶翠阳',
        'note': '#',
        'speed': 5
    }, {
        'id': 3,
        'name': '崔琴韵',
        'note': '#',
        'speed': 10
    }, {
        'id': 4,
        'name': '松青',
        'note': '#',
        'speed': 7
    }],
    'sensors_info': [{
        'id': 1,
        'x': 100,
        'y': 200,
        'note': ''
    }, {
        'id': 2,
        'x': 300,
        'y': 400,
        'note': ''
    }, {
        'id': 3,
        'x': 500,
        'y': 700,
        'note': ''
    }]
}]

SMOKE_STANDARD = {
    'concentration_extreme_range': [0, 5],  # mg/m3
    'temperature_extreme_range': [2, 30],  # ℃
    'humidity_extreme_range': [30, 100]  # %
}

SENSOR_INTERVAL = 3  # 单位s
WORKER_INTERVAL = 3 * 60  # 单位s
SIMULATE_PAUSE = 1  # 单位s
DISTRIBUTION_IP = '127.0.0.1'
DISTRIBUTION_PORT = 8080



USER='root'
PASSWORD='1234aA'
HOST_IP='39.108.120.233'
DATABASE='DUST'
MYSQL_PORT=3306
CHARSET='utf8mb4'