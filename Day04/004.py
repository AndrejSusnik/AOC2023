import numpy as np

if __name__ == "__main__":
    scores = list(map(lambda x: len(np.intersect1d(x[0], x[1])),
                      [list(map(lambda x: np.array(list(map(int, x.split()))),
                                line.strip().split(':')[1].split('|')))
                      for line in open('input').readlines()]))

    print(sum(map(lambda x: 2 ** (x - 1) if x > 0 else 0, scores)))

    scrds = np.ones(len(scores))

    for i, value in enumerate(scores):
        scrds[i + 1: i+value+1] += 1 * scrds[i]

    print(int(sum(scrds)))
