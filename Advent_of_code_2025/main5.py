import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input5.txt')

# Reading content of file
with open(input) as file:
    lines = [i[:-1] for i in file.readlines()]
ranges = []
numbers = []
for line in lines:
    if '-' in line:
        ranges.append(tuple(int(i) for i in line.split('-')))
    elif line!='':
        numbers.append(int(line))

################################
## Part 1
################################

# Consolodating ranges - overlapping ones are merged
final_ranges = []
for range in ranges:
    found_place = False
    for i,final_range in enumerate(final_ranges):
        # check if this range is below the one being checked
        if final_range[0]>range[1]:
            found_place = True
            final_ranges.insert(i,range)
            break
        # Check if this range is above the one being checked
        elif final_range[1]<range[0]:
            continue
        # Only remaining case is that they overlap in some way, so we combine them
        else:
            new_range = (min(final_range[0],range[0]),max(final_range[1],range[1]))
            final_ranges[i] = new_range
            found_place = True
            break
    # if it's not found, it must be larger than the other ranges
    if not found_place:
        final_ranges.append(range)

# Now checking how many numbers fit into any range
total = 0
for number in numbers:
    to_break = False
    for final_range in final_ranges:

        # if it's below the range it's not included
        if number < final_range[0]:
            to_break = True
            break
        
        # is it above the bottom end
        if number>=final_range[0]:
            # is it below the top end
            if number<=final_range[1]:
                total+=1
                to_break = True
                break
            # Must be above the top end so try next range
            else:
                continue

print('PART 1: ',total)

################################
## Part 2
################################
# For what feels like the first time ever my part 1 solution has actually been constructed in a way that benefits pt 2. It's a rare moment

# First pass
total_fresh = 0
for final_range in final_ranges:
    to_add = final_range[1]-final_range[0]+1
    total_fresh += to_add
    print(final_range,to_add)

print('PART 2 (attempt 1): ',total_fresh)

# Apparently this gives an answer that's too high...