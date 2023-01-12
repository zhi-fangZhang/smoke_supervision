'''
Description:
version: 
Author: Zhang Zhifang
Date: 2023-01-10 00:04:21
LastEditTime: 2023-01-13 01:39:25
'''

import math
import conf


class Smoke:
    def __init__(self, id, f_id, time, conc, temp, hum) -> None:
        self.f_id = f_id
        self.id = id
        self.time = time
        self.content = conc
        self.temp = temp
        self.hum = hum

    def is_overrich(self):
        max_still_conc = conf.SMOKE_STANDARD_CN[
            'concentration_extreme_range_still'][1]
        range_temp = conf.SMOKE_STANDARD_CN[
            'concentration_extreme_range_still']
        if self.content > max_still_conc or self.content not in [range_temp]:
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
    def get_detected_dust(self, smoke_record):
        # 位置阈值
        for item in self.traj:
            f = lambda x: (conf.spatial_threshold * x[1]
                           ) * conf.INTERVAL_TO_YEAR if x[
                               0] < conf.spatial_threshold else 0
            record = [[
                math.sqrt((item[1] - sr[2])**2 + (item[2] - sr[3])**2), sr[1]
            ] for sr in smoke_record]
            # 增量
            return sum(list(map(f, record)))

    def get_current_dust(self, smoke_record):
        # 增量+存量
        return self.get_detected_dust(smoke_record) + self.former_total_dust

    def get_antipate_dust(self, smoke_record):
        return self.former_total_dust + self.get_current_dust(smoke_record)
        # alternative: polyfit

    def is_danger(self, smoke_record):
        anti = self.get_antipate_dust(smoke_record)  #总量
        acc = self.get_detected_dust(smoke_record)
        if anti > conf.safety_threshold[0] or acc > conf.safety_threshold[1]:
            return True
        return False
