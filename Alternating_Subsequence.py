t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    total_sum = 0

    i = 0
    while i < n:
        cur = a[i]
        j = i
        while j < n and (a[i] > 0) == (a[j] > 0):
            cur = max(cur, a[j])
            j += 1
        total_sum += cur
        i = j

    print(total_sum)
    t -= 1
