#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from bisect import bisect_left

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here

    s = sum(s, [])

    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], 
      [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8], 
      [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6],
      [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    
    minimum_cost = sys.maxsize

    for mag in magic:
        diff = 0
        for i, j in zip(s, mag):
            diff += abs(s[i] - mag[j])
        minimum_cost = min(diff, minimum_cost)
    
    return minimum_cost

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = []

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    # result = formingMagicSquare(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    # s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # s = sum(s, [])
    # print(s)
    # # print(sys.maxsize)

    # alice = [5, 25, 50, 120]
    # scores = [100, 100, 50, 40, 40, 20, 10]
    # # counts [10, 20, 40, 50, 100]

    # counts = Counter(scores)
    # counts = sorted(counts)
    # print("counts", counts)
    # n = len(counts)
    # for a in alice:
    #     i = bisect_left(counts, a)
    #     print(a, i)
    #     # if i < n and counts[i] == a:
    #         # print()


    # scores = [10, 20, 30, 40, 90, 90, 100]
    # i = bisect_left(scores, 35)
    # print(i)






