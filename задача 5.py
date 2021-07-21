rating=[100,10,7,7,5,4,3,2,2]
print('Это рейтинг:', rating)
print('Введите элемент рейтинга - натуральное число. Отрицательное число - конец ввода.')
new=int(input())
while new>=0:
    length_rating=len(rating)
    i=0
    while i<length_rating:
        if new>rating[i]:
            rating.insert(i,new)
            break;
        i+=1
    if i==length_rating:
        rating.append(new)
    print('Рейтинг обновлен: ', rating)
    new = int(input('Ведите новый элемент: '))