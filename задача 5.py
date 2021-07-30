from functools import reduce
my_list=[el for el in range(100,1001) if (el % 2 == 0)]
def calc(a,b):
    return a*b
print(reduce(calc,my_list))