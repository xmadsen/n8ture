import pytest

from n8ture.lifeform import Lifeform


def test_lifeform_inits_with_calorie_level():
    lifeform = Lifeform(calorie_level=100)
    assert lifeform.calorie_level == 100


def test_lifeform_inits_with_location_tuple():
    lifeform = Lifeform()
    assert isinstance(lifeform.location, tuple)


# def test_lifeform
