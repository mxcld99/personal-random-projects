def get_lists(path):
    with open(path) as f:
        l = f.readlines()
    out1=[]
    out2=[]
    for line in l:
        ls = line[:-1].split('   ')
        out1.append(int(ls[0]))
        out2.append(int(ls[1]))
    return out1,out2

## General
path_to_input = 'input.txt'
lists =get_lists(path_to_input)
sorted_lists = list(map(lambda x: sorted(x),lists))

## Part 1
out = 0
for l1,l2 in zip(sorted_lists[0],sorted_lists[1]):
    out+=abs(l1-l2)
print('Part 1 answer: ',out)

## Part 2
left_list = sorted_lists[0]
right_list = sorted_lists[1]
tot=0
for l_val in left_list:
    r_val=right_list[0]
    i=0
    while r_val<=l_val:
        if r_val==l_val:
            tot+=l_val
        i+=1
        r_val=right_list[i]

print('Part 2 answer: ',tot)