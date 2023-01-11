'''
Description:
version: 
Author: Zhang Zhifang
Date: 2023-01-10 00:04:21
LastEditTime: 2023-01-10 14:06:48
'''

import math


class Smoke:
    def __init__(self, id, f_id, time, conc, temp, hum) -> None:
        self.f_id = f_id
        self.id = id
        self.time = time
        self.conc = conc
        self.temp = temp
        self.hum = hum

    '''
    待解决！
    '''

    def is_overrich(self):
        # 计算危险指数
        self.content = self.conc + self.hum
        # 判断是否危险
        return True
        if not self.id % 2:
            return True
        return False

    def __gt__(self, other):
        return self.content > other.content


class Miner:
    def __init__(self, id, f_id, time, x, y) -> None:
        self.f_id = f_id
        self.id = id
        self.time = time
        self.x = x
        self.y = y


class Miner_insist(Miner):
    def __init__(
        self,
        id,
        f_id,
        former_total_dust,
        st_traj,
    ) -> None:
        super(Miner_insist, self).__init__(id, f_id, time=-1, x=-1, y=-1)
        # [(t1,x1,y1),(t2,x2,y2)]
        self.traj = st_traj
        self.former_total_dust = former_total_dust

    # smoke_record: [(t1,conc1,x1,y1),(t2,conc2,x2,y2)]
    def get_history_dust_now(self, smoke_record):
        # 位置阈值
        spatial_threshold = 100
        for item in self.traj:
            f = lambda distance: math.log2(math.sqrt(10 - distance)
                                           ) if distance < 10 else 0
            distances = [
                math.sqrt((item[1] - sr[2])**2 + (item[2] - sr[3])**2)
                for sr in smoke_record
            ]
            # 增量
            return list(map(f, distances))

    def get_total_dust_now(self, smoke_record):
        # 增量+存量
        return sum(
            self.get_history_dust_now(smoke_record)) + self.former_total_dust

    def get_antipate_dust(self, smoke_record):
        # history = self.get_history_dust_now(
        #     smoke_record) + self.get_total_dust_now(smoke_record)
        # 未解决，用数模预测一下！
        return 1

    def is_danger(self, smoke_record):
        safety_threshhold = 100
        anti = self.get_antipate_dust(smoke_record)
        if anti > safety_threshhold: return True
        return False
