from functools import reduce
import operator


def is_possible(game: str):
    max_stones = {"red": 12, "green": 13, "blue": 14}

    id, draws = game.split(':')
    id = int(id.split(' ')[1])

    for draw in draws.split(';'):
        stones = draw.split(',')
        for stone in stones:
            number, color = stone.strip().split(' ')
            if max_stones[color] < int(number):
                return 0
    return id


def power_of_the_game(game: str):
    id, draws = game.split(':')
    id = int(id.split(' ')[1])

    max_stone = {"red": 0, "green": 0, "blue": 0}

    for draw in draws.split(';'):
        stones = draw.split(',')
        for stone in stones:
            number, color = stone.strip().split(' ')
            max_stone[color] = max(max_stone[color], int(number))

    return reduce(operator.mul, max_stone.values(), 1)


if __name__ == "__main__":
    print(sum([is_possible(line) for line in open('input').readlines()]))

    print(sum([power_of_the_game(line) for line in open('input').readlines()]))
