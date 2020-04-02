import pytest
from retire import *


def test_retire_age():
    with pytest.raises(SystemExit):
        retire(-1, 1, 0.1, 1)
    with pytest.raises(SystemExit):
        retire(0, 1, 0.1, 1)
    assert retire(40, 1, 0.1, 1) == float or int
    assert retire(100, 200000, 0.9, 200000) == float or int
    with pytest.raises(SystemExit):
        retire(101, 1, 0.1, 1)


def test_retire_salary():
    with pytest.raises(SystemExit):
        retire(1, -1, 0.1, 1)
    with pytest.raises(SystemExit):
        retire(1, -1, 0.1, 1)
    assert retire(1, 1, 0.1, 1) == float or int


def test_retire_save():
    with pytest.raises(SystemExit):
        retire(1, 1, -1, 1)
    with pytest.raises(SystemExit):
        retire(1, 1, 0, 1)
    assert retire(1, 1, .5, 1) == float or int
    assert retire(1, 1, 1, 1) == float or int
    with pytest.raises(SystemExit):
        retire(1, 1, 1.5, 1)


def test_retire_goal():
    with pytest.raises(SystemExit):
        retire(1, 1, 1.5, -1)
    assert retire(1, 1, .5, 0) == float or int
    assert retire(1, 1, .5, 1) == float or int
