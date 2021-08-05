class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')

painter_1 = Stationery('розовый мелок')
painter_2 = Pen('красная авторучка')
painter_3 = Pencil('карандаш Koh-i-Noor')
painter_4 = Handle('черный фломастер')
painter_1.draw()
painter_2.draw()
painter_3.draw()
painter_4.draw()