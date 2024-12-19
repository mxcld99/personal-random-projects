rules_input='input5a_rules.txt'
updates_input='input5b_updates.txt'
rules_raw = [x[:-1].split('|') for x in open(rules_input).readlines()]
updates_raw = [x[:-1].split(',') for x in open(updates_input).readlines()]

# ## Debug
# print(rules_raw[:5])

## Making a dictionary in which we have each page number as the key, with a list of any pages that must be printed after in it in the value
rules_dict = {}
for rule_before,rule_after in rules_raw:
    rules_dict[rule_before] = rules_dict.get(rule_before,set())
    rules_dict[rule_before].add(rule_after)

# ## Debug
# for k,v in rules_dict.items():
#     print(k,v)

running_total_pt1=0
running_total_pt2=0
for update in updates_raw:
    bad_update=False

    ## Part 1
    # Now for each update, we do the following:
    # 1. Start at the last value.
    # 2. For all entries before, create a set.
    # 3. Find the intersection between all items in this set and the corresponding rules_dict set.
    # 4. If there is any intersection, the update is not valid.
    # 5. If there is no intersection, calculate the middle index and add to the running total.
    # 6. Repeat the above until the first character is reached. This one does not need to be checked because it comes first.
    
    for end_index,number in enumerate(reversed(update[1:]),start=1):
        rules_set = rules_dict.get(number,set())
        check_set = set(update[:-end_index])
        if not len(rules_set.intersection(check_set))==0:
            bad_update=True
            break
    if not bad_update:
        running_total_pt1+=int(update[int((len(update)-1)/2)])

    ## Part 2
    # If update is bad...
    else:
        # 1. For every number in the list, get the rules_dict and trim set down to only include the intersection between it and those in the update
        # 2. Find the number that has the count of values requiring as being listed before it at exactly the halfway point
        # 3. Add this number to the total
        # This works because of the following. Let's say we have an update including 3 numbers in the wrong order. One of these numbers will require 2 numbers appear after it, another 1 and the final 0.
        # This is the only way that this condition can be satisfied. As a result, the number requiring only 1 be after it must fall in the middle.
        # The same can be said for a list of 7. If you intersect each number's dict with those in the list, it will result in sets of length 6,5,4,3,2,1,0.
        # The one with the middle length must be the one that falls in the middle of the ordered list.
        current_rules_dict = {}
        update_set = set(update)
        for number in update:
            if len(rules_dict[number].intersection(update_set)) == (len(update)-1)/2:
                running_total_pt2 += int(number)
                break
        
        

print('Part 1: ',running_total_pt1)
print('Part 1: ',running_total_pt2)

