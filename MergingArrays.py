n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# merge two sorted arrays
def merge(a, b):
    i = 0
    j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    if i < len(a):
        merged.extend(a[i:])
    if j < len(b):
        merged.extend(b[j:])
    return merged

print(*merge(a, b) , sep = " ")
