from sympy import Symbol, solveset, S
import re
from functools import reduce
from operator import mul

x = Symbol('x')
files = list(map(lambda x: list(map(int, re.findall(r'\d+', x.strip().split(': ')[1]))), open('input').readlines()))

print(reduce(mul, [len(solveset(files[0][i] * x - x ** 2 - files[1][i] > 0, x, domain=S.Integers)) for i in range(len(files[0]))], 1))

files = list(map(lambda x: int(x.strip().split(': ')[1].replace(" ", "")), open('input').readlines()))
print(len(solveset(files[0] * x - x ** 2 - files[1] > 0, x, domain=S.Integers)))

