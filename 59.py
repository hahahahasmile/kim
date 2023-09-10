#벨만포드 알고리즘 음수 사이클
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
edges = []
distance = [sys.maxsize]*(n+1)
for i in range(m):
    s,e,v = map(int,input().split())
    edges.append((s,e,v))

distance[1] = 0
for _ in range(n+1):
    for start,end,time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start]+time:
            distance[end] = distance[start]+time
mycycle = False
for start,end,time in edges:
    if distance[start] != sys.maxsize and distance[end]>distance[start]+time:
        mycycle = True

if not mycycle:
    for i in range(2,n+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)