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


#########################
## Part 2
#########################

numbers = [list(i) for i in lines[:-1]]
operations = lines[-1].split(' ')
numbers_per_operation = len(numbers)
total = 0
while True:
    # Getting operation
    operation = get_next(operations)
    # if no operation found it's the end of the operation list
    if not operation:
        break

    number_strings = []
    blank_count = 0

    # Stopping condition when there is a fully blank column - signifies new calc
    while blank_count < numbers_per_operation:
        blank_count = 0
        number_strings.append('')

        # If the end of the file is reached
        if len(numbers[0])==0:
            break
        
        # Going column by column and recording the number in that column
        for i in range(numbers_per_operation):
            item = numbers[i].pop(0)
            if item == ' ':
                blank_count+=1
            else:
                number_strings[-1] += item

    # There will always be one more blank string added to the list than necessary
    number_strings.pop(-1)

    # print(number_strings)

    # Turning strings into numbers and calculating the output of the calculation    
    number_ints = [int(i) for i in number_strings]
    total += perform_operation(number_ints,operation)

print('PART 2: ', total)
        
    
