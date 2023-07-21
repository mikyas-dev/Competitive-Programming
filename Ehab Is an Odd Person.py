n = int(input())
arr = list(map(int, input().split()))

ex = [False, False]

for i in range(n):
    ex[arr[i] % 2] = True

if ex[0] and ex[1]:
    arr.sort()

for i in range(n):
    print(arr[i], end=" ")
