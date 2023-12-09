lines = list(map(lambda x: list(map(int, x.strip().split(' '))), open('input').readlines()))

def get_next_item(sequence: list[int]) -> int:
    if not any(sequence):
        return 0

    return sequence[-1] + get_next_item(list(map(lambda x: x[1] - x[0], zip(sequence, sequence[1:]))))

def get_prev_item(sequence: list[int]) -> int:
    if not any(sequence):
        return 0

    return sequence[0] - get_prev_item(list(map(lambda x: x[1] - x[0], zip(sequence, sequence[1:]))))


print(sum([get_next_item(line) for line in lines]))
print(sum([get_prev_item(line) for line in lines]))
