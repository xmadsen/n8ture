class Tree:
    def __init__(self, fruit: int, max_fruit: int, ripen_rate: float):
        self.fruit = fruit
        self.max_fruit = max_fruit
        self.ripen_rate = ripen_rate
        self.unripe_fruit = [0 for _ in range(max_fruit - fruit)]


    def update(self, times=1):
        for _ in range(times):
            self.unripe_fruit = [fruit_progress + self.ripen_rate for fruit_progress in self.unripe_fruit]
            for fruit in self.unripe_fruit:
                if fruit == 1:
                    self.fruit += 1
            self.unripe_fruit = list(filter(lambda x: x != 1, self.unripe_fruit))
        
    def remove(self, count):
        self.fruit -= count
        self.unripe_fruit.extend([0] * count)
