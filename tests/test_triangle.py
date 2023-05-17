import pytest
from src.triangle import Triangle

@pytest.mark.parametrize('side_a, side_b, side_c, expected_perimeter, expected_area',
                         [
                             (10, 10, 10, 30, 43.3),
                             (2, 2, 3, 7, 1.98),
                             (5, 6, 8, 19, 14.98)
                         ]
                         )
def test_triangle_positive(side_a, side_b, side_c, expected_perimeter, expected_area):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.name == 'Triangle', 'Expected name is Triangle'
    assert triangle.perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert triangle.area() == expected_area, 'Expected correct area'

@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             (0, 0, 0),
                             (-1, -2, -3),
                             (1, 1, 3)
                         ]
                         )
def test_triangle_negative(side_a, side_b, side_c):
    try:
        Triangle(side_a, side_b, side_c)
    except:
        assert ValueError