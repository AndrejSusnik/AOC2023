import numpy as np


def find_vertical_symetry(grid: np.ndarray[np.ndarray[str]]):
    cols = len(grid[0])

    for i in range(1, len(grid[0])):
        a = grid[:, :i][:, ::-1][:, :min(cols - i, i)]
        b = grid[:, i:][:, :min(cols - i, i)]

        if (len(a[0]) * len(a)) - np.count_nonzero(a == b) == 1:
            return i

    return 0


def find_horizontal_symetry(grid: np.ndarray[np.ndarray[str]]):
    rows = len(grid)
    for i in range(1, len(grid)):
        a = grid[:i, :][::-1, :][:min(rows - i, i), :]
        b = grid[i:, :][:min(rows - i, i), :]

        if (len(a[0]) * len(a)) - np.count_nonzero(a == b) == 1:
            return i

    return 0


if __name__ == "__main__":
    print(sum(map(lambda x: 100 * find_horizontal_symetry(x) + find_vertical_symetry(x), list(map(lambda x: np.array(list(map(lambda y: np.array([*y]), x.strip().split('\n')))), open('input').read().split("\n\n"))))))

import numpy as np

images = [np.array([[c == "#" for c in line] for line in im.splitlines()])
                   for im in open("input.txt").read().split("\n\n")]
