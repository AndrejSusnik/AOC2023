import numpy as np
import sys

def get_next_pos(prev_pos: tuple[int, int], current_pos: tuple[int, int], grid) -> tuple[int, int]:
    if grid[current_pos[0], current_pos[1]] == '-':
        return (current_pos[0], current_pos[1] + (1 if prev_pos[1] < current_pos[1] else -1))
    elif grid[current_pos[0], current_pos[1]] == '|':
        return (current_pos[0] + (1 if prev_pos[0] < current_pos[0] else -1), current_pos[1])
    elif grid[current_pos[0], current_pos[1]] == 'L':
        if prev_pos[1] > current_pos[1]:
            return (current_pos[0] - 1, current_pos[1])
        else:
            return (current_pos[0], current_pos[1] + 1)
    elif grid[current_pos[0], current_pos[1]] == 'J':
        if prev_pos[1] < current_pos[1]:
            return (current_pos[0] - 1, current_pos[1])
        else:
            return (current_pos[0], current_pos[1] - 1)
    elif grid[current_pos[0], current_pos[1]] == '7':
        if prev_pos[0] > current_pos[0]:
            return (current_pos[0], current_pos[1] - 1)
        else:
            return (current_pos[0] + 1, current_pos[1])
    elif grid[current_pos[0], current_pos[1]] == 'F':
        if prev_pos[1] > current_pos[1]:
            return (current_pos[0] + 1, current_pos[1])
        else:
            return (current_pos[0], current_pos[1] + 1)

def get_loop(start, grid):
    current = start
    prev_pos = start
    loop = {current}
    while True:
        tmp = current
        current = get_next_pos(prev_pos, current, grid)

        if current == start:
            break

        loop.add((current[0], current[1]))
        prev_pos = tmp

    return loop

flooded = set()
def flood(i, j, loop, grid):
    if (i, j) in flooded or (i, j) in loop:
        return 0

    flooded.add((i, j))
    sum = 0

    for y in range(-1, 2):
        for x in range(-1, 2):
            if y == 0 and x == 0:
                continue
            if i - y < 0 or j - x < 0 or i - y >= len(grid) or j - x >= len(grid[0]):
                continue
            if grid[i - y, j - x] in ['O', '.']:
                sum += flood(i - y, j - x, loop, grid)
    return sum + (1 if grid[i, j] == 'O' else 0)



if __name__ == "__main__":
    grid = np.array([np.array([*line.strip()]) for line in open('input').readlines()])
    gridsize = len(grid) * len(grid[0])
    sys.setrecursionlimit(gridsize)

    start = np.where(grid == 'S')
    start = (start[0][0], start[1][0])

    grid[start[0], start[1]] = '7'
    # grid[start[0], start[1]] = 'F'

    loop = get_loop(start, grid)

    extended_grid = np.array([np.array(['.'] * len(grid[0]) * 2)] * len(grid) * 2)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i, j] == '.' or (i, j) not in loop:
                extended_grid[i*2, j*2] = 'O'
            elif grid[i, j] == 'F':
                extended_grid[i * 2, j * 2] = 'F'
                extended_grid[i * 2 + 1, j * 2] = '|'
                extended_grid[i * 2, j * 2 + 1] = '-'
                pass
            elif grid[i, j] == 'L':
                extended_grid[i * 2, j * 2] = 'L'
                extended_grid[i * 2, j * 2 + 1] = '-'
            elif grid[i, j] == '7':
                extended_grid[i * 2, j * 2] = '7'
                extended_grid[i * 2 + 1, j * 2] = '|'
            elif grid[i, j] == 'J':
                extended_grid[i * 2, j * 2] = 'J'
            elif grid[i, j] == '-':
                extended_grid[i * 2, j * 2] = '-'
                extended_grid[i * 2, j * 2 + 1] = '-'
            elif grid[i, j] == '|':
                extended_grid[i * 2 + 1, j * 2] = '|'
                extended_grid[i * 2, j * 2] = '|'

    np.set_printoptions(linewidth=190)
    loop_2 = get_loop((start[0] * 2, start[1] * 2), extended_grid)
    
    flood_size = 0
    for i in range(len(extended_grid)):
        for j in range(len(extended_grid[0])):
            if i == 0 or j == 0 or i == (len(extended_grid) - 1) or j == (len(extended_grid[0]) - 1):
                flood_size += flood(i, j, loop_2, extended_grid)

    print(int(len(loop) / 2))
    print(gridsize - flood_size - len(loop))
