print('Создание каталога товаров на складе.')
products=[]
i=0
print('Оформляем товар №', i + 1)
name = input('Введите название товара: ')
while name != 'стоп':
    price = input('Введите цену товара, руб: ')
    num = input('Введите количество товара: ')
    unit = input('Введите единицу измерения товара: ')
    products.append((i+1,{'название':name,'цена':price,'количество':num,'ед':unit}))
    i+=1
    print('Текущий каталог товаров: ')
    for n in range(len(products)): # выводим каталог товаров
        print(products[n])
    print('Оформляем товар №', i + 1)
    name=input('Введите название товара: ')

#-------------------------------------------------------------------
print('Немного аналитики по получившемуся каталогу...')
name=[]
price=[]
num=[]
unit=[]
for n in range(len(products)):
    name.append(products[n][1].get('название'))
    price.append(products[n][1].get('цена'))
    num.append(products[n][1].get('количество'))
    unit.append(products[n][1].get('ед'))
analys={'название':name,'цена':price,'количество':num,'ед':unit}
for n in analys.keys():
    print(n,':', analys[n])

