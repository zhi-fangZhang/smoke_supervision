'''
Description: 
version: 
Author: Zhang Zhifang
Date: 2023-01-09 23:41:47
LastEditTime: 2023-01-12 14:54:07
'''
import utils
import conf

'''
检测记录是否有粉尘危害超限的情况
'''


def check_overrich(cursor):
    sql = '''select * from sensor_spvs 
        WHERE UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(time)<={} ORDER BY id ASC,f_id ASC;
    '''.format(conf.DETECT_INTERVAL)
    smokes = utils.operate(cursor, sql, 'ss')
    alert_smokes = list(filter(lambda smoke: smoke.is_overrich(), smokes))
    if len(alert_smokes) > 0:
        # 根据id 和 f_id 将列表分组,并取每组的最大危险值
        temp = utils.group_by_key(alert_smokes,
                                  lambda smoke: [smoke.id, smoke.f_id])
        alert_smokes = list(map(max, temp))
        # 将危险值存入数据库
        for smoke in alert_smokes:
            alert = [str(smoke.id), str(smoke.f_id), str(smoke.content)]
            sql = 'INSERT INTO sensor_alert(id,f_id,content) VALUES ({},{},{})'.format(
                *alert)
            utils.operate(cursor, sql, 'as')
