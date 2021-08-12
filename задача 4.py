class Storage:
    pass

class Equipment:
    def __init__(self, eq_type, brand, model, count):
        self.eq_type = eq_type
        self.brand = brand
        self.model = model
        self.count = count

class Printer(Equipment):
    #printer_type - лазерный или струйный
    def __init__(self, eq_type, brand, model, count, printer_type):
        super().__init__(eq_type, brand, model, count)
        self.printer_type = printer_type

class Computer(Equipment):
    #computer_type - стационарный или ноутбук
    def __init__(self, eq_type, brand, model, count, computer_type):
        super().__init__(eq_type, brand, model, count)
        self.computer_type = computer_type

class Xerox(Equipment):
    #xerox_type - форматы: А4,А3,A2,A1
    def __init__(self, eq_type, brand, model, count, xerox_type):
        super().__init__(eq_type, brand, model, count)
        self.xerox_type = xerox_type


shipment_1 = Printer('printer', 'EPSON', 'EP-101', 120, 'laser')
print(shipment_1.eq_type)
shipment_2 = Computer('computer', 'ASUS', 'ASUS-5477', 15, 'notebook')
print(shipment_2.brand)
shipment_3 = Xerox('xerox', 'CANON', 'CANON-E200', 45, 'A1')
print(shipment_3.xerox_type)