#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    moves = {"no": n-r_q, "ne":min(n-r_q, n-c_q), "ea": n-c_q,
             "se": min(n-c_q, r_q-1), "so": r_q-1,
             "sw": min(r_q-1, c_q-1), "we": c_q-1,
             "nw": min(c_q-1, n-r_q)}
    
    for obs in obstacles:
        r = obs[0]
        c = obs[1]
    
        if c_q==c:
            if r > r_q:
                moves["no"] = min(r-r_q-1, moves["no"])
            else:
                moves["so"] = min(r_q-r-1, moves["so"])
        if c-c_q == r-r_q and c-c_q > 0:
            moves["ne"] = min(c-c_q-1, moves["ne"])
        if r == r_q:
            if c > c_q:
                moves["ea"] = min(c-c_q-1, moves["ea"])
            else:
                moves["we"] = min(c_q-c-1, moves["we"])
        if c-c_q == r_q-r and c-c_q > 0:
            moves["se"] = min(c-c_q-1, moves["se"])
        if r_q-r == c_q-c and r_q-r > 0:
            moves["sw"] = min(r_q-r-1, moves["sw"])
            # fptr.write(str("Q"))
        if r-r_q == c_q-c and r-r_q > 0:
            moves["nw"] = min(r-r_q-1, moves["nw"])
    
    return sum(moves.values())


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # second_multiple_input = input().rstrip().split()

    # r_q = int(second_multiple_input[0])

    # c_q = int(second_multiple_input[1])

    # obstacles = []

    # for _ in range(k):
    #     obstacles.append(list(map(int, input().rstrip().split())))

    # result = queensAttack(n, k, r_q, c_q, obstacles)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    s = ["a", "b", "c", "d", "e", "f", "g"]
    print()
    print(s[0:24])
