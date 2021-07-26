# def div(a,b):
#     if b==0:
#         c='деление на ноль'
#     else:
#         c=a/b
#     return c

def div(a,b):
    try:
        c = a/b
    except ZeroDivisionError:
        return 'деление на 0'
    return c

del_1 = float(input('Введите делимое: '))
del_2 = float(input('Введите делитель: '))
print('Результат деления: ', div(del_1, del_2))