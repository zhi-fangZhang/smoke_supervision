'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-13 01:15:21
LastEditTime: 2023-01-13 01:34:42
'''

from uploader import Uploader
from watcher import Watcher
import threading

class Superviser:
    def __init__(self) -> None:
        self.watcher=Watcher()
        self.uploader=Uploader()


    def transfer(self,new_client_socket):
        conn=self.uploader.conn
        conn.cursor().execute('USE DUST;')
        conn.commit()
        while True:
            recv_date = new_client_socket.recv(1024)
            if recv_date:
                lock = threading.Lock()
                lock.acquire()
                str = recv_date.decode("utf-8")
                self.uploader.upload(str)
                lock.release()
            else:
                break
        new_client_socket.close()
        conn.close()
    
    def run(self):
        self.watcher.socket_watch(self.transfer)


