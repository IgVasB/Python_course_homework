my_dict={'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
f=open("задача 4.txt",'r', encoding='utf-8')
f_1=open("задача 4_1.txt",'w', encoding='utf-8')
for line in f:
    data = line.split()
    my_str = line.replace(data[0],my_dict.get((data[0])))
    f_1.write(my_str)
f.close()
f_1.close()