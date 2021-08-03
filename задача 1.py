print('Записываем файл. Пустая строка - конец записи')
f = open("задача 1.txt", 'w')
user_str=input()
while user_str!='':
    f.write(user_str+'\n')
    user_str=input()
f.close()