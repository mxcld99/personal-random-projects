import os
from functools import lru_cache

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input8.txt')

# Reading content of file
with open(input) as file:
    lines = [[int(j) for j in i[:-1].split(',')] for i in file.readlines()]


# Getting distance between any two boxes
def compare_boxes(b1,b2):
    out = 0
    for a,b in zip(b1,b2):
        out+=(a-b)**2
    return out**0.5

# Getting all distances between boxes
comps = []
for b1,box1 in enumerate(lines):
    for b2,box2 in enumerate(lines[:b1]):
        comps.append(((b1,b2),compare_boxes(box1,box2)))

# Sorting smallest to largest
comps.sort(key=lambda i: i[1])


###################
## Part 1
###################

groups = []
for i in comps[:1000]:
    b1,b2 = i[0]
    b1i,b2i = (-1,-1)

    # Checking if boxes are already in any networks
    for j,group in enumerate(groups):
        if b1 in group:
            b1i = j
        if b2 in group:
            b2i = j
    
    # If boxes aren't in any networks, make a new one
    if b1i== -1 and b2i == -1:
        groups.append({b1,b2})
    
    # If boxes are already in the same group, do nothing
    elif b1i==b2i:
        pass
    
    # If boxes are in different networks, combine networks
    elif b1i != -1 and b2i != -1:
        combined_set = groups[b1i].union(groups[b2i])
        groups[b1i] = combined_set
        groups.pop(b2i)

    # If only one box is already in a group, add other box to that group
    elif b1i != -1:
        groups[b1i].add(b2)
    elif b2i != -1:
        groups[b2i].add(b1)

groups.sort(key=lambda i: len(i), reverse=True)

part1 = 1
for i in groups[:3]:
    part1 *= len(i)

print(part1)


###################
## Part 2
###################

groups = []
i=0
while True:
    b1,b2 = comps[i][0]
    b1i,b2i = (-1,-1)
    i+=1

    # Checking if boxes are already in any networks
    for j,group in enumerate(groups):
        if b1 in group:
            b1i = j
        if b2 in group:
            b2i = j
    
    # If boxes aren't in any networks, make a new one
    if b1i== -1 and b2i == -1:
        groups.append({b1,b2})
    
    # If boxes are already in the same group, do nothing
    elif b1i==b2i:
        pass
    
    # If boxes are in different networks, combine networks
    elif b1i != -1 and b2i != -1:
        combined_set = groups[b1i].union(groups[b2i])
        groups[b1i] = combined_set
        groups.pop(b2i)

    # If only one box is already in a group, add other box to that group
    elif b1i != -1:
        groups[b1i].add(b2)
    elif b2i != -1:
        groups[b2i].add(b1)

    if len(groups)>0:
        if len(groups[0])==1000:
            break


print('PART 2: ',lines[b1][0]*lines[b2][0])

# Nice and easy switch from part 1 to part 2 there