#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    out = copy.deepcopy(matrix)
    m = len(matrix)
    n = len(matrix[0])
    for i in range(1, n):
        out[m-1][i] = matrix[m-1][i-1]
    for i in range(m-2, -1, -1):
        out[i][n-1] = matrix[i+1][n-1]
    for i in range(n-2, -1, -1):
        out[0][i] = matrix[0][i+1]
    for i in range(1, m):
        out[i][0] = matrix[i-1][0]


    for i in range(2, n-1):
        out[m-2][i] = matrix[m-2][i-1]




        
        
        
    

    for i in range(m):
        line = ""
        for j in range(n):
            line += str(out[i][j]) + " "
        print(line)
    
    
    
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
