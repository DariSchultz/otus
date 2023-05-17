import pytest
from src.square import Square

@pytest.mark.parametrize('height, width, expected_perimeter, expected_area',
                         [
                             (1, 1, 4, 1),
                             (5, 5, 20, 25),
                             (10, 10, 40, 100)
                         ]
                         )
def test_square_positive(height, width, expected_perimeter, expected_area):
    square = Square(height, width)
    assert square.name == 'Square', 'Expected name is Square'
    assert square.perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert square.area() == expected_area, 'Expected correct area'

@pytest.mark.parametrize('height, width',
                         [
                             (0, 0),
                             (-1, 50),
                             (5, 6)
                         ]
                         )
def test_square_negative(height, width):
    try:
        Square(height, width)
    except:
        assert ValueError