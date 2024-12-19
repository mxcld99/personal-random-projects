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

def get_operator_perms(operators,number_of_operators):
    if number_of_operators == 1:
        for operator in operators:
            yield [operator]
    else:
        for operator in operators:
            internal_perm_gen = get_operator_perms(operators,number_of_operators-1)
            for internal_perm in internal_perm_gen:
                yield [operator] + internal_perm

def check_solvable(operators,number_list,target_val):
    permutations = get_operator_perms(operators,len(number_list)-1)
    match = False
    for p in permutations:
        tot = number_list[0]
        for o,n in zip(p,number_list[1:]):
            if o == '+':
                tot+=n
            elif o == '*':
                tot*=n
            elif o == '||':
                order_n = len(str(n))
                tot = tot*(10**order_n) + n
            else:
                raise ValueError('Invalid Operator')
        if tot == target_val:
            match=True
            break
    return match

## Test
operators = ['+','*']
perm_gen = get_operator_perms(operators,5)
for i in perm_gen:
    print(i)
    
# Running
to_process = read_in_equations(path)
total_to_do = len(to_process)
count1=0
count2=0
operators1 = ['+','*']
operators2 = ['+','*','||']

for i_val , (target_value,number_list) in enumerate(to_process.items()):
    print(f'Starting {i_val}/{total_to_do}')
    l = len(number_list)
    match = check_solvable(operators1,number_list,target_value)
    if match:
        count1+=target_value
    if not match:
        match = check_solvable(operators2,number_list,target_value)
    if match:
        count2+=target_value
    

print(f'Part 1 ans: {count1}')
            
print(f'Par 2 ans: {count2}')
