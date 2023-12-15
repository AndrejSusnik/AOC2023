from functools import reduce
from operator import mul

def get_code(input: str) -> int:
    code = 0
    for char in input:
        code += ord(char)
        code *= 17
        code = code % 256
    return code

if __name__ == "__main__":
    print(sum(map(get_code, open('input').read().strip().split(','))))
    init = open('input').read().strip().split(',')
 
    boxes = [[] for _ in range(256)]

    for inst in init:
        if '-' in inst:
            orig = inst[:inst.index('-')]
            code = get_code(orig)
            selected_box = boxes[code]
            boxes[code] = list(filter(lambda x: x[0] != orig, selected_box))
        else:
            orig = inst[:inst.index('=')]
            code = get_code(orig)
            selected_box = boxes[code]
            value = int(inst.split('=')[1])
            
            if orig in map(lambda x: x[0], selected_box):
                boxes[code] = list(map(lambda x: (x[0], x[1]) if x[0] != orig else (x[0], value), selected_box))
            else:
                boxes[code].append((orig, value))

    print(sum([(1 + i) * (1 + j) * lens[1] for i, box in enumerate(boxes) for j, lens in enumerate(box)]))
