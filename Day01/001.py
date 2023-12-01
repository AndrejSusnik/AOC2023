import re
solution1 = sum(map(lambda x: int(x[0] + x[-1]),[list(filter(lambda x: x.isnumeric(), line.strip())) for line in open('input1').readlines()]))
print(solution1)

def str_to_int(input: str) -> list[int]:
    input = re.sub('one', 'o1e', input)
    input = re.sub('two', 't2o', input)
    input = re.sub('three', 't3e', input)
    input = re.sub('four', 'f4r', input)
    input = re.sub('five', 'f5e', input)
    input = re.sub('six', 's6x', input)
    input = re.sub('seven', 's7n', input)
    input = re.sub('eight', 'e8t', input)
    input = re.sub('nine', 'n9e', input)

    return list(filter(lambda x: x.isnumeric(), input))

solution2 = sum(map(lambda x: int(x[0] + x[-1]),[str_to_int(line.strip()) for line in open('input1').readlines()]))
print(solution2)
