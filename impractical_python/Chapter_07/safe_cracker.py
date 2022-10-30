import time
from random import randint, randrange, choice
from typing import Callable


def fitness(combo: list[int], attempt: list[int]) -> int:
    """Compare items in two lists and count number of matches."""
    return sum(i == j for i, j in zip(combo, attempt))


def hill_climb_crack(combo: list[int]) -> int:
    best_attempt = [0 for _ in range(len(combo))]
    best_grade = fitness(combo, best_attempt)
    count = 0

    while best_grade != len(combo):
        next_try = best_attempt[:]
        lock_wheel = randrange(0, len(combo))
        next_try[lock_wheel] = randint(0, 9)
        next_grade = fitness(combo, next_try)
        if next_grade > best_grade:
            best_grade = next_grade
            best_attempt = next_try[:]
        count += 1
    return count


def effective_hill_climb_crack(combo: list[int]) -> int:
    best_attempt = [0 for _ in range(len(combo))]
    best_grade = fitness(combo, best_attempt)
    idx_to_choose = list(range(len(combo)))
    count = 0

    while best_grade != len(combo):
        next_try = best_attempt[:]
        lock_wheel = choice(idx_to_choose)
        next_try[lock_wheel] = randint(0, 9)
        next_grade = fitness(combo, next_try)
        if next_grade > best_grade:
            best_grade = next_grade
            best_attempt = next_try[:]
            idx_to_choose.remove(lock_wheel)
        count += 1
    return count


def test_runtime(fn: Callable[[list[int]], int], comb: list[int]) -> tuple[int, float]:
    start_time = time.perf_counter()
    iters_num = fn(comb)
    end_time = time.perf_counter()
    duration = end_time - start_time
    return iters_num, duration


def main():
    for comb_len in range(5, 15):
        comb = [randint(0, 9) for _ in range(comb_len)]
        iters_1, time_1 = test_runtime(hill_climb_crack, comb)
        iters_2, time_2 = test_runtime(effective_hill_climb_crack, comb)
        print(f"Runtime for {comb_len} digits:\t{time_1:.5f} seconds in {iters_1:03} \
iterations vs {time_2:.5f} seconds in {iters_2:03} iterations")


if __name__ == '__main__':
    main()
