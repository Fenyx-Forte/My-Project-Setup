import pytest

from src.math_area import area


def test_calculate_area_square():
    assert area.calculate_area_square(2) == 4
    assert area.calculate_area_square(2.5) == 6.25


def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        area.calculate_area_square(-2)


def test_calculate_area_square_string():
    with pytest.raises(TypeError):
        area.calculate_area_square("2")


def test_calculate_area_square_list():
    with pytest.raises(TypeError):
        area.calculate_area_square([2])
