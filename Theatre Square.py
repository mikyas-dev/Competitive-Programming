import math
inp=input()
s =inp.split()
m=math.ceil(int(s[0])/int(s[-1]))
n=math.ceil(int(s[1])/int(s[-1]))
print(m*n)
