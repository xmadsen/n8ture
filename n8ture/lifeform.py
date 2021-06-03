class Lifeform:
    def __init__(
        self,
        location: tuple = (0.0, 0.0),
        calorie_level: float = 100.0,
        max_calorie_level: float = 120.0,
        calorie_usage_rate: float = 1.0,
        eaten_calorie_value: float = 100.0,
    ):
        self.location = location
        self.calorie_level = float(calorie_level)
        self.calorie_usage_rate = calorie_usage_rate
        self.max_calorie_level = max_calorie_level
        self.eaten_calorie_value = eaten_calorie_value

        self.age = 0

    def update(self):
        self.use_calories(self.calorie_usage_rate)
        self.age += 1

    def use_calories(self, calories: float):
        if self.calorie_level - calories < 0:
            self.calorie_level = 0
            return
        self.calorie_level -= calories

    def eat_calories(self, calories: float):
        if self.calorie_level + calories > self.max_calorie_level:
            self.calorie_level = self.max_calorie_level
            return
        self.calorie_level += calories
