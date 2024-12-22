# Parses memory into a list of memory blocks and blank blocks
def parse_memory(memory):
    out = [[],[]]
    for i,b in enumerate(memory):
        out[i%2].append(int(b))
    return out

path='input9.txt'
input_mem = open(path).readline()
if len(input_mem)%2==0:
    input_mem = input_mem[:-1]

## Testing
# input_mem = '12345678922222'


################
#### Part 1 ####
################
used_memory,blank_memory = parse_memory(input_mem)
end_block_index = len(used_memory)-1
end_write_queue = []

# Generating the output memory
output_memory = []
for bi,b in enumerate(used_memory):
    output_memory+= [bi]*b
    blank_block_len = blank_memory.pop(0)
    while len(end_write_queue)<blank_block_len:
        end_write_queue+=[end_block_index]*used_memory.pop()
        end_block_index-=1
    for i in range(blank_block_len):
        # print(output_memory)
        output_memory.append(end_write_queue.pop(0))

# Generating the memory
for i in end_write_queue:
    output_memory.append(i)

# Calculating checksum
checksum_total = 0
for i,n in enumerate(output_memory):
    checksum_total+=i*n

print(f'Part 1: {checksum_total}')

# ## Debugging
# print(''.join(str(x) for x in output_memory))


################
#### Part 2 ####
################
used_memory,blank_memory = parse_memory(input_mem)
end_block_index = len(used_memory)-1
end_write_queue = []

# Creating a dict to store the ammount of free space remaining in each blank block
space_remaining_dict = dict((i,m) for i,m in enumerate(blank_memory))

# Creating a dict to store the memory blocks stored in each blank block
fill_dict = dict((i,{}) for i,_ in enumerate(blank_memory))

# Finding out where the blocks can fit and recording this
moved_list = []
for i,block in enumerate(used_memory[::-1]):
    i = end_block_index-i
    for empty_block_index, space in space_remaining_dict.items():
        if space>=block:
            space_remaining_dict[empty_block_index] -= block
            fill_dict[empty_block_index][i] = block
            moved_list.append(i)
            break
        if empty_block_index+1 == i:
            break

# ## Debugging
# l = list(fill_dict.keys())
# print(l[:10])
# print(l[-10:])

# Generating the final memory list
output_memory = []
for block_index,mem_block in enumerate(used_memory):
    if block_index in moved_list:
        output_memory += [0]*mem_block
    else:
        output_memory += [block_index]*mem_block
        
    if block_index<end_block_index:
        for k,v in fill_dict[block_index].items():
            output_memory += [k]*v

        output_memory += [0]*space_remaining_dict[block_index]

# Calculating checksum
checksum_total2 = 0
for i,n in enumerate(output_memory):
    checksum_total2+=i*n

print(f'Part 2: {checksum_total2}')