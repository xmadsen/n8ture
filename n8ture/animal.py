import math

from n8ture.lifeform import Lifeform
from n8ture.constants import Directions


class Animal(Lifeform):
    def __init__(
        self,
        location: tuple = (0.0, 0.0),
        calorie_level: float = 100.0,
        max_calorie_level: float = 120.0,
        calorie_usage_rate: float = 1.0,
        move_speed: float = 1.0,
    ):
        super().__init__(location, calorie_level, max_calorie_level, calorie_usage_rate)
        self.move_speed = move_speed

    def move(self, direction):
        mag = math.sqrt(direction[0] ** 2 + direction[1] ** 2)

        self.location = (
            self.location[0] + self.move_speed * mag * direction[0],
            self.location[1] + self.move_speed * mag * direction[1],
        )
