class List_Num_Validate(Exception):
    def __init__(self, txt):
        self.txt = txt

print('Создаем список из чисел. СТОП - конец ввода.')
list_of_numbers = []
while True:
    try:
        str = input('Введите число: ')
        if str == 'СТОП':
            break
        try:
            a = float(str)
        except ValueError:
            raise List_Num_Validate('Вы ввели не число!')
    except List_Num_Validate as err:
        print(err)
    else: list_of_numbers.append(float(str))

print(list_of_numbers)
