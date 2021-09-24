import pytest


def test_tuple_order():
    (a, b) = (1, 2)
    assert a == 1
    assert b == 2


@pytest.mark.parametrize('a, b, c, d, value, result',
                         [
                             (1, 2, 3, 4, 0, 0),
                             (0, 0, 0, 0, 0, 4),
                             (1, 2, 3, 4, 4, 1),
                             (-1, -2, -3, -1, -1, 2),
                             (0, 3, 3, 3, 3, 3)
                         ])
def test_tuple_count(a, b, c, d, value, result):
    tup = (a, b, c, d)
    assert tup.count(value) == result


@pytest.mark.parametrize('a, b, c, d, value',
                         [
                             (1, 2, 3, 4, 0),
                             (0, 0, 0, 0, -1)
                         ])
def test_tuple_index(a, b, c, d, value):
    tup = (a, b, c, d)
    try:
        assert tup.index(value)
    except ValueError:
        pass
