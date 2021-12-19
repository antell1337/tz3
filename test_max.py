from count import *

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [2, 3, 4, 6, 7, 3, 1, 6, 10]


def test_on_first_input_max():
    assert maximalochka(list_1) == 9


def test_on_second_input_max():
    assert maximalochka(list_2) == 10
