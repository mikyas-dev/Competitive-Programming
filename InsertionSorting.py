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
    temp = arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i]>temp:
            arr[i+1]=arr[i]
            for y in arr:
                print(y,end=" ")
        else:
            arr[i+1]=temp
            for y in arr:
                print(y,end=" ")
            break
        if i == 0 and temp<arr[0]:
            arr[i]=temp
            print()
            for y in arr:
                print(y,end=" ")
            
        print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
