import os
from sympy.ntheory import factorint

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input3.txt')

# Reading content of file
with open(input) as file:
    lines = [[int(j) for j in list(i[:-1])] for i in file.readlines()]

##############################
# Part 1
##############################

total = 0
for line in lines:

    maxnum = 0
    pos = 0
    for i,num in enumerate(line[:-1]):
        if num>maxnum:
            maxnum = num
            pos = i
    total+=10*maxnum

    maxnum = 0
    for i,num in enumerate(line[pos+1:]):
        if num>maxnum:
            maxnum=num
    total+=maxnum

print('PART 1: ', total)


##############################
# Part 2
##############################
# Clycles through using some simple rules - for digits 12-1
# 1. Search through the list for the left-most instance of the highest number across list [offset:digit-1] (offset=0 for digit=12)
# 2. Set offset to prior offset + relative position of highest digit + 1 ; this is so that the start point in the next digit search only includes those to the right of the last digit

total = 0
for line in lines:
    offset = 0
    print(''.join([str(i) for i in line]))
    line_total = 0
    for oom in range(11,-1,-1):
        print(oom,offset)
        maxnum = 0
        pos = 0

        ## Zero edge-case
        if oom == 0:
            for i,num in enumerate(line[offset:]):
                if num>maxnum:
                    maxnum = num
                    pos = i
        
        else:
            for i,num in enumerate(line[offset:-oom]):
                if num>maxnum:
                    maxnum = num
                    pos = i

        line_total+=maxnum*(10**oom)
        offset = offset+pos+1
        print(line_total)
    total+=line_total

print('PART 2: ', total)