#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    x = arr[n-1]
    for j in range(1, n):
        if x<arr[n-j-1]:
            arr[n-j]=arr[n-j-1]
        else:
            arr[n-j]=x
        for y in arr:
            print(y,end=" ")
        if j==n-1 and x<arr[0]:
            arr[0]=x
            print()
            for y in arr:
                print(y,end=" ")
        if x>arr[n-j-1]:
            break
        print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
