import time

class Trafficlight:
    __color = {'красный':7,'желтый':2,'зеленый':10}

    def running(self):
        for col in Trafficlight.__color:
            print(f'Горит {col} в течении {Trafficlight.__color.get(col)} сек')
            time.sleep(float(Trafficlight.__color.get(col)))

sign = Trafficlight()
sign.running()