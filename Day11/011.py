import numpy as np

if __name__ == "__main__":
    grid = np.array([np.array([*line.strip()]) for line in open('input').readlines()])

    galaxyes = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i, j] == '#']

    acum = 10e5 - 1

    added_rows = []
    acc = 0
    for i in range(len(grid)):
        if all(grid[i, :] == '.'):
            acc += acum

        added_rows.append(acc)

    added_columns = []
    acc = 0
    for i in range(len(grid[0])):
        if all(grid[:, i] == '.'):
            acc += acum

        added_columns.append(acc)

    galaxyes = list(map(lambda x: (x[0] + added_rows[x[0]], x[1] + added_columns[x[1]]), galaxyes))

    pairs = {(tuple([*galaxyes[i]]), tuple([*galaxyes[j]])) for i in range(len(galaxyes)) for j in range(i + 1, len(galaxyes))}

    print(int(sum(map(lambda x: abs(x[1][0] - x[0][0]) + abs((x[1][1] - x[0][1])), pairs))))
