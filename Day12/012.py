from itertools import groupby
from functools import cache
import numpy as np

lines = list(map(lambda x: (x.strip().split(' ')[0], tuple(map(int, x.strip().split(' ')[1].split(',')))), open('input').readlines()))

@cache
def get_number_of_arrangements1(line: str, group: list[int]):
    line = line.lstrip('.')

    if not line:
        return not group
    elif not group:
        return '#' not in line
    if line[0] == '?':
        return get_number_of_arrangements1('.' + line[1:], group) + get_number_of_arrangements1('#' + line[1:], group)

    current_group = group[0]
    if len(line) < current_group or "." in line[:current_group] or (len(line) > current_group and line[current_group] == "#"):
        return 0

    return get_number_of_arrangements1(line[current_group + 1:], group[1:])

print(sum(map(lambda x: get_number_of_arrangements1(*x), lines)))

acc = 0
for line in lines:
    lin, group = line
    lin, group = ("?".join([lin] * 5), group*5)
    acc += get_number_of_arrangements1(lin, group)
print(acc)
