import pytest

from n8ture.lifeform import Lifeform


def test_lifeform_inits_with_calorie_level():
    lifeform = Lifeform(calorie_level=100)
    assert lifeform.calorie_level == 100


def test_lifeform_inits_with_location_tuple():
    lifeform = Lifeform()
    assert isinstance(lifeform.location, tuple)


def test_lifeform_inits_with_calorie_usage_rate():
    lifeform = Lifeform()
    assert isinstance(lifeform.calorie_usage_rate, float)


def test_lifeform_subtracts_calorie_usage_rate_from_calorie_level_on_update():
    lifeform = Lifeform()
    before_level = lifeform.calorie_level
    lifeform.update()
    assert lifeform.calorie_level == before_level - lifeform.calorie_usage_rate


def test_lifeform_gains_calories_on_get_calories():
    lifeform = Lifeform()
    before_level = lifeform.calorie_level
    lifeform.get_calories(10)
    assert lifeform.calorie_level == before_level + 10


def test_lifeform_get_calories_will_not_gain_more_than_max_calorie_level():
    lifeform = Lifeform(calorie_level=140, max_calorie_level=150)
    more_calories_than_needed = 20
    lifeform.get_calories(more_calories_than_needed)
    assert lifeform.calorie_level == lifeform.max_calorie_level
