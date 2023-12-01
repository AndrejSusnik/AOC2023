solution1 = sum(map(lambda x: int(x[0] + x[-1]),[list(filter(lambda x: x.isnumeric(), line.strip())) for line in open('input1').readlines()]))
print(solution1)


str_to_digit = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}


def str_to_int(input: str) -> list[int]:
    numbers = []
    for i in range(len(input)):
        if input[i].isnumeric():
            numbers.append(input[i])
            continue

        for key, value in str_to_digit.items():
            if i + len(key) <= len(input) and input[i: i + len(key)] == key:
                numbers.append(value)
                break

    return numbers


solution2 = sum(map(lambda x: int(x[0] + x[-1]),[str_to_int(line.strip()) for line in open('input1').readlines()]))
print(solution2)
