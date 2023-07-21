# Read n and k
n, k = map(int, input().split())

# Read the list a
a = list(map(int, input().split()))

# Sort the list
a.sort()

ans = 0

if k == 0:
    ans = a[0] - 1
else:
    ans = a[k - 1]

cnt = 0

for i in range(n):
    if a[i] <= ans:
        cnt += 1

if cnt != k or not (1 <= ans <= 1000 * 1000 * 1000):
    print("-1")
else:
    print(ans)
