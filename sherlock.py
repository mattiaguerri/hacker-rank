#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    dct = {s[0]: 1}
    for i in s[1:]:
        if i not in dct.keys():
            dct[i] = 1
        else:
            dct[i] += 1
    lst = list(dct.values())
    lst = list(set(lst))
    
    if len(lst) == 1:
        res = "YES"
    
    if len(lst) > 2:
        res = "NO"
    
    if len(lst) == 2:
        ma = max(list(dct.values()))
        mi = min(list(dct.values()))    
        if ma - mi > 1:
            res = "NO"
        elif ma - mi == 1:
            count = 0
            for num in list(dct.values()):
                if num == ma:
                    count+=1
            if count == 1:
                res = "YES"
            else:
                res = "NO"
    

    return res
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
