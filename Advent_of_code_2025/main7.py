import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input7.txt')

# Reading content of file
with open(input) as file:
    lines = [list(i[:-1]) for i in file.readlines()]

#########################
## Part 1
#########################

# Finding start point
beams = {lines.pop(0).index('S')}

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

