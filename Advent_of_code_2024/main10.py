from copy import deepcopy

# Defining search vectors, around which to look for the next trail square
search_vectors = [(1,0),(-1,0),(0,1),(0,-1)]

# Generator to generate positions of starts in the array
def find_start_positions(map_array):
    for ir,row in enumerate(map_array):
        for ic,char in enumerate(row):
            if char == 0:
                yield (ir,ic)

# Moves a given position by the given vector and returns the new point
# If the new point is off the array, it returns None
def new_pos(current_pos,vector,map_array):
    rows = len(map_array)
    cols = len(map_array[0])
    new_pos_ri = current_pos[0]+vector[0]
    new_pos_ci = current_pos[1]+vector[1]
    if (0<=new_pos_ri<rows and 0<=new_pos_ci<cols):
        return new_pos_ri,new_pos_ci
    else:
        return None
    
# Recursive function to find the number of trails from a certain starting point
def find_trail_order(map_array,current_pos,search_order,to_print=False):
    trail_count = 0
    current_height = map_array[current_pos[0]][current_pos[1]]
    if current_height == '.':
        return 0
    search_height = current_height+1
    if search_order == 9:
        if current_height == 9:
            
            ######################################
            ## Comment this line out for part 2 ##
            ######################################
            # map_array[current_pos[0]][current_pos[1]] = '.'
            
            return 1
        else:
            return 0
    elif search_order == current_height:
        for search_vector in search_vectors:
            pos_to_try = new_pos(current_pos,search_vector,map_array)
            if not pos_to_try is None:
                trail_count += find_trail_order(map_array,pos_to_try,search_height,to_print=to_print)
        return trail_count
    else:
        return 0

# ## Testing
# example = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""
# input_lines = example.split('\n')
# map_array = list(list(int(y) for y in list(x)) for x in input_lines)

# Parsing input
path = 'input10.txt'
input_lines = open(path).readlines()
map_array = list(list(int(y) for y in list(x[:-1])) for x in input_lines)

trailhead_count = 0
start_pos_generator = find_start_positions(map_array)
for i,start_pos in enumerate(start_pos_generator):
    if i==3:
        tp=True
    else:
        tp=False
    map_array_copy = deepcopy(map_array)
    count = find_trail_order(map_array_copy,start_pos,0,to_print=tp)
    trailhead_count += count

print(trailhead_count)