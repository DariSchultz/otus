from src.figure import Figure
import math

class Triangle(Figure):
    '''Класс треугольник'''
    def __init__(self, side_a:int, side_b:int, side_c:int):
        self.name = 'Triangle'
        if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            raise ValueError('Invalid triangle sides')

    def perimeter(self):
        '''Метод для вычисления периметра треугольника'''
        return self.side_a + self.side_b + self.side_c

    def area(self):
        '''Метод для вычисления площади треугольника'''
        half_perimeter = self.perimeter() / 2
        area = math.sqrt(half_perimeter * (half_perimeter - self.side_a) * (half_perimeter - self.side_b) * (half_perimeter - self.side_c))
        return round(area, 2)
         

    
