income = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))
if income > costs:
    print('Фирма работает с прибылью')
    print('Рентабельность - %.3f' % (1-costs/income))
else:
    print('Фирма не приносит доход')
staff = int(input('Введите число сотрудников фирмы: '))
print('Прибыль на одного сотрудника - %.3f' % ((income-costs)/staff))