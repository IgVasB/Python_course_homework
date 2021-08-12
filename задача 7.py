# Тут я напрасно кажется заморочился с переопределением __str__ :(
class complex:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a != 0:
            real = str(self.a)
        else:
            real = ''
        if self.b != 0:
            if self.b < 0:
                img = str(self.b)
            else:
                if real == '':
                    img = str(self.b)
                else:
                    img = '+'+str(self.b)
        else:
            img = ''

        if real == '' and img == '':
            return '0'
        else:
            if img == '':
                return real
            else:
                if self.b == -1:
                    img = '-'
                else:
                    if self.b == 1:
                        if real == '':
                            img = ''
                        else:
                            img = '+'
                return real + img + 'i'

    def __add__(self, other):
        return complex(self.a+other.a, self.b+other.b)

    def __mul__(self, other):
        real = self.a*other.a-self.b*other.b
        img =self.a*other.b+self.b*other.a
        return complex(real,img)

x = complex(-1,0)
y = complex(-2,5)
print(x)
print(y)
print(x+y)
print(x*y)
