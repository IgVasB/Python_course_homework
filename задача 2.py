# Не понял задание. Ведь есть стандартное исключение ZeroDivisionError!
# Требуется переопределить его? Или что?
# Сделал по стандартному шаблону из лекции/методички

class Div_By_Zero(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    dividend = float(input("Введите делимое: "))
    divisor = float(input("Введите делитель: "))
    if divisor == 0:
        raise Div_By_Zero("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число!")
except Div_By_Zero as err:
    print(err)
else:
    print(f"Результат деления: {dividend/divisor}")
