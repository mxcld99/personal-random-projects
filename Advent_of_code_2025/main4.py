import os
from sympy.ntheory import factorint

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input4.txt')

# Reading content of file
with open(input) as file:
    read_lines = [i[:-1] for i in file.readlines()]
    rows = len(read_lines[0])
    cols = len(read_lines)
    buffer = list('.'*rows)
    lines = [list('.'+i+'.') for i in read_lines]
    lines = [buffer]+lines+[buffer]

def check_move(array,row,col):
    count_rolls = 0
    for row_diff in range(-1,0,2):
        for col_diff in range(-1,0,2):
            if row_diff==0 and col_diff==0:
                continue
            row_coord = row+row_diff
            col_coord = col+col_diff
            count_rolls += 1 if array[col_coord][row_coord] == '@' else 0
            if count_rolls >3:
                return 0  
    return 1


with open('output.txt','w') as file:
    total = 0
    for col in range(1,cols+1):
        for row in range(1,rows+1):
            total += check_move(lines,row,col)
            file.write(lines[col][row])
        file.write('\n')
    print(total)

# Checking output 
with open('output.txt','r') as file1:
    out_lines = file1.readlines()

with open(input) as file2:
    in_lines  = file2.readlines()

for i,j in zip(out_lines,in_lines):
    if i!=j:
        print('mismatch')