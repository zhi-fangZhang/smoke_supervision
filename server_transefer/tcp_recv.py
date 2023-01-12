'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 01:54:23
LastEditTime: 2023-01-12 13:45:51
'''
import socket
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import server_run
import conf
'''
服务器接收信息
'''
'''
初始化监听socket
'''


def server_init(ip=conf.DISTRIBUTION_IP):
    socket_tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tcp_server.bind((ip, conf.LISTEN_PORT))
    socket_tcp_server.listen(conf.MAX_LINK)
    return socket_tcp_server


'''
轮询监听新的客户端连接
'''


def socket_watch(socket_tcp_server, pool):
    while True:
        new_client_socket, client_addr = socket_tcp_server.accept()
        client1_threading = threading.Thread(target=server_run.run,
                                             args=(new_client_socket,))
        client1_threading.setDaemon(True)

        client1_threading.start()


def start():
    socket_tcp_server = server_init()
    pool = ThreadPoolExecutor(max_workers=conf.MAX_LINK)
    socket_watch(socket_tcp_server, pool)
