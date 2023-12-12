from itertools import groupby
from functools import cache
import numpy as np

lines = list(map(lambda x: (x.strip().split(' ')[0], tuple(map(int, x.strip().split(' ')[1].split(',')))), open('input').readlines()))

def get_groups(line: str) -> np.ndarray[int]:
    groups = groupby(line)
    return np.array([sum(1 for _ in group) for label, group in groups if label not in ['.', '?']])

def get_number_of_arrangements(line: tuple[str, tuple[int]]) -> int:
    cons = get_groups(line[0])
    if '?' in line[0]:
        idx = line[0].index('?')

        return get_number_of_arrangements((line[0][: idx] + '.' + line[0][idx + 1:], line[1])) + get_number_of_arrangements((line[0][:idx] + '#' + line[0][idx + 1:], line[1]))

    else:
        if np.array_equal(cons, line[1]):
            return 1
        else:
            return 0


print(sum(map(get_number_of_arrangements, lines)))
