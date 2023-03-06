inputs = int(input())
for i in range(inputs):
    a,b = map(int,input().split())
    check = min(a,b)
    low = 0
    ans = high = (a+b)//4
    while low <= high:
        mid = (low+high)//2

        if mid < check:
            low = mid + 1
        elif mid > check:
            high = mid - 1
        else:
            ans = mid
            break
    print(ans)
 
