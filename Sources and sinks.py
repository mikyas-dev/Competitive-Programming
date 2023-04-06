from collections import defaultdict
import sys

n = int(sys.stdin.readline())


adj = defaultdict(set)



for i in range(n):
    arr = [int(x) for x in sys.stdin.readline().split()]
    for j in range( n):
        if arr[j] == 1:
            adj[i+1].add(j+1)
        if i+1 not in adj:
            adj[i+1] = set()        

source = []
sink = []
all = set()
for i in range(1, n+1):
    all.update(adj[i])
for i in range(1, n+1):
    if len(adj[i]) == 0:
        sink.append(i)
    if i not in all:
        source.append(i)

print(len(source),end=" ")
print(*source, sep=" ")
print(len(sink),end=" ")
print(*sink, sep=" ")
