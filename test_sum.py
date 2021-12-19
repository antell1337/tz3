from count import *

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [2, 3, 4, 6, 7, 3, 1, 6, 10]


def test_on_first_input_sum():
    assert summa(list_1) == 45


def test_on_second_input_sum():
    assert summa(list_2) == 42
