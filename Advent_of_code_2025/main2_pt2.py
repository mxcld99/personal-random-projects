import os
from sympy.ntheory import factorint

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input2.txt')

# Reading content of file
with open(input) as file:
    ranges = file.readline()[:-1].split(',')

##################################
# Part 2
##################################

# Splits number into sets
def split_number(number,oom,split):
    interval = int(oom/split)
    number_str = str(number)
    out = []
    for i in range(0,oom,interval):
        out.append(int(number_str[i:i+interval]))
    return out

def blank_start(oom,split):
    return int(f'1{'0'*int(oom/split-1)}')

def blank_end(oom,split):
    return int('9'*int(oom/split))

def generate_full_number(part_num,split):
    return int(str(part_num)*split)

def get_start(start_int,oom,split):
    split_num = split_number(start_int,oom,split)
    proposed_start = generate_full_number(split_num[0],split)
    return split_num[0] if start_int<=proposed_start else split_num[0]+1

def get_end(end_int,oom,split):
    split_num = split_number(end_int,oom,split)
    proposed_end = generate_full_number(split_num[0],split)
    return split_num[0] if end_int>=proposed_end else split_num[0]-1

def get_range_sum(start_val,end_val):
    diff = end_val - start_val
    if diff < 0:
        return 0
    elif diff == 0:
        return start_val
    elif diff % 2 != 0:
        return (start_val+end_val)*(1+diff//2)
    else:
        return (start_val+end_val-1)*(diff/2) + end_val
    
def get_total_to_add(oom,split,start,end):
    range_sum = get_range_sum(start,end)
    interval = int(oom/split)
    out = 0
    for i in range(0,oom,interval):
        out += range_sum * 10**i
    return out

def get_sum_of_all_same(oom,start_int,end_int):
    out = 0
    for i in range(1,10):
        num = int(str(i)*oom)
        if num >= start_int and num <= end_int:
            out+=num
    return out

total = 0
for r in ranges:
    print(f'START:{r}')
    start_str, end_str = r.split('-')
    start_int, end_int = (int(start_str),int(end_str))
    start_oom, end_oom = (len(start_str),len(end_str))

    intermitent_total = 0
    for oom in range(start_oom, end_oom+1):

        # Ignore single digits
        if oom == 1:
            continue

        print(f'STARTING OOM: {oom}')
        prime_factors = factorint(oom)
        num_prime_factors = sum(i for i in prime_factors.values())
        unique_prime_factors = set(prime_factors)
        num_unique_prime_factors = len(unique_prime_factors)
        # print(prime_factors)
        # print(unique_prime_factors)
        # print(num_prime_factors)

        # Accounting for case with no prime factors
        if num_prime_factors == 1:
            intermitent_total += get_sum_of_all_same(oom,start_int,end_int)
            continue
        
        # When there is prime factors, we need to do splits because there are multiple ways to split up the number
        for split in unique_prime_factors:
            print(f'STARTING SPLIT: {split}')
            start = get_start(start_int,oom,split) if start_oom == oom else blank_start(oom,split)
            end = get_end(end_int,oom,split) if end_oom == oom else blank_end(oom,split)
            print(f'START: {start}, END: {end}')
            to_add = get_total_to_add(oom,split,start,end)
            intermitent_total += to_add
            # print(f'TO ADD: {to_add}')

        # We also need to account for the fact that the case where all digits are the same will have been counted more than once
        same_sum = get_sum_of_all_same(oom,start_int,end_int)
        intermitent_total -= same_sum * (num_unique_prime_factors-1)

    total += intermitent_total
    print(f'range: {r}, total:{intermitent_total}\n\n')
    # break

print(total)


##############################
## Note, that this only works for oom <12
## After this point, the subtracting correction factor starts to get more complex.
## - Let s and t be two prime splits for oom
## - s*S = oom & t*T = oom
## - If S and T share a factor X, any repetitions of length X will be repeated in both the s & t splits.
## - For oom < 12 there are no such cases, so this is safe.
## - However, for oom = 12, s=3 & t=2 making S=4 and T=6; both share X=2, meaning we need to account for repeats here also
##############################