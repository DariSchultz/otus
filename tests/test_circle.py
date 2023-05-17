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
                             (-1),
                             ('text')
                         ]
                         )
def test_circle_negative(radius):
    try:
        Circle(radius)
    except:
        assert ValueError