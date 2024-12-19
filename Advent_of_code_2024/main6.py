from copy import deepcopy

# Reading in data
input_path = 'input6.txt'
input_array = [list(x[:-1]) for x in open(input_path).readlines()]
original_array = deepcopy(input_array)

row_count = len(input_array)
col_count = len(input_array[0])

# Defining the cycle of directions that the guard goes through
# up,right,down,left. Each is assigned an ID and they are cycled through using mod 4 when an obstacle is hit.
direction_cycle = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

# Finds the starting point in the array
def find_starting_point(array):
    for r,row in enumerate(array):
        for c,char in enumerate(row):
            if char == '^':
                return r,c

# Counts the number of X's in the array when done
def count_positions_visited(array):
    count=0
    for r,row in enumerate(array):
        for c,char in enumerate(row):
            if char == 'X':
                count+=1
    return count

# Increments the direction ID by 1 mod 4 so that the direction is cyclical
def change_direction(current_dir_id):
    new_dir_id = (current_dir_id+1)%4
    return new_dir_id

# Takes the position supplied and calculates the next position based on the direction ID supplied
def project_position(current_pos,current_dir_id):
    current_dir = direction_cycle[current_dir_id]
    next_pos = tuple(map(sum, zip(current_pos, current_dir)))
    return next_pos

# Checks whether the next position is off the map
def check_map_exit(array,current_pos,current_dir_id):
    next_pos = project_position(current_pos,current_dir_id)
    return not(0<=next_pos[0]<=row_count-1 and 0<=next_pos[1]<=col_count-1)

# Checks whether the next position is an obstacle
def check_obstacle(array,current_pos,current_dir_id):
    next_pos = project_position(current_pos,current_dir_id)
    return array[next_pos[0]][next_pos[1]] == '#'

# Function to move the guard one step.
# Firstly it turns the current tile into an X, prior to moving
# If the move takes the guard off the map it returns False, False
# If not, it returns the position and direction post move.
def move(array,current_pos,current_dir_id):
    # Assigning X to current pos
    array[current_pos[0]][current_pos[1]] = 'X'

    # Is the next pos off map
    if check_map_exit(array,current_pos,current_dir_id):
        return False,False

    # Until an obstacle is not encountered in the path of the guard, the task of changing direction, checking for an exit then checking for an obstacle repeats
    while check_obstacle(array,current_pos,current_dir_id):
        current_dir_id = change_direction(current_dir_id)
        if check_map_exit(array,current_pos,current_dir_id):
            return False,False

    # Returns next pos and direction
    return project_position(current_pos,current_dir_id),current_dir_id

## Debugging
out_file = 'out.txt'
with open(out_file,'w') as f:
    pass
def write_to_out(array):
    with open(out_file,'a') as f:
        for line in array:
            f.write(''.join(line)+'\n')
        f.write('\n\n------------------------------------------------------------------------------------------------------------------\n\n')

# Initialising starting conditions
current_pos = find_starting_point(input_array)
current_dir_id = 0

# Cycling through movement
while current_pos:
    current_pos,current_dir_id = move(input_array,current_pos,current_dir_id)

    # ## Debugging
    # write_to_out(input_array)
    # print(current_pos)

# Calculating answer
part1ans = count_positions_visited(input_array)
print('Part 1: ',part1ans)



## For part 2, we need to cycle through additions of obstacles and see if they create a loop
## Only obstacles in place of where the guard goes in their original path can affect them
## We can detect whether the guard is stuck in a loop if they make it back to a position they have already been in
## AND are going in the same direction that they were previously.

def generate_dir_array(array):
    row_count = len(array)
    col_count = len(array[0])
    out = [[[] for i in range(col_count)] for j in range(row_count)]
    return out

# Updating the move function to check if the starting position is reached again with an up dir
def move2(array,current_pos,current_dir_id,dir_array):

    # If guard is back at a square they have already been at, in a direction they were already facing, then there is a loop
    dir_array_values = dir_array[current_pos[0]][current_pos[1]]
    if current_dir_id in dir_array_values:
        return 'LOOP','LOOP'
    dir_array[current_pos[0]][current_pos[1]].append(current_dir_id)
    
    # Assigning X to current pos
    array[current_pos[0]][current_pos[1]] = 'X'

    # Is the next pos off map
    if check_map_exit(array,current_pos,current_dir_id):
        return False,False

    # Until an obstacle is not encountered in the path of the guard, the task of changing direction, checking for an exit then checking for an obstacle repeats
    while check_obstacle(array,current_pos,current_dir_id):
        current_dir_id = change_direction(current_dir_id)
        if check_map_exit(array,current_pos,current_dir_id):
            return False,False

    # Returns next pos and direction
    return project_position(current_pos,current_dir_id),current_dir_id

# Invoking a solver function, for tidier code.
def solve_array(func_array,starting_pos,current_dir_id,dir_array):
    current_pos = starting_pos
    while current_pos and current_pos != 'LOOP':
        current_pos,current_dir_id = move2(func_array,current_pos,current_dir_id,dir_array)
    return current_pos

counter = 0 #Counting instances where a loop is created
starting_pos = find_starting_point(original_array)
base_dir_array = generate_dir_array(original_array)

row_count = len(original_array)
for ri,row in enumerate(input_array):
    print(f'{ri}/{row_count}')
    for ci,col in enumerate(row):
        if col == 'X' and (ri,ci) != starting_pos:
            dir_array = deepcopy(base_dir_array)
            
            edited_array = deepcopy(original_array)
            edited_array[ri][ci] = '#'
            current_dir_id = 0
            result = solve_array(edited_array,starting_pos,current_dir_id,dir_array)
            if result == 'LOOP':
                counter+=1
        
# Returns number of obstacles that can cause a loop
print(f'Part 2: {counter}')
    
    
