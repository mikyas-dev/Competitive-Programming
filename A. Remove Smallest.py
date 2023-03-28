n = int(input())

for i in range(n):
    l = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = True
    for j in range(l-1):
        if a[j+1] - a[j] > 1:
            ans = False
            break
    if ans:
        print("YES")
    else:    
        print("NO")
