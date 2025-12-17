import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input6.txt')

# Reading content of file
with open(input) as file:
    lines = [i[:-1] for i in file.readlines()]

#########################
## Part 1
#########################

number_lists = [i.split(' ') for i in lines[:-1]]
operations = lines[-1].split(' ')

def get_next(in_list):
    while len(in_list)>0:
        out = in_list.pop(0)
        if out!='':
            return out
    return False

def perform_operation(numbers,operation):
    start = numbers[0]
    for n in numbers[1:]:
        if operation=='*':
            start*=n
        else:
            start+=n
    return start

total = 0
while True:
    # Get operation to perform
    operation = get_next(operations)
    # if no operation found it's the end of the operation list
    if not operation:
        break

    numbers = []
    for number_list in number_lists:
        numbers.append(int(get_next(number_list)))
    
    # print(operation, numbers)
    total+=perform_operation(numbers, operation)

print('PART 1: ', total)