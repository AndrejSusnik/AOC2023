import numpy as np


def tilt_north(grid):
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if grid[i, j] == 'O':
                k = i - 1
                while k >= 0:
                    if grid[k, j] in ['#', 'O']:
                        break
                    k -= 1

                grid[i, j] = '.'
                grid[k + 1, j] = 'O'


def tilt_south(grid):
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0])):
            if grid[i, j] == 'O':
                k = i + 1
                while k < len(grid):
                    if grid[k, j] in ['#', 'O']:
                        break
                    k += 1

                grid[i, j] = '.'
                grid[k - 1, j] = 'O'


def tilt_west(grid):
    for i in range(len(grid)):
        for j in range(1, len(grid[0])):
            if grid[i, j] == 'O':
                k = j - 1
                while k >= 0:
                    if grid[i, k] in ['#', 'O']:
                        break
                    k -= 1

                grid[i, j] = '.'
                grid[i, k + 1] = 'O'


def tilt_east(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0]) - 1, -1, -1):
            if grid[i, j] == 'O':
                k = j + 1
                while k < len(grid[0]):
                    if grid[i, k] in ['#', 'O']:
                        break
                    k += 1

                grid[i, j] = '.'
                grid[i, k - 1] = 'O'


def cycle(grid):
    tilt_north(grid)
    tilt_west(grid)
    tilt_south(grid)
    tilt_east(grid)

if __name__ == "__main__":
    grid = np.array([np.array([*line.strip()]) for line in open('input').readlines()])


    # tilt_north(grid)
    for i in range(1000):
        print(i)
        cycle(grid)

    print(sum(map(lambda x: (len(grid) - x[0]) * len(list(filter(lambda y: y == 'O', x[1]))), enumerate(grid))))




