'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-13 01:05:48
LastEditTime: 2023-01-13 01:33:59
'''
import conf
import socket
import threading

class Watcher:
    def __init__(self) -> None:
        self.server_init()


    '''
    服务器接收信息
    初始化监听socket
    '''


    def server_init(self,ip=conf.DISTRIBUTION_IP):
        self.socket_tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_tcp_server.bind((ip, conf.LISTEN_PORT))
        self.socket_tcp_server.listen(conf.MAX_LINK)


    '''
    轮询监听新的客户端连接
    '''


    def socket_watch(self,hook):
        while True:
            new_client_socket, client_addr = self.socket_tcp_server.accept()
            client1_threading = threading.Thread(target=hook,
                                                args=(new_client_socket,))
            client1_threading.setDaemon(True)
            client1_threading.start()


    

