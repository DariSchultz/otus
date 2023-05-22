class Figure:
    '''Базовый класс для всех фигур'''
    def __init__(self, name:str, area, perimeter):
        self.name = name
        self.area = area
        self.perimeter = perimeter
    
    def area(self):
        raise NotImplementedError
    
    def perimeter(self):
        raise NotImplementedError

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return round(self.area() + figure.area(), 2)
        raise ValueError(f'Object {figure} is not subclass of Figure class')