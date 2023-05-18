import pytest
from src.circle import Circle 

@pytest.mark.parametrize('radius, expected_perimeter, expected_area',
                         [
                             (10, 62.83, 314.16),
                             (50, 314.16, 7853.97),
                             (100, 628.32, 31415.9)
                         ]
                         )
def test_circle_positive(radius, expected_perimeter, expected_area):
    circle = Circle(radius)
    assert circle.name == 'Circle', 'Expected name is Circle'
    assert circle.perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert circle.area() == expected_area, 'Expected correct area'

@pytest.mark.parametrize('radius',
                         [
                             (0),
                             (-1)
                         ]
                         )
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)

def test_two_circle_areas_sum():
    expected_sum = 326.73
    circle_1 = Circle(10)
    circle_2 = Circle(2)
    assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'