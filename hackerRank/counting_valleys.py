#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
# n: the number of steps Gary takes
# s: a string describing his path
# if "seaLevel" is the same as the "valley". Then:

def countingValleys(n, s):
    seaLevel = valley = 0
    for step in s:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        if step == 'U' and seaLevel == 0:
            valley += 1
    return valley

# Test this by running these parameters with the inputs: 8 and "UDDDUDUU".
# Your result should be = 1, which is what HackerRank is looking for.

n = int(input('The number of steps Gary takes: ')) # 8
s = input('The string describing his path: ') # UDDDUDUU
print("The number of valleys is {}".format(countingValleys(n, s)))

# what's below is required by HackerRank to run the countingValleys function

'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
'''
