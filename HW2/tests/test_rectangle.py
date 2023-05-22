import pytest
from src.rectangle import Rectangle

@pytest.mark.parametrize('height, width, expected_perimeter, expected_area',
                         [
                             (1, 10, 22, 10),
                             (5, 10, 30, 50),
                             (10, 9, 38, 90)
                         ]
                         )
def test_rectangle_positive(height, width, expected_perimeter, expected_area):
    rectangle = Rectangle(height, width)
    assert rectangle.name == 'Rectangle', 'Expected name is Rectangle'
    assert rectangle.perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert rectangle.area() == expected_area, 'Expected correct area'

@pytest.mark.parametrize('height, width',
                         [
                             (0, 1),
                             (-1, 50),
                             (5, 5)
                         ]
                         )
def test_rectangle_negative(height, width):
    with pytest.raises(ValueError):
      Rectangle(height, width)

def test_two_rectangle_areas_sum():
    expected_sum = 60
    rectangle_1 = Rectangle(1, 10)
    rectangle_2 = Rectangle(5, 10)
    assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'