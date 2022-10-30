from random import randint
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

NUM_EQUIV_VOLUMES = 1_000
MAX_CIVS = 5_000
TRIALS = 1_000
CIV_STEP_SIZE = 100


def estimate_params() -> tuple[list[float], list[float]]:
    x, y = [], []
    for num_civs in range(2, MAX_CIVS+2, CIV_STEP_SIZE):
        civs_per_vol = num_civs / NUM_EQUIV_VOLUMES
        num_single_civs = 0

        for trial in range(TRIALS):
            locations: list[int] = []
            while len(locations) < num_civs:
                location = randint(1, NUM_EQUIV_VOLUMES)
                locations.append(location)
            overlap_count = Counter(locations)
            overlap_rollup = Counter(overlap_count.values())
            num_single_civs += overlap_rollup[1]
        prob = 1 - (num_single_civs / (num_civs * TRIALS))
        print(f"{civs_per_vol:.4f} {prob:.4f}")
        x.append(civs_per_vol)
        y.append(prob)
    return x, y


def plot_results(x: list[float], y: list[float]) -> None:
    coefficients = np.polyfit(x, y, 4)
    p = np.poly1d(coefficients)
    xp = np.linspace(0, 5)
    _ = plt.plot(x, y, '.', xp, p(xp), '-')
    plt.ylim(-0.5, 1.5)
    plt.show()


def main():
    plot_results(*estimate_params())


if __name__ == '__main__':
    main()
