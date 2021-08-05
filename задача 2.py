class Road:
    def __init__(self,length,width):
        self._length = length
        self._width = width
    def cover_weight(self, surface_density,thickness):
        return self._length*self._width*surface_density*thickness
r=Road(5000,20)
print(r.cover_weight(25,5)/1000, 'тонн афальта')