
import time
import random
import conf


SMOKE_STANDARD = conf.SMOKE_STANDARD

class Simulator:

    def __init__(self,factory,sender) -> None:
        self.factory=factory
        self.sender=sender

    '''
    生成烟尘浓度 温度 湿度
    '''    
    def env_gen(self):
        for sensor in self.factory.sensors:
            conc, temp, hum = conf.SMOKE_STANDARD[
                'concentration_extreme_range'], conf.SMOKE_STANDARD[
                    'temperature_extreme_range'], conf.SMOKE_STANDARD[
                        'humidity_extreme_range']

            sensor.concentration = random.uniform(conc[0], conc[1])
            sensor.temperature = random.uniform(temp[0], temp[1])
            sensor.humidity = random.uniform(hum[0], hum[1])
        return self.factory.sensors
    
    
    '''
    根据speed,x,y生成一组新的x,y
    '''

    def traj_gen(self):
        for worker in self.factory.workers:
            key = random.randint(0, 5)
            if key == 0:
                worker.x += worker.speed
            elif key == 1:
                worker.y += worker.speed
            elif key == 2:
                worker.x -= worker.speed
            elif key == 3:
                worker.y -= worker.speed
            else:
                pass

            if worker.x > self.factory.x_max: worker.x = self.factory.x_max - 1
            if worker.y > self.factory.y_max: worker.y = self.factory.y_max - 1
            if worker.x < self.factory.x_min: worker.x = self.factory.x_min + 1
            if worker.y < self.factory.y_min: worker.y = self.factory.y_min + 1
        return self.factory.workers
        

    
    def simulate(self):
        sensor_interval = conf.SENSOR_INTERVAL
        worker_interval = conf.WORKER_INTERVAL
        start = int(time.time())
        while True:
            now = int(time.time())
            if not (now - start) % sensor_interval:
                sensors=self.env_gen()
                self.sender.send(sensors,'s')
            if not (now - start) % worker_interval:
                workers=self.traj_gen()
                self.sender.send(workers,'w')
            time.sleep(conf.SIMULATE_PAUSE)
