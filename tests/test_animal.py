import pytest
import math

from n8ture.lifeform import Lifeform
from n8ture.animal import Animal
from n8ture.constants import Directions


def test_animal_is_a_lifeform():
    animal = Animal()
    assert isinstance(animal, Lifeform)


def test_animal_inits_with_move_speed():
    animal = Animal()
    assert hasattr(animal, "move_speed")


def test_animal_moves_at_move_speed_4_directions():
    animal = Animal(location=(0, 0), move_speed=2.0)
    animal.move(Directions.LEFT)
    assert animal.location == (-2, 0)
    animal.move(Directions.DOWN)
    assert animal.location == (-2, -2)
    animal.move(Directions.RIGHT)
    assert animal.location == (0, -2)
    animal.move(Directions.UP)
    assert animal.location == (0, 0)


def test_animal_moves_at_move_speed_8_directions():
    animal = Animal(location=(0, 0), move_speed=1.0)
    animal.move(Directions.UPLEFT)
    assert animal.location == (-math.sqrt(2), math.sqrt(2))
    animal.move(Directions.DOWNLEFT)
    assert animal.location == (-2 * math.sqrt(2), 0)
    animal.move(Directions.DOWNRIGHT)
    assert animal.location == (-math.sqrt(2), -math.sqrt(2))
    animal.move(Directions.UPRIGHT)
    assert animal.location == (0, 0)
