from src.figure import Figure

class Circle(Figure):
    '''Класс круг'''
    def __init__(self, radius:int):
        self.name = 'Circle'
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError('Invalid circle radius')
        
    def perimeter(self):
        '''Метод для вычисления периметра круга'''
        perimeter = 2 * 3.14159 * self.radius
        return round(perimeter, 2)

    def area(self):
        '''Метод для вычисления площади круга'''
        area = 3.14159 * self.radius ** 2
        return round(area, 2)