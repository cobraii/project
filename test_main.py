
from main import my_sum


def test_my_sum():
    assert my_sum(2, 3) == 5


def test_my_sum_zero():
    assert my_sum(1, 0) == 1
