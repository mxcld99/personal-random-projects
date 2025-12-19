import os
from functools import lru_cache
import time as t

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
input = os.path.join(os.getcwd(),'input10.txt')

# Reading content of file
with open(input) as file:
    lines = [i[:-1].split(' ') for i in file.readlines()]

def buttons_to_bits(buttons,final_length):
    out_list = []
    for button in buttons:
        out = 0
        for b in button:
            out+=2**(final_length-b-1)
        out_list.append(out)
    return out_list

def final_state_to_bits(button):
    out = 0
    for i,char in enumerate(button[::-1]):
        out+=0 if char=='.' else 2**i
    return out

final_states_raw = [i[0][1:-1] for i in lines]
final_states_lengths = [len(i) for i in final_states_raw]
final_states = [final_state_to_bits(i) for i in final_states_raw]

buttons = [buttons_to_bits([tuple(int(k) for k in j[1:-1].split(',')) for j in i[1:-1]],L) for i,L in zip(lines,final_states_lengths)]
joltages = [tuple(int(j) for j in i[-1][1:-1].split(',')) for i in lines]

# print(final_states[0])
# print(final_state_lengths[0])
print(bin(final_states[0]))
# print(joltages[0])

###################
## Part 1
###################

# Iniitial thoughts are that a breadth-first search algorithm is the best approach for pt 1
total_presses_overall = 0
total_to_do = len(final_states)

for i, final_state, button_list in zip(range(1,total_to_do+1), final_states, buttons):
    
    # print(f'Starting {i}/{total_to_do}')

    # Initially all buttons are off
    state_cache = set([0b0])
    depth = 1
    to_break = False
    # print(f'Final state: {bin(final_state)}')

    while True:
        # print(f'Starting depth {depth}\nState cache: {[bin(i) for i in state_cache]}')

        # Generating a new state map
        new_state_cache = set()

        # Running through all possible buttons
        for button in button_list:

            # Running through all states the indicators could be in
            for state in state_cache:

                # Trialling the new state if the button is pressed
                new_state = button^state
                if new_state == final_state:
                    to_break = True
                    break
                
                new_state_cache.add(new_state)
            if to_break:
                break
        if to_break:
            break
        
        state_cache = new_state_cache

        depth+=1
        # t.sleep(2)

    total_presses_overall+=depth

print('PART 1: ',total_presses_overall)
