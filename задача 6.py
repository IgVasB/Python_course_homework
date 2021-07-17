import math
a = float(input('Пробег в 1ый день, км: '))
b = float(input('Пробег в n-ый день (не менее), км: '))
print('Будет достигнут на', 1+math.trunc(1+math.log(b/a,1.1)), 'день')