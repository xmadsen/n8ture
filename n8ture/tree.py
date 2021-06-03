from n8ture.lifeform import Lifeform


class Tree(Lifeform):
    def __init__(
        self,
        location: tuple = (0.0, 0.0),
        calorie_level: float = 100.0,
        max_calorie_level: float = 120.0,
        calorie_usage_rate: float = 1.0,
        fruit: int = 5,
        max_fruit: int = 10,
        ripen_rate: float = 0.1,
    ):
        super().__init__(location, calorie_level, max_calorie_level, calorie_usage_rate)
        self.fruit = fruit
        self.max_fruit = max_fruit
        self.ripen_rate = ripen_rate
        self.unripe_fruit = [0 for _ in range(max_fruit - fruit)]

    def update(self, times: int = 1):
        for _ in range(times):
            super().update()
            self.unripe_fruit = [
                fruit_progress + self.ripen_rate for fruit_progress in self.unripe_fruit
            ]
            for fruit in self.unripe_fruit:
                if fruit == 1:
                    self.fruit += 1
            self.unripe_fruit = list(filter(lambda x: x != 1, self.unripe_fruit))

    def remove(self, count: int):
        self.fruit -= count
        self.unripe_fruit.extend([0] * count)
