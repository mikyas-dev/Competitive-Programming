import math


n = int(input())
for i in range(n):
    x = int(input())
    
    if x == 1:
        print(3)
    elif math.log2(x).is_integer():
        print(x+1)
    elif x % 2 == 0:
        print(x - (x&(x-1)))
    else:
        print(1)
