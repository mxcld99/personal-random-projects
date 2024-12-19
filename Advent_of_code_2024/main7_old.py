from itertools import permutations

path = 'input7.txt'

# Function to read in values from input file
def read_in_equations(input_path):
    with open(input_path,'r') as f:
        content = f.readlines()
    out = {}
    for line in content:
        total,numbers = line.split(': ')
        numbers = [int(x) for x in numbers[:-1].split(' ')]
        out[int(total)] = numbers
    return out

# Find the absolute upper limit value from operating with supplied numbers
def get_upper_limit(number_list):
    total = number_list[0]
    for n in number_list[1:]:
        if n==0:
            total+=n
        elif n==1:
            total+=n
        else:
            total*=n
    return total

# Find the absolute lower limit value from operating with supplied numbers
def get_lower_limit(number_list):
    total = number_list[0]
    for n in number_list[1:]:
        if n==0:
            total*=n
        elif n==1:
            total*=n
        else:
            total+=n
    return total

# Test upper and lower limits
def test_limits(total_num,number_list):
    ll = get_lower_limit(number_list)
    ul = get_upper_limit(number_list)
    if ll<=total_num<=ul:
        return 1
    else:
        return 0



# Running
to_process = read_in_equations(path)
count=0
total_items = len(to_process)
for i,(num,ls) in enumerate(to_process.items()):

    if i%100==0:
        print(f'Starting {i}/{total_items}')
    
    # Test limits first as initial check
    limits_test = test_limits(num,ls)
    count+=limits_test*num
    
print(f'Part 1: {count}')


######################################################
# ## Brute force approach tried below, takes wayyyyyyy too long
######################################################
# # Generate operator permutations for a given number os plus and mult operators
# def generate_operator_perms(pluses,multiplies):
#     l = ['+']*pluses + ['*']*multiplies
#     return permutations(l)

# # generate all operator perms
# def generate_all_operator_perms(list_length):
#     out = []
#     for i in range(list_length):
#         pluses = i
#         multiplies = list_length - i
#         perms = generate_operator_perms(pluses,multiplies)
#         out.append(perms)
#     return out

# def calc_total_from_perm(num_list,perm):
#     out = num_list[0]
#     for symbol,num in zip(perms,num_list[1:]):
#         if symbol == '+':
#             out+=num
#         else:
#             out*=num
#     return out

# perm_dict = {}
# for i,(num,ls) in enumerate(to_process.items()):

#     print(f'Starting {i}/{total_items}')
    
#     # Test limits first as initial check
#     limits_test = test_limits(num,ls)

#     # If limits are deemed acceptable, move onto brute force approach
#     if limits_test == 1:
#         list_length = len(ls)
#         perms = perm_dict.get(list_length,None)
#         if perms is None:
#             perms = generate_all_operator_perms(list_length)
#             perm_dict[list_length] = perms

#         to_break = False
#         for perm_group in perms:
#             for perm in perm_group:
#                 t = calc_total_from_perm(ls,perm)
#                 if t==num:
#                     count+=1
#                     to_break = True
#                     break
#             if to_break:
#                 break
# print(count)