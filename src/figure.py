class Figure:
    '''Базовый класс для всех фигур'''
    _PATH = '/home/dschultz/Рабочий стол/Otus/otus/src'
    def __init__(self, name:str, area, perimeter):
        self.name = name
        self.area = area
        self.perimeter = perimeter
    
    @property
    def area(self):
        raise NotImplementedError
    
    @property
    def perimeter(self):
        raise NotImplementedError

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Invalid figure type')
        return self.area + figure.area 