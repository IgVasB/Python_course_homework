class Data:
    max_year = 2200
    min_year = 1
    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def to_int(cls,input_list):
        data_list=input_list.split('-')
        res=[]
        for el in data_list:
            res.append(int(el))
        return res

    @staticmethod
    def validate(data_list): #проверять високосность года не будем
        res=''
        month_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if data_list[1] > 12 or data_list[1] < 1:
            res = 'Неверно задан месяц. \n'
            if data_list[0] < 1 or data_list[0] > 31:
                res = res + 'Неверно задан день. \n'
        else:
            if data_list[0] > month_day.get(data_list[1]) or data_list[0] < 1 or data_list[0] > 31:
                res = res + 'Неверно задан день. \n'
        if data_list[2] > Data.max_year or data_list[2] < Data.min_year:
            res = res + 'Неверно задан год. \n'
        if res == '':
            res = 'Дата задана корректно.'
        print(res)

print(f'год должен быть в диапазоне от {Data.min_year} до {Data.max_year} \n')

str = '29-02-2201'
print(str, Data.to_int(str))
Data.validate(Data.to_int(str))

str = '29-13-2201'
print(str, Data.to_int(str))
Data.validate(Data.to_int(str))

str = '32-13-2201'
print(str, Data.to_int(str))
Data.validate(Data.to_int(str))