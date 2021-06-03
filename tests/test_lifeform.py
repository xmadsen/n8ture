import pytest

from n8ture.lifeform import Lifeform


def test_lifeform_inits_with_calorie_level():
    lifeform = Lifeform(calorie_level=100)
    assert lifeform.calorie_level == 100


def test_lifeform_inits_with_location_tuple():
    lifeform = Lifeform()
    assert hasattr(lifeform, "location")


def test_lifeform_inits_with_calorie_usage_rate():
    lifeform = Lifeform()
    assert hasattr(lifeform, "calorie_usage_rate")


def test_lifeform_subtracts_calorie_usage_rate_from_calorie_level_on_update():
    lifeform = Lifeform()
    before_level = lifeform.calorie_level
    lifeform.update()
    assert lifeform.calorie_level == before_level - lifeform.calorie_usage_rate


def test_lifeform_cannot_go_below_zero_calories():
    lifeform = Lifeform(calorie_level=1, calorie_usage_rate=2.0)
    lifeform.update()
    assert lifeform.calorie_level == 0


def test_lifeform_gains_calories_on_eat_calories():
    lifeform = Lifeform()
    before_level = lifeform.calorie_level
    lifeform.eat_calories(10)
    assert lifeform.calorie_level == before_level + 10


def test_lifeform_eat_calories_will_not_gain_more_than_max_calorie_level():
    lifeform = Lifeform(calorie_level=140, max_calorie_level=150)
    more_calories_than_needed = 20
    lifeform.eat_calories(more_calories_than_needed)
    assert lifeform.calorie_level == lifeform.max_calorie_level


def test_lifeform_inits_with_age_0():
    lifeform = Lifeform()
    assert lifeform.age == 0


def test_lifeform_age_increments_on_update():
    lifeform = Lifeform()
    initial_age = lifeform.age

    lifeform.update()
    lifeform.update()

    assert lifeform.age == initial_age + 2
