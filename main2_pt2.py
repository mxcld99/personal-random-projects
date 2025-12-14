import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input2.txt')

# Reading content of file
with open(input) as file:
    ranges = file.readline()[:-1].split(',')

##################################
# Part 1
##################################

def split_number(number,half_oom):
    number_first_half = number // 10**half_oom
    number_second_half = number - (number_first_half*10**half_oom)
    return number_first_half, number_second_half

def blank_start(half_oom):
    return 10**(half_oom-1)

def blank_end(half_oom):
    return int('9'*half_oom)

def get_start(start_int,half_oom):
    fh,sh = split_number(start_int,half_oom)
    return fh+1 if fh<sh else fh
    
def get_end(end_int,half_oom):
    fh,sh = split_number(end_int,half_oom)
    return fh-1 if fh>sh else fh

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


total = 0
for r in ranges:
    start_str, end_str = r.split('-')
    start_int, end_int = (int(start_str),int(end_str))
    start_oom, end_oom = (len(start_str),len(end_str))

    intermitent_total = 0
    for oom in range(start_oom, end_oom+1):
        if oom%2 != 0:
            continue
        half_oom = int(oom/2)
        start = get_start(start_int,half_oom) if start_oom == oom else blank_start(half_oom)
        end = get_end(end_int,half_oom) if end_oom == oom else blank_end(half_oom)
        range_sum = get_range_sum(start,end)

        intermitent_total += range_sum + (range_sum*10**half_oom)

    total += intermitent_total
    print(f'range: {r}, total:{intermitent_total}')

print(total)
    