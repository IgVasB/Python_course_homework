from itertools import count, cycle
print('Скрипт с итератором count')
start=int(input('Введите начальное целое число: '))
num=int(input('Введите сколько чисел генерировать: '))
end=start+num-1
for el in count(start):
    if el > end:
        break
    else:
        print(el)

print('Скрипт с итератором cycle')
num=int(input('Сколько элементов вывести из бесконечного \
циклического списка "ABCDFABCDFABCDF...": '))-1
i = 0
for el in cycle("ABCDF"):
    if i > num:
        break
    print(el)
    i += 1
