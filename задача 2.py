sec_total=int(input('Введите время в секундах: '))
# вычисляем часы, минуты, секунды
hour = sec_total // 3600
sec_div = sec_total % 3600
minutes = sec_div // 60
sec = sec_div % 60
# --- преобразуем часы, минуты и секунты в строки формата ЧЧ, ММ, СС добавлением 0, если необходимо
if sec>9:
    sec=str(sec)
else:
    sec='0'+str(sec)

if minutes>9:
    minutes=str(minutes)
else:
    minutes='0'+str(minutes)

if hour > 9:
    hour = str(hour)
else:
    hour = '0' + str(hour)

print(f'Время в формате "чч:мм:сс": {hour}:{minutes}:{sec}')