n = abs(int(input('Введите натуральное число n\n'))) # гарантируется получение натурального числа
n=str(n)
len_n = len(n)
maxim = 0
i = 0
while i < len_n:
    if int(n[i]) > maxim:
        maxim = int(n[i])
    i=i+1
print('Максимальная цифра в числе: ', maxim)