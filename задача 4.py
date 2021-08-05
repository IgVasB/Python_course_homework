class Car:
    def __init__(self,name,color,speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print('Создан новый объект класса Car')

    def go(self):
        print(f'Автомобиль {self.name} начал движение со скоростью {self.speed} км/ч.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn(self,direction):
        print(f'Автомобиль {self.name} повернул {direction}.')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed} км/ч.')

class TownCar(Car):
    def  __init__(self,name,color,speed, is_police, type):
        super().__init__(name,color,speed,is_police)
        self.type = type
        print(f'Создан новый объект класса TownCar, тип - {type}')

    def show_type(self):
        print(f'Это автомобиль класса TownCar, тип - {self.type}')

    def show_speed(self, max_speed=60):
        print(f'Скорость автомобиля {self.name} - {self.speed} км/ч.')
        if self.speed > max_speed:
            print(f'Внимание! Превышение максимально допустимой скорости {max_speed} км/ч!')

class SportCar(Car):
    def  __init__(self,name,color,speed, is_police, racing_type):
        super().__init__(name,color,speed,is_police)
        self.racing_type = racing_type
        print(f'Создан новый объект класса SportCar')

    def show_racing_type(self):
        print(f'Это автомобиль класса SportCar для гонок {self.racing_type}')

class WorkCar(Car):
    def  __init__(self,name,color,speed, is_police, work_type):
        super().__init__(name,color,speed,is_police)
        self.work_type = work_type
        print(f'Создан новый объект класса WorkCar')

    def show_work_type(self):
        print(f'Это автомобиль класса WorkCar для работы {self.work_type}')

    def show_speed(self, max_speed = 40):
        print(f'Скорость автомобиля {self.name} - {self.speed} км/ч.')
        if self.speed > max_speed:
            print(f'Внимание! Превышение максимально допустимой скорости {max_speed} км/ч!')

class PoliceCar(Car):
    def  __init__(self,name,color,speed, is_police, police_type):
        super().__init__(name,color,speed,is_police)
        self.police_type = police_type
        print(f'Создан новый объект класса PoliceCar')

    def show_police_type(self):
        print(f'Это автомобиль класса PoliceCar для работы {self.police_type}')

авто_1 = Car("Шкода", "черный", 120, False)
print(авто_1.name, '', авто_1.color)
авто_1.go()
авто_1.turn("налево")
авто_1.show_speed()
авто_1.stop()

print('')
авто_2 = TownCar("Нефаз", "бело-синий", 60, False, 'автобус')
авто_2.show_type()
авто_2.go()
авто_2.turn("направо")
авто_2.show_speed()
авто_2.stop()

print('')
авто_3 = SportCar("McLaren", "бело-красный", 260, False, 'Формула 1')
авто_3.show_racing_type()
авто_3.go()
авто_3.stop()

print('')
авто_4 = WorkCar("Камаз", "красный", 60, False, 'автоцистерна')
авто_4.show_work_type()
print('Принадлежность полиции - ', авто_4.is_police)
авто_4.go()
авто_4.show_speed()
авто_4.stop()

print('')
авто_5 = PoliceCar("Ниссан", "бело-синий", 135, True, 'ДПС')
авто_5.show_police_type()
print('Принадлежность полиции - ', авто_5.is_police)
авто_5.go()
авто_5.turn("направо")
авто_5.show_speed()
авто_5.stop()