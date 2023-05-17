from src.figure import Figure

class Square(Figure):
    '''Класс квадрат'''
    def __init__(self, height:int, width:int):
        self.name = 'Square'
        if height == width and height > 0 and width > 0:
            self.height = height
            self.width = width
        else:
            raise ValueError('Invalid square height or width')
        
    def perimeter(self):
        '''Метод для вычисления периметра квадрата'''
        return self.height + self.height + self.width + self.width

    def area(self):
        '''Метод для вычисления площади квадрата'''
        return self.height * self.width