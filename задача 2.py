from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self,size):
        self.size = size

    @abstractmethod
    def calc_consumption(self):
        pass

class Suit(Clothes):
    def calc_consumption(self):
        return 2*self.size+0.3

class Coat(Clothes):
    @property # потестируем декоратор
    def calc_consumption(self):
        return self.size/6.5+0.5

blue_suit = Suit(5)
raincoat = Coat(10)
print('%.2f' % blue_suit.calc_consumption())
#print('%.2f' % raincoat.calc_consumption())
print('%.2f' % raincoat.calc_consumption)
