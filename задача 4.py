def my_func_1(x,y):
    return x**y

def my_func_2(x,y):
    m=1
    for i in range(abs(y)):
        m=m*x
    return 1/m

print(my_func_1(2,-2),my_func_2(2,-2))