import time
import random
from itertools import product


def brute_force_crack(combo: tuple[int, ...]) -> None:
    for perm in product(list(range(0, 10)), repeat=len(combo)):
        if perm == combo:
            return


def main():
    for comb_len in range(5, 10):
        comb = tuple(random.randint(0, 9) for _ in range(comb_len))
        start_time = time.time()
        brute_force_crack(comb)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Runtime for {comb_len} digits:\t{duration:.4f} seconds")


if __name__ == '__main__':
    main()
