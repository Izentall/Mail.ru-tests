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


@pytest.mark.parametrize('length', [0, 1, 10])
def test_set_len(length):
    s = set()
    for i in range(length):
        s.add(i)
    assert len(s) == length


def test_set_union():
    s1 = set([0, 2, 4, 6, 8, 10, 12])
    s2 = set([0, 3, 6, 9, 12])
    check = set([0, 2, 3, 4, 6, 8, 9, 10, 12])
    assert s1.union(s2) == check


@pytest.mark.parametrize('s, elem',
                         [
                             ([1, 2, 3], 4),
                             ([1, 2, 3, 4], 4),
                             ([1, 2, 3, 4, 4], 4)
                         ])
def test_set_discard(s, elem):
    s1 = set(s)
    s1.discard(elem)
    assert not (elem in s1)
