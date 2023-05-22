import pytest
from src.square import Square

@pytest.mark.parametrize('side, expected_perimeter, expected_area',
                         [
                             (1, 4, 1),
                             (5, 20, 25),
                             (10, 40, 100)
                         ]
                         )
def test_square_positive(side, expected_perimeter, expected_area):
    square = Square(side)
    assert square.name == 'Square', 'Expected name is Square'
    assert square.perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert square.area() == expected_area, 'Expected correct area'

@pytest.mark.parametrize('side',
                         [
                             (0),
                             (-1)
                         ]
                         )
def test_square_negative(side):
   with pytest.raises(ValueError):
      Square(side)

def test_two_square_areas_sum():
    expected_sum = 101
    square_1 = Square(1)
    square_2 = Square(10)
    assert square_1.add_area(square_2) == expected_sum, f'Expected sum is {expected_sum}'