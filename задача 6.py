# Добавим в проект проверку, что количество товара должно быть числом.
class Storage:
    goods = []

    @classmethod
    def add_to_storage(cls,ex):
        exist = False
        for i, el in enumerate(Storage.goods):
            if ex == el: #тут функция равенства переопределена в классе Equipment
                Storage.goods[i].count = Storage.goods[i].count + ex.count
                exist = True
                break
        if not exist:
            Storage.goods.append(ex)

    @classmethod
    def remove_from_storage(self,ex):
        exist = False
        for i, el in enumerate(Storage.goods):
            if ex == el: #тут функция равенства переопределена в классе Equipment
                if Storage.goods[i].count > ex.count:
                    Storage.goods[i].count = Storage.goods[i].count - ex.count
                else:
                    if Storage.goods[i].count == ex.count:
                        Storage.goods.pop(i)
                        print('Этот товар на складе закончился!')
                    else:
                        print('На складе не хватает товара для отгрузки!')
                exist = True
                break
        if not exist:
            print('На складе нет такого товара!')

class Equipment:
    def __init__(self, eq_type, brand, model):
        self.eq_type = eq_type
        self.brand = brand
        self.model = model

    def __eq__(self, other): #тут определим, когда объекты класса равны друг другу
        if self.eq_type != other.eq_type:
            return False
        if self.brand != other.brand:
            return False
        if self.model != other.model:
            return False
        return True



class Printer(Equipment):
    #printer_type - лазерный или струйный
    def __init__(self, eq_type, brand, model, count, printer_type):
            super().__init__(eq_type, brand, model)
            self.printer_type = printer_type
            if type(count) != int:  # тут встроена проверка, что параметр count должен быть числом
                print('Количество товара должно быть числом! Будет указано кол-во товара - 0')
                self.count = 0
            else:
                self.count = count

    def __str__(self):
        return f'{self.eq_type}, {self.brand}, {self.model}, {self.count}, {self.printer_type}'


class Computer(Equipment):
    #computer_type - стационарный или ноутбук
    def __init__(self, eq_type, brand, model, count, computer_type):
            super().__init__(eq_type, brand, model)
            self.computer_type = computer_type
            if type(count) != int:  # тут встроена проверка, что параметр count должен быть числом
                print('Количество товара должно быть числом! Будет указано кол-во товара - 0')
                self.count = 0
            else:
                self.count = count

    def __str__(self):
        return f'{self.eq_type}, {self.brand}, {self.model}, {self.count}, {self.computer_type}'

class Xerox(Equipment):
    #xerox_type - форматы: А4,А3,A2,A1
    def __init__(self, eq_type, brand, model, count, xerox_type):
            super().__init__(eq_type, brand, model)
            self.xerox_type = xerox_type
            if type(count) != int:  # тут встроена проверка, что параметр count должен быть числом
                print('Количество товара должно быть числом! Будет указано кол-во товара - 0')
                self.count = 0
            else:
                self.count = count

    def __str__(self):
        return f'{self.eq_type}, {self.brand}, {self.model}, {self.count}, {self.xerox_type}'

print('На склад прибыла партия товара:')
shipment_1 = Printer('printer', 'EPSON', 'EP-101', 120, 'laser')
print(shipment_1)
Storage.add_to_storage(shipment_1)

print('Сейчас на складе:')
for el in Storage.goods:
    print(el)

print()

print('На склад прибыла партия товара:')
shipment_2 = Computer('computer', 'ASUS', 'ASUS-5477', 15, 'notebook')
print(shipment_2)
Storage.add_to_storage(shipment_2)

print('Сейчас на складе:')
for el in Storage.goods:
    print(el)

print()

print('На склад прибыла партия товара:')
shipment_3 = Xerox('xerox', 'CANON', 'CANON-E200', 45, 'A1')
print(shipment_3)
Storage.add_to_storage(shipment_3)

print('Сейчас на складе:')
for el in Storage.goods:
    print(el)

print()

print('На склад прибыла партия товара:')
shipment_4 = Computer('computer', 'ASUS', 'ASUS-5477', 20, 'notebook')
print(shipment_4)
Storage.add_to_storage(shipment_4)

print('Сейчас на складе:')
for el in Storage.goods:
    print(el)

print()

print('Пришел наряд на отгрузку партии товара:')
shipment_5 = Xerox('xerox', 'CANON', 'CANON-E200', 25, 'A1')
print(shipment_5)
print()

Storage.remove_from_storage(shipment_5)
print('Сейчас на складе:')
for el in Storage.goods:
    print(el)

print()

print('Пришел наряд на отгрузку партии товара:')
shipment_6 = Xerox('xerox', 'EPSON', 'EPSON-E4500', 25, 'A1')
print(shipment_6)
print()

Storage.remove_from_storage(shipment_6)
print('Сейчас на складе:')
for el in Storage.goods:
    print(el)

print()

print('Пришел наряд на отгрузку партии товара:')
print(shipment_1)
print()

Storage.remove_from_storage(shipment_1)
print('Сейчас на складе:')
for el in Storage.goods:
    print(el)

print()

shipment_7 = Printer('printer', 'EPSON', 'EPSON-E4500', '-dfgsd', 'A1')
print(shipment_7)
