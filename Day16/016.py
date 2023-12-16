import numpy as np
from enum import Enum
from functools import cache
import sys


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


activated = set()


@cache
def get_next_pos(pos: tuple[int, int], dir: Direction):
    if dir is Direction.UP:
        return (pos[0] - 1, pos[1])
    elif dir is Direction.DOWN:
        return (pos[0] + 1, pos[1])
    elif dir is Direction.LEFT:
        return (pos[0], pos[1] - 1)
    elif dir is Direction.RIGHT:
        return (pos[0], pos[1] + 1)

# @cache
def travel(pos: tuple[int, int], dir: Direction, grid):
    if pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0]) or (pos, dir) in activated:
        return 0

    activated.add((pos, dir))

    if grid[pos[0]][pos[1]] == '/':
        if dir is Direction.UP:
            dir = Direction.RIGHT
        elif dir is Direction.DOWN:
            dir = Direction.LEFT
        elif dir is Direction.LEFT:
            dir = Direction.DOWN
        elif dir is Direction.RIGHT:
            dir = Direction.UP
    elif grid[pos[0]][pos[1]] == '\\':
        if dir is Direction.UP:
            dir = Direction.LEFT
        elif dir is Direction.DOWN:
            dir = Direction.RIGHT
        elif dir is Direction.LEFT:
            dir = Direction.UP
        elif dir is Direction.RIGHT:
            dir = Direction.DOWN
    elif grid[pos[0]][pos[1]] == '-':
        if dir in [Direction.UP, Direction.DOWN]:
            return travel(get_next_pos(pos, Direction.LEFT), Direction.LEFT, grid) + travel(get_next_pos(pos, Direction.RIGHT), Direction.RIGHT, grid)
    elif grid[pos[0]][pos[1]] == '|':
        if dir in [Direction.LEFT, Direction.RIGHT]:
            return travel(get_next_pos(pos, Direction.UP), Direction.UP, grid) + travel(get_next_pos(pos, Direction.DOWN), Direction.DOWN, grid)

    return travel(get_next_pos(pos, dir), dir, grid)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    grid = tuple([tuple([*line.strip()]) for line in open('input').readlines()])

    start_pos = (0, 0)
    start_dir = Direction.RIGHT

    a = travel(start_pos, start_dir, grid)
    print(len({x[0] for x in activated}))

    max_len = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if i == 0 or j == 0 or i == (len(grid) - 1) or j == (len(grid[0]) - 1):
                start_pos = (i, j)
                if i == 0:
                    start_dir = Direction.DOWN
                    a = travel(start_pos, start_dir, grid)
                    max_len = max(max_len, len({x[0] for x in activated}))
                    activated = set()
                if j == 0:
                    start_dir = Direction.RIGHT
                    a = travel(start_pos, start_dir, grid)
                    max_len = max(max_len, len({x[0] for x in activated}))
                    activated = set()

                if j == (len(grid[0]) - 1):
                    start_dir = Direction.LEFT
                    a = travel(start_pos, start_dir, grid)
                    max_len = max(max_len, len({x[0] for x in activated}))
                    activated = set()

                if i == (len(grid) - 1):
                    start_dir = Direction.UP
                    a = travel(start_pos, start_dir, grid)
                    max_len = max(max_len, len({x[0] for x in activated}))
                    activated = set()

    print(max_len)
