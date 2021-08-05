class Worker:
    def __init__(self,name,surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
    def get_income(self):
        return self._income

class Position(Worker):
    def get_full_name(self):
        return self.name+' '+self.surname
    def get_total_income(self):
        return self.get_income()['wage']+self.get_income()['bonus']

Oleg_income = {'wage': 25000, 'bonus': 5000}
Oleg = Position('Олег','Николаев', 'грузчик', Oleg_income)
print(Oleg.name)
print(Oleg.surname)
print(Oleg.position)
print(Oleg.get_full_name(), Oleg.get_total_income())