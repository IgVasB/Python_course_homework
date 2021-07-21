my_list=[]
my_list.append(1)
to_be=True;
my_list.append(to_be)
my_list.append(3.14)
my_list.append([1, 3.14,'charm'])
my_list.append(('l',2,'hj'))
my_list.append({'dict': 1, 'dictionary': 2})
print('имеем список', my_list, 'со следующим типом данных:')
i=0
while i<len(my_list):
    print(my_list[i],type(my_list[i]))
    i+=1
