'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-08 01:54:23
LastEditTime: 2023-01-09 22:50:42
'''
import socket
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import server_run
'''
服务器接收信息
'''
'''
初始化监听socket
'''


def server_init(ip='127.0.0.1'):
    socket_tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tcp_server.bind((ip, 8080))
    socket_tcp_server.listen(5)
    return socket_tcp_server


'''
轮询监听新的客户端连接
'''


def socket_watch(socket_tcp_server, pool):

    while True:
        new_client_socket, client_addr = socket_tcp_server.accept()
        client1_threading = threading.Thread(target=server_run.run,
                                             args=(new_client_socket,))
        client1_threading.start()


if __name__ == '__main__':
    socket_tcp_server = server_init()
    pool = ThreadPoolExecutor(max_workers=100)
    client1_threading = threading.Thread(target=socket_watch,
                                         args=(socket_tcp_server, pool))
    client1_threading.start()
    time.sleep(1)
