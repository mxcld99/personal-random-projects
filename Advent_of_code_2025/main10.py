import os
from functools import lru_cache

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input10.txt')

# Reading content of file
with open(input) as file:
    lines = [i[:-1].split(' ') for i in file.readlines()]

final_states = [i[0] for i in lines]
buttons = [[tuple(int(k) for k in j[1:-1].split(',')) for j in i[1:-1]] for i in lines]
joltages = [tuple(int(j) for j in i[-1][1:-1].split(',')) for i in lines]

print(final_states[0])
print(buttons[0])
print(joltages[0])

# Iniitial thoughts are that a breadth-first search algorithm is the best approach for pt 1

