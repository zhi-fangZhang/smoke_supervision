'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-10 23:01:20
LastEditTime: 2023-01-10 23:03:19
'''



from client_upload import Client_generator,Sensor,Worker,simulate



if __name__ == '__main__':
    simulate(Client_generator(
            11, 22, 2,
            [Sensor(3, 0.3, 0.2), Sensor(4, 0.4, 0.1)],
            [Worker(3, 1, 1, 3), Worker(4, 2, 2, 4)]))