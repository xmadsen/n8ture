import pytest

from n8ture.tree import Tree


@pytest.fixture
def test_tree():
    test_tree = Tree(fruit=5, max_fruit=10, ripen_rate=0.2)
    return test_tree


def test_tree_inits_with_fruit(test_tree):
    assert test_tree.fruit == 5


def test_tree_has_unripe_growing_fruit_if_total_fruits_is_less_than_max(test_tree):
    assert test_tree.unripe_fruit == [0, 0, 0, 0, 0]


def test_tree_grows_unripe_fruit_at_ripen_rate(test_tree):
    test_tree.update()
    assert test_tree.unripe_fruit == [0.2, 0.2, 0.2, 0.2, 0.2]


def test_fully_ripened_fruit_is_added_to_fruit(test_tree):
    test_tree.update(times=5)
    assert test_tree.unripe_fruit == []
    assert test_tree.fruit == 10


def test_removing_fruit_from_tree_adds_new_unripe_fruit(test_tree):
    test_tree.remove(count=2)
    assert test_tree.unripe_fruit == [0, 0, 0, 0, 0, 0, 0]


# def test_tree_has_max_fruit_amount():
#     tree = Tree(fruit=5, max_fruit=10)
