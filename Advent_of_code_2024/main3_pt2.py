valid_beginning='mul('
valid_nums='1234567890'
valid_do='do()'
valid_dont="don't()"


# Part 1 & 2

def check_mul(string):
    found = string[:4]==valid_beginning
    return found, (string[4:] if found else string[1:])

def check_dont(string):
    found = string[:7]==valid_dont
    return found, (string[7:] if found else string[1:])

def check_do(string):
    found = string[:4]==valid_do
    return found, (string[4:] if found else string[1:])

def check_do_dont(string,existing_do_dont_value):
    do_found, do_str = check_do(string)
    if do_found:
        return 1,do_str
    dont_found, dont_str = check_dont(string)
    if dont_found:
        return 0,dont_str
    return existing_do_dont_value,string

def check_nums(string):
    # max number of digits is 3 for each number so the max. length of the whole expression is mul(123,456)
    # mul( makes up 4, the rest 8
    sub_string = string[:8]

    # Close bracket must be present between index 3 or later the sub-string to be valid,
    # as the min distance between the open bracket and closed is 4, as the smallest valid expression is 2 single digit no.'s
    if ')' in sub_string[3:]:
        closed_bracket_index = sub_string.index(')')

        # ',' must be a minimum distance of 1 character away from the open and closed brackets
        if ',' in sub_string[1:closed_bracket_index-1]:
            sub_string_numbers = sub_string[:closed_bracket_index].split(',')

            # If there are more than 1 comma's, the expression is invalid
            if len(sub_string_numbers)!=2:
                return 0,string[1:]

            mult_total = 1
            for number_text in sub_string_numbers:
                for character in number_text:

                    # If there are any invalid characters in numbers, 
                    if not character in valid_nums:
                        return 0,string,string[1:]
                mult_total*=int(number_text)

            return mult_total, string[closed_bracket_index+1:]
            
        else:
            # If there is no ',', then the expression cannot be complete.*
            return 0,string[1:]
    else:
        # If there is no ')', then the expression cannot be complete.*
        return 0,string[1:]

# *There could still be another valid mul( expression starting within these 8 characters
# so we can't afford to exclude them from the next iteration of the check

# # Tests
# t1 = 'mul(123,100)'
# t2 = '23198shmul(123,100)dm&mul(34,deh7h(320j99)mdi&()mul(67,9)37y&H'
# r1 = check_mul(t1)
# t3 = "!*^mul(363,974)&(how()'mul(307,210)(:]+$:!why()%@mul(542,323)&(when()"
# running_string=t3

input_path = 'input3.txt'
with open(input_path) as f:
    lines=f.readlines()
running_string = '*'.join(lines)

running_total=0
do_dont_value = 1
while len(running_string)>=8:
    do_dont_value, running_string = check_do_dont(running_string,do_dont_value)
    found,running_string = check_mul(running_string)
    if found:
        # init_str=running_string ## Debug
        mult_result,running_string = check_nums(running_string)
        # print('mul('+init_str[:8],mult_result,running_string[:15]) ## Debug
        running_total+=mult_result*do_dont_value
print(running_total)
    