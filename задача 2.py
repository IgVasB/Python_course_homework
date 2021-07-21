print('Сейчас мы создадим список. Вводите элементы. Когда закончите, наберите "всё"')
my_list=[]
inp = input()
while inp != 'всё':
    my_list.append(inp)
    inp = input()
print('Вот такой список получился: ', my_list)
i=0
len_my_list = len(my_list)-1
while i<len_my_list:
    a=my_list[i]
    my_list[i]=my_list[i+1]
    my_list[i+1]=a
    i+=2
print('И теперь мы пошалили со списком, исковеркав его: ', my_list)

