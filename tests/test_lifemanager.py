import pytest

from n8ture.lifemanager import LifeManager
from n8ture.tree import Tree
from n8ture.constants import INITIAL_TREES_MIN, INITIAL_TREES_MAX


@pytest.fixture
def lifemgr():
    lifemgr = LifeManager()
    return lifemgr


def test_lifemanager_inits_with_no_timepassed(lifemgr):
    assert lifemgr.timepassed == 0


def test_lifemanager_inits_with_random_number_of_trees(lifemgr):
    assert len([life for life in lifemgr.lifeforms if isinstance(life, Tree)]) in range(
        INITIAL_TREES_MIN, INITIAL_TREES_MAX
    )
