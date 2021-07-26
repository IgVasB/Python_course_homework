def user_data(fst_name, snd_name, birthday, city, email, phone):
    return 'имя:'+str(fst_name)+' фамилия:'+str(snd_name)+' год рождения:'+str(birthday)+ \
           ' город:'+str(city)+' email:'+str(email)+' тел:'+str(phone)

print(user_data(fst_name='Глеб',snd_name='Жеглов',birthday=1902,city='Москва',\
                email='"МУР, до востребования"',phone='+7(495)694-94-70'))
