def spl(user_str): #если строка начинается с числа, выдает это число; если нет, то 0
    s=''
    for el in user_str:
        if el.isnumeric():
            s=s+el
        else:
            if s=='':
                s='0'
            break
    return int(s)

my_dict=dict() # создаем пустой словарь
f=open("задача 6.txt",'r', encoding='utf-8')
for line in f: #считываем построчно файл
    data = line.split() #делаем из строки список, разделяя по пробелам
    name = data[0] #это название предмета
    lessons = 0 # Это сумма всех занятий по предмету
    for el in data:
        lessons = lessons+spl(el) # вычисляем сумму всех занятий
    my_dict.update({name:lessons}) #добавляем предмет с количеством занятий в словарь
f.close()
print(my_dict)