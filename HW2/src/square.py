from src.figure import Figure

class Square(Figure):
    '''Класс квадрат'''
    def __init__(self, side:int):
        self.name = 'Square'
        if side > 0 and side !=0:
            self.side = side
        else:
            raise ValueError('Invalid square height or width')
        
    def perimeter(self):
        '''Метод для вычисления периметра квадрата'''
        return self.side + self.side + self.side + self.side

    def area(self):
        '''Метод для вычисления площади квадрата'''
        return self.side * self.side