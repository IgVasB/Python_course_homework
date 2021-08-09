class Matrix:
    def __init__(self,cell):
        self.cell = cell
        len_list2d = len(self.cell[0])
        for i in self.cell: # проверяем, все ли строки одинаковой длины; нет - получаем пустоту
            if len(i)!=len_list2d:
                self.cell=[]
                print('Строки разной длины!')
                break

    def __str__(self):
        sum_str=''
        def str_mod(lst): # функция преобразует список в строку (join() не годится - работает со строковыми списками)
            res=''
            for i in lst:
                res = res + str(i) +' '
            return res[:-1]
        for my_list in self.cell:
            sum_str=sum_str+str_mod(my_list)+'\n'
        return sum_str[:-1]

    def __add__(self, other):
        result = []
        def sum(list_1,list_2): # функция суммирует два списка поэлементно
            s=[]
            for i,j in zip(list_1,list_2):
                s.append(i+j)
            return s
        for i,j in zip(self.cell, other.cell):
            result.append(sum(i,j))
        return Matrix(result)


a = [[1,2,100],[1,2,10]]
b = [[-1,-2,-100],[-1,-2,-10]]
A = Matrix(a)
B = Matrix(b)
print('матрица A:')
print(A)
print('матрица B:')
print(B)
print('матрица А+B:')
print(A+B)