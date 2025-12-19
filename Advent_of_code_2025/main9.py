import os
from functools import lru_cache

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input9.txt')

# Reading content of file
with open(input) as file:
    lines = [[int(j) for j in i[:-1].split(',')] for i in file.readlines()]

# Just going to brute force this...easy enough

# Getting rectangle size
def get_rectangle(b1,b2):
    out = 1
    for a,b in zip(b1,b2):
        out*=abs(a-b)+1
    return out

# Sizing all possible rectangles
comps = []
for c1,coord1 in enumerate(lines):
    for c2,coord2 in enumerate(lines[:c1]):
        comps.append(get_rectangle(coord1,coord2))

# Getting largest rectangle
print(max(comps))