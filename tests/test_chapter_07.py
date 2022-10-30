import pytest
from impractical_python.Chapter_07.super_rats import \
        populate, fitness, select, breed, mutate
from impractical_python.Chapter_07.safe_cracker import \
        fitness as cracker_fitness


def test_populate():
    num, min_val, max_val, mode_val = 30, 50, 80, 65
    arr = populate(num, min_val, max_val, mode_val)
    assert all([x >= min_val for x in arr])
    assert all([x <= max_val for x in arr])
    assert len(arr) == num


@pytest.mark.parametrize("test_input,expected", [
    (([1, 2, 3, 4, 5], 7), 0.428571428),
    (([5, 4, 3, 4, 5], 5), 0.84),
    (([-5, -4, 3, 4, 5], 5), 0.12)
])
def test_fitness(test_input, expected):
    assert abs(fitness(*test_input) - expected) <= 1e-06


def test_select():
    arr = list(range(1, 10))
    assert select(arr, 4) == ([8, 9], [3, 4])


def test_breed():
    males, females = [8, 9], [3, 4]
    arr = breed(males, females, 6)
    assert len(arr) == 12
    assert min(arr) >= min(females)
    assert max(arr) <= max(males)


def test_mutate():
    inp = [40, 50, 60, 70]
    rate, min_mut, max_mut = 0.5, 0.6, 1.5
    arr = mutate(inp, rate, min_mut, max_mut)
    assert min(arr) >= min(inp) * min_mut
    assert max(arr) <= max(inp) * max_mut
