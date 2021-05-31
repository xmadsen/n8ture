class Lifeform():
    def __init__(self, location=(0, 0), calorie_level=100, max_calorie_level=120, calorie_usage_rate=1.0):
        self.location = location
        self.calorie_level = calorie_level
        self.calorie_usage_rate = calorie_usage_rate
        self.max_calorie_level = max_calorie_level

    def update(self):
        self.use_calories(self.calorie_usage_rate)

    def use_calories(self, calories):
        self.calorie_level -= calories

    def get_calories(self, calories):
        if self.calorie_level + calories > self.max_calorie_level:
            self.calorie_level = self.max_calorie_level
            return
        self.calorie_level += calories
