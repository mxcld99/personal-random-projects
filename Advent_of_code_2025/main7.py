import os
from functools import lru_cache

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input7.txt')

# Reading content of file
with open(input) as file:
    lines = [list(i[:-1]) for i in file.readlines()]

# Finding start point
beam_start_x = lines.pop(0).index('S')
tach_map = lines.copy()
beams = {beam_start_x}

#########################
## Part 1
#########################

split_count = 0
while len(lines)>0:
    splitters = lines.pop(0)
    beam_snapshot = list(beams)
    for beam in beam_snapshot:
        if splitters[beam] == '^':
            split_count += 1
            beams.remove(beam)
            beams.add(beam-1)
            beams.add(beam+1)

print('PART1: ', split_count)


#########################
## Part 2
#########################
# Immediately Thinking recursion is best for this


max_y = len(tach_map)

# Tried without caching and it just takes way too long - there will be a lot of repeated paths here, so may as well use caching
@lru_cache
def get_num_of_paths(current_y,beam_x):

    total_paths = 0
    while True:
        # Have we reached the end of the map, if so, +1 to path
        if current_y == max_y:
            return 1
        
        # If not, get the next block in the splitter graph
        next_block = tach_map[current_y][beam_x]

        # If a splitter is encountered
        if next_block == '^':
            for new_beam_x in (beam_x-1, beam_x+1):
                total_paths += get_num_of_paths(current_y+1,new_beam_x)
            break

        else:
            current_y += 1
            
    return total_paths

current_y = 0

total_paths = get_num_of_paths(current_y,beam_start_x)

print('PART 2: ', total_paths)
