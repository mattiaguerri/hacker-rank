#!/bin/python3

from itertools import groupby
import math
import os
import random
import re
import sys

# Complete the substrCount function below.



# def check(st):
#     if len(st) % 2 == 1:
#         cent = len(st) // 2
#         st = st[:cent] + st[cent+1:]
#     if len(set(st)) == 1:
#         return 1
#     else:
#         return 0

# def substrCount(n, s):
#     count = 0
#     count += n
    
#     for i in range(2, n+1):
#         for j in range(0, n-i+1):
#             count += check(s[j:j+i])

#     return count



def k_sum(k):
    return (k*(k+1))//2

def substrCount(n, s):
    case_a = 0
    case_b = 0
    for x,y in groupby(s):
        case_a += k_sum(sum(1 for i in y))
    for i in range(1,len(s)-1):
        skip = 1
        if s[i-skip] == s[i] or s[i+skip] == s[i]:
            continue
        match = s[i-skip]
        while i-skip>-1 and i+skip<len(s) and s[i-skip]==match and s[i+skip]==match:
            case_b += 1
            skip += 1
    return case_a + case_b



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 7

    s = "abcbaba"

    result = substrCount(n, s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
