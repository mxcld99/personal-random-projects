path = 'input8.txt'

# Reads input into a workable array
def get_grid(path_to_grid):
    with open(path_to_grid) as f:
        lines = f.readlines()
    return [list(line[:-1]) for line in lines]

# Makes a blank grid of 0's to record where antinodes are
def get_node_grid(grid):
    return [[0 for x in row] for row in grid]

# Turning the antenna grid into a dict of lists
# key is the character and value is the list of postions of that character
def get_antenna_dict(grid):
    out = {}
    for ri,row in enumerate(grid):
        for ci,ch in enumerate(row):
            if not ch=='.':
                out[ch] = out.get(ch,[])
                out[ch].append((ri,ci))
    return out

# Generating combinations of antenna positions
def antenna_combo_generator(pos_list):
    for i,pos_1 in enumerate(pos_list[:-1],start=1):
        for pos_2 in pos_list[i:]:
            yield (pos_1,pos_2)


# Get node positions from a given pair of antenna
def get_node_positions(a1,a2):
    a1_to_a2 = a2[0]-a1[0],a2[1]-a1[1]
    p1 = a1[0]-a1_to_a2[0],a1[1]-a1_to_a2[1]
    p2 = a2[0]+a1_to_a2[0],a2[1]+a1_to_a2[1]
    return p1,p2

# Get node positions from a given pair of antenna
def get_node_positions2(a1,a2,node_map):
    a1_to_a2 = a2[0]-a1[0],a2[1]-a1[1]
    out = []
    map_cols = len(node_map[0])
    map_rows = len(node_map)

    current_pos = a1[0],a1[1]
    while 0<=current_pos[0]<map_rows and 0<=current_pos[1]<map_cols:
        out.append(current_pos)
        current_pos = current_pos[0]-a1_to_a2[0],current_pos[1]-a1_to_a2[1]
        
    current_pos = a2[0],a2[1]
    while 0<=current_pos[0]<map_rows and 0<=current_pos[1]<map_cols:
        out.append(current_pos)
        current_pos = current_pos[0]+a1_to_a2[0],current_pos[1]+a1_to_a2[1]
        
    return out

def mark_out_node(map_to_mark,node_pos):
    rows = len(map_to_mark)
    cols = len(map_to_mark[0])
    on_map = True
    for map_dim,node_coord in zip((rows,cols),node_pos):
        if not 0<=node_coord<map_dim:
            on_map=False
            break
    if on_map:
        map_to_mark[node_pos[0]][node_pos[1]] = '.'

# Mark antinodes on antinode map for a given pair of antenna
def mark_nodes(map_to_mark,a1,a2):
    node_positions = get_node_positions(a1,a2)
    for node_pos in node_positions:
        mark_out_node(map_to_mark,node_pos)

# Mark antinodes on antinode map for a given pair of antenna
def mark_nodes2(map_to_mark,a1,a2):
    node_positions = get_node_positions2(a1,a2,map_to_mark)
    for node_pos in node_positions:
        mark_out_node(map_to_mark,node_pos)

# Counting antinodes in map
def count_antinodes(node_map):
    count = 0
    for l in node_map:
        for c in l:
            count += 1 if c=='.' else 0
    return count

# ## Checking functions
# l = [1,2,3,4,5]
# g = antenna_combo_generator(l)
# for i in g:
#     print(i)

antenna_grid = get_grid(path)
node_grid = get_node_grid(antenna_grid)
antenna_dict = get_antenna_dict(antenna_grid)

# ## Debugging
# a2= [5,6]
# a1= [3,10]
# mark_out_node1(node_grid,a1)
# mark_out_node1(node_grid,a2)
# ps = get_node_positions(a1,a2)
# for p in ps:
#     print(p)
#     mark_out_node(node_grid,p)
# for l in node_grid:
#     print(''.join(str(x) for x in l))

for ch, pos_list in antenna_dict.items():
    combo_gen = antenna_combo_generator(pos_list)
    for a1,a2 in combo_gen:
        mark_nodes(node_grid,a1,a2)

# ## Debugging
# for l in node_grid:
#     print(''.join(str(x) for x in l))

node_count = count_antinodes(node_grid)

print(f'Part 1: {node_count}')


node_grid2 = get_node_grid(antenna_grid)
for ch, pos_list in antenna_dict.items():
    combo_gen = antenna_combo_generator(pos_list)
    for a1,a2 in combo_gen:
        mark_nodes2(node_grid2,a1,a2)
node_count2 = count_antinodes(node_grid2)

print(f'Part 2: {node_count2}')