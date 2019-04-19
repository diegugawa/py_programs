#!/usr/bin/env python3

import os
import sys

#
# Complete the extremumPermutations function below.
#
def extremumPermutations(n, a, b):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkl = input().split()

    n = int(nkl[0])

    k = int(nkl[1])

    l = int(nkl[2])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = extremumPermutations(n, a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
