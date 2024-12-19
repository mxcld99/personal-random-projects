import numpy as np
from scipy.ndimage import rotate

dirs = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

# Checking for Xmas in all 8 directions
def count_XMAS(matrix,row_i,col_i):
    count = 0
    if matrix[row_i][col_i]=='X':
        for direction in dirs:
            x_diff,y_diff = direction
            if matrix[row_i+y_diff][col_i+x_diff] == 'M':
                if matrix[row_i+y_diff*2][col_i+x_diff*2] == 'A':
                    if matrix[row_i+y_diff*3][col_i+x_diff*3] == 'S':
                        count+=1
    return count

# Checking for X-mas in all 4 rotations
def count_X_MAS(matrix,row_i,col_i):
    if matrix[row_i,col_i]=='A':
        sub_array = np.array([x[col_i-1:col_i+2] for x in matrix[row_i-1:row_i+2]])
        for rot in range(0,4):
            sub_array = np.rot90(sub_array,k=rot)
            if sub_array[0,0]=='M':
                if sub_array[0,2]=='M':
                    if sub_array[2,0]=='S':
                        if sub_array[2,2]=='S':
                            return 1
    return 0
        

# Read in the input
input_path = 'input4.txt'
input_array = np.array([list(x[:-1]) for x in open(input_path).readlines()])

# Part 1
wordsearch_matrix=np.pad(input_array,3,mode='constant')

total_XMAS = 0
for row_i, row in enumerate(wordsearch_matrix[3:-3],start=3):
    for col_i,letter in enumerate(row[3:-3],start=3):
        total_XMAS+=count_XMAS(wordsearch_matrix,row_i,col_i)

print('Part 1: ',total_XMAS)


# Part 2
total_X_MAS = 0
for row_i, row in enumerate(input_array[1:-1],start=1):
    for col_i,letter in enumerate(row[1:-1],start=1):
        total_X_MAS+=count_X_MAS(input_array,row_i,col_i)

print('Part 2: ',total_X_MAS)