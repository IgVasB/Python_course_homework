f=open("задача 3.txt",'r', encoding='utf-8')
staff_num=0
staff_salary=0
print('Зарплата меньше 20000 у следующих сотрудников:')
for line in f:
    staff_num+=1
    data = line.split()
    name = data[0]
    salary = float(data[1])
    staff_salary+=salary
    if salary < 20000:
        print(name)
print('Средняя зарплата:  %.2f' % (staff_salary/staff_num))
f.close()