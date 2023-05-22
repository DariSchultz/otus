from src.figure import Figure

class Rectangle(Figure):
    '''Класс прямоугольник'''
    def __init__(self, height:int, width:int):
        self.name = 'Rectangle'
        if height > 0 and width > 0 and height != width:
            self.height = height
            self.width = width
        else:
            raise ValueError('Invalid rectangle height or width')
    
    def perimeter(self):
        '''Метод для вычисления периметра прямоугольника'''
        return 2 * (self.height + self.width)

    def area(self):
        '''Метод для вычисления площади прямоугольника'''
        return self.height * self.width