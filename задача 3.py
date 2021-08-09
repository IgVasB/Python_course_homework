class Cell:
    def __init__(self,n):
        self.n = n
        if self.n <=0:
            self.n = 0
            print('Появилась мертвая клетка. У нее 0 ячеек.')

    def __add__(self, other):
        return Cell(self.n+other.n)

    def __sub__(self, other):
        diff = self.n-other.n
        if diff > 0:
            return Cell(diff)
        else:
            print('клетка уничтожена')
            return Cell(0)

    def __mul__(self, other):
        mult = self.n*other.n
        if mult > 0:
            return Cell(mult)
        else:
            print('клетка уничтожена')
            return Cell(0)

    def __truediv__(self, other):
        divis = self.n//other.n
        if divis > 0:
            return Cell(divis)
        else:
            print('клетка уничтожена')
            return Cell(0)

    def __str__(self):
        if self.n <= 0:
            return f'Это мертвая клетка. У нее 0 ячеек.'
        else:
            return f'В этой клетке {self.n} ячеек'

    def make_order(self,m):
        res=''
        s1 = ''.join('*' for i in range(m))
        s2 = ''.join('*' for i in range(self.n % m))
        for i in range(self.n//m):
            res = res + s1 + '\n'
        return res + s2


a = Cell(4)
b = Cell(6)
print(a+b)
d=a-b
print(d)
c = Cell(-2)
print(c)
print(a*b)
print(a*c)
print(a/b)
print((a*b).make_order(5))
