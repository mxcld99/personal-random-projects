import os
from sympy.ntheory import factorint

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input4.txt')

# Reading content of file
with open(input) as file:
    read_lines = [i[:-1] for i in file.readlines()]
    cols = len(read_lines[0])
    rows = len(read_lines)
    buffer = list('.'*(cols+2))
    lines = [list('.'+i+'.') for i in read_lines]
    lines = [buffer]+lines+[buffer]

###########################
## Part 1
###########################

def check_move(array,col,row,debug=False):
    count_rolls = 0
    print_str = ''
    for row_diff in range(-1,2):
        for col_diff in range(-1,2):
            col_coord = col+col_diff
            row_coord = row+row_diff
            char = array[row_coord][col_coord]
            print_str+=char
            if col_diff==0 and row_diff==0:
                continue
            count_rolls += 1 if array[row_coord][col_coord] == '@' else 0
            if count_rolls >3:
                return 0  
        print_str+='\n'
    if debug:
        print('\n')
        print(print_str)
        print('Roll count: ',count_rolls)
    return 1


total = 0
for row in range(1,rows+1):
    for col in range(1,cols+1):
        if lines[row][col]!='@':
            continue
        total += check_move(lines,col,row,debug=False)

print(total)

###########################
## Part 2
###########################

some_removed = True
current_array = lines
total_removed = 0
iteration = 1
while some_removed:
    new_array = []
    removed_this_loop = 0
    # print(len(current_array[0]))
    # print(len(current_array))
    for row in range(1,rows+1):
        new_row = ['.']

        for col in range(1,cols+1):
            if current_array[row][col]!='@':
                new_row.append('.')
                continue
            move_check = check_move(current_array,col,row,debug=False)
            if move_check:
                new_row.append('.')
            else:
                new_row.append('@')
            removed_this_loop += move_check

        new_row.append('.')
        new_array.append(new_row.copy())

    current_array = [buffer]+new_array.copy()+[buffer]
    some_removed = removed_this_loop > 0
    total_removed+=removed_this_loop
    print(f'Iteration {iteration} complete. Removed: {removed_this_loop}')
    iteration += 1

print(total_removed)