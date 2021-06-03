from random import randrange

from n8ture.tree import Tree
from n8ture.constants import INITIAL_TREES_MIN, INITIAL_TREES_MAX


class LifeManager:
    def __init__(self):
        self.timepassed = 0
        self.lifeforms = []

        self.add_lifeforms()

    def add_lifeforms(self):
        self.add_trees()

    def add_trees(self):
        for _ in range(randrange(INITIAL_TREES_MIN, INITIAL_TREES_MAX)):
            loc = (randrange(-10, 10), randrange(-10, 10))
            while any(life for life in self.lifeforms if life.location == loc):
                loc = (randrange(-10, 10), randrange(-10, 10))

            self.lifeforms.append(Tree(location=loc))
