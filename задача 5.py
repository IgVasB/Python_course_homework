print('Вводите строки чисел, разделенных пробелом.'
      ' Числа будут суммироваться с ранее введенными числами.')
print('После получения не числа в строке суммирование прекращается.')
print('Все числа после этого символа будут проигнорированы.')

def summ(my_str):
    ex = True # переменная для определения, что в строке есть не число
    my_str = my_str.split()
    s=0
    for el in my_str:
        try:    # обрабатывваем исключение - в строке найдено не число
            s=s+float(el)
        except ValueError:
            ex = False
            return s,ex
    return s,ex

continue_enter = True
sum_enter=0
while continue_enter: # цикл ввода строк пользователем
    res_calc = summ(input())
    sum_enter=sum_enter+res_calc[0] # это сумма всех чисел со всех введенных строк
    continue_enter = res_calc[1] # это признак ввода не числа
    print(sum_enter)