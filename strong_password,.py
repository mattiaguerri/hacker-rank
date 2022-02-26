#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    res = 0
    
    spec = ["!","@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
    
    count_u = 0
    count_l = 0
    count_d = 0
    count_s = 0
    for i in range(n):
        if password[i].isupper():
            count_u += 1
        if password[i].islower():
            count_l += 1
        if password[i].isdigit():
            count_d += 1
        if password[i] in spec:
            count_s += 1

    if count_u == 0:
        res+=1
    if count_l == 0:
        res+=1
    if count_d == 0:
        res+=1
    if count_s == 0:
        res+=1
    
    if n + res < 6:
        res += n-res
        
    return res
    
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
