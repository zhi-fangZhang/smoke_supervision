'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-10 01:25:25
LastEditTime: 2023-01-12 16:58:37
'''
import utils
import beans
import conf


def get_smoke_record(cursor):
    # smoke_record: [(t1,conc1,x1,y1),(t2,conc2,x2,y2)]
    sql = '''
    SELECT time,concentration,x,y 
    FROM sensor_info NATURAL JOIN sensor_spvs 
    where UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(time)<={}
    ORDER BY sensor_info.id ASC,sensor_info.f_id ASC;
    '''.format(conf.DETECT_INTERVAL)
    return utils.operate(cursor, sql, 'sr')


def get_former_total_dust(cursor, id, f_id):
    sql = '''
    SELECT accumulate_dust FROM worker_alert 
    WHERE id={} and f_id={}
    ORDER BY time DESC
    LIMIT 1
    '''.format(id, f_id)
    return utils.operate(cursor, sql, 'sr')[0][0]


def check_dust(cursor):
    smoke_record = get_smoke_record(cursor)
    #接尘总量，预期接尘量被动
    sql = '''
    select * from worker_pos where UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(time)<={} ORDER BY id ASC,f_id ASC;
    '''.format(conf.DETECT_INTERVAL)
    miners = utils.operate(cursor, sql, 'sm')
    temp = utils.group_by_key(miners, lambda miner: [miner.f_id, miner.id])
    for lis in temp:
        # routine
        traj = [(item.time, item.x, item.y) for item in lis]
        id, f_id = lis[0].id, lis[0].f_id
        former_dust = get_former_total_dust(cursor, id, f_id)
        # 分组后生成一个持久工人模型
        mi = beans.Miner_insist(id, f_id, former_dust, traj)
        total_dust_now = mi.get_total_dust_now(smoke_record)
        anticipated_dust = mi.get_antipate_dust(smoke_record)
        total_dust_now = total_dust_now
        is_danger = int(mi.is_danger(smoke_record))
        # 上传worker_alert数据库
        sql = 'INSERT INTO worker_alert(id,f_id,accumulate_dust,anticipated_dust,is_danger) VALUES ({},{},{},{},{});'.format(
            id, f_id, total_dust_now, anticipated_dust, is_danger)
        utils.operate(cursor, sql)
