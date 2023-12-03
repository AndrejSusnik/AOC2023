import numpy as np
from functools import reduce
from operator import mul


def check_nighbour(i: int, j: int, lines) -> bool:
    for k in range(-1, 2):
        for p in range(-1, 2):
            x = np.clip(j + p, 0, len(lines[0]) - 1)
            y = np.clip(i + k, 0, len(lines) - 1)
            if not lines[y][x].isnumeric() and lines[y][x] != '.':
                return y, x, lines[y][x]

    return 0, 0, ''


if __name__ == "__main__":
    lines = list(map(lambda x: x.strip(), open('input').readlines()))
    a: dict[tuple[int, int, str], list[str]] = {}
    for i in range(len(lines)):
        num = ''
        symb = ''
        for j in range(len(lines[0])):
            if lines[i][j].isnumeric():
                num += lines[i][j]
                if symb == '':
                    y, x, symb = check_nighbour(i, j, lines)

            elif num != '':
                if (y, x, symb) not in a.keys():
                    a[(y, x, symb)] = []
                a[(y, x, symb)].append(int(num))
                num = ''
                symb = ''
        if num != '':
            if (y, x, symb) not in a.keys():
                a[(y, x, symb)] = []
            a[(y, x, symb)].append(int(num))
            num = ''
            symb = ''

    print(sum([sum(val) for val in a.values()]) - sum(a[(0, 0, '')]))
    print(sum([reduce(mul, item[1], 1) for item in list(filter(lambda x: x[0][2] == '*' and len(x[1]) == 2, a.items()))]))
