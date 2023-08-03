n = int(input())
one = 0
two = 0
for i in range(n):
    temp = [int(i) for i in input().split()]
    for j  in range(len(temp)):
        if i == j and temp[j] == 1:
            one += 1
        elif temp[j] == 1:
            two += 1
print(one + two//2)
