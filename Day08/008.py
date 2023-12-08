from math import gcd
if __name__ == "__main__":
    lines = open('input').readlines()

    directions = [0 if char == 'L' else 1 for char in [*lines[0].strip()]]
    nodes = {d[0]: d[1] for d in list(map(lambda z: [z[0], [z[1].split(',')[0][1:], z[1].split(',')[1][1:-1]]], list(map(lambda x: list(map(str.strip, x.strip().split('='))), lines[2:]))))}

    i = 0
    steps = 1
    current = 'AAA'
    next = ''
    while True:
        next = nodes[current][directions[i]]
        if next == 'ZZZ':
            print(steps)
            break

        current = next
        i = (i + 1) % len(directions)
        steps += 1

    current_nodes = [node for node in filter(lambda x: x[-1] == 'A', nodes.keys())]

    i = 0
    steps = 0
    lengths = [0] * len(current_nodes)
    while not all([True if x > 0 else False for x in lengths]):
        current_nodes = [nodes[current][directions[i]] for current in current_nodes]

        lengths = [steps + 1 if node[-1] == 'Z' else c_steps for node, c_steps in zip(current_nodes, lengths)]

        i = (i + 1) % len(directions)
        steps += 1

    lcm = 1
    for i in lengths:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)
